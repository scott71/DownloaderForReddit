"""
Downloader for Reddit takes a list of reddit users and subreddits and downloads content posted to reddit either by the
users or on the subreddits.


Copyright (C) 2017, Kyle Hickey


This file is part of the Downloader for Reddit.

Downloader for Reddit is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Downloader for Reddit is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Downloader for Reddit.  If not, see <http://www.gnu.org/licenses/>.
"""


import praw
import prawcore
from PyQt5.QtCore import QObject, pyqtSignal, QThreadPool


class RedditExtractor(QObject):

    remove_invalid_user = pyqtSignal(object)
    remove_invalid_subreddit = pyqtSignal(object)
    finished = pyqtSignal()
    downloaded_users_signal = pyqtSignal(list)
    unfinished_downloads_signal = pyqtSignal(list)
    status_bar_update = pyqtSignal(str)
    update_download_count = pyqtSignal()

    def __init__(self, user_list, subreddit_list, queue, post_limit, save_path, subreddit_sort_method,
                 subreddit_sort_top_method, restrict_date, restrict_by_score, restrict_score_method,
                 restrict_score_limit, unfinished_downloads_list):
        """
        Class that does the main part of the work for the program.  This class contains the praw instance that is used
        for actually extracting the content from reddit.  When an instance is created all settings parameters must be
        supplied to the instance.  This class also calls the necessary functions of the other classes and completes the
        downloads.

        :param user_list: The actual list of User objects contained in the user ListModel class displayed in the GUI
        :param subreddit_list: The actual list of Subreddit objects contained in the subreddit ListModel class displayed
                               in the GUI. If this class is initialized to only run a user list, this parameter is None
        :param queue: The queue that text is added to in order to update the GUI
        The rest of teh parameters are all configuration options that are set in the settings dialog
        """
        super().__init__()
        self._r = praw.Reddit(user_agent="python:DownloaderForReddit:V1.0 (by /u/MalloyDelacroix)",
                              client_id='frGEUVAuHGL2PQ', client_secret=None)
        self.user_list = user_list
        self.subreddit_list = subreddit_list
        self.queue = queue
        self.validated_users = []
        self.validated_subreddits = []
        self.failed_downloads = []
        self.downloaded_users = []
        self.unfinished_downloads = []

        self.post_limit = post_limit
        self.save_path = save_path
        self.subreddit_sort_method = subreddit_sort_method
        self.subreddit_sort_top_method = subreddit_sort_top_method
        self.restrict_date = restrict_date
        self.restrict_by_score = restrict_by_score
        self.restrict_score_method = restrict_score_method
        self.restrict_score_limit = restrict_score_limit
        self.unfinished_downloads_list = unfinished_downloads_list

        self.queued_posts = []
        self.run = True

        self.download_pool = QThreadPool()
        self.download_pool.setMaxThreadCount(4)

    def validate_users(self):
        """Validates users and builds a list of all posts to reddit that meet the user provided criteria"""
        self.status_bar_update.emit('Validating Users...')
        for user in self.user_list:
            redditor = self._r.redditor(user.name)
            try:
                test = redditor.fullname
            except (prawcore.exceptions.Redirect, prawcore.exceptions.NotFound):
                redditor = None
                self.remove_invalid_user.emit(user)

            if redditor is not None:
                self.queue.put("%s is valid" % user.name)
                # Sets date limit according to settings GUI
                if not self.restrict_date:
                    date_limit = 1
                elif user.custom_date_limit is not None:
                    date_limit = user.custom_date_limit
                else:
                    date_limit = user.date_limit
                post_limit = user.post_limit
                submissions = self.get_submissions_user(redditor, date_limit, post_limit)
                user.get_new_submissions(submissions)
                self.validated_users.append(user)
                user.check_save_path()
            else:
                self.queue.put("%s does not exist" % user.name)

        self.run_user()

    def validate_subreddits(self):
        """See validate_users"""
        self.status_bar_update.emit('Validating Subreddits...')
        for sub in self.subreddit_list:
            subreddit = self._r.subreddit(sub.name)
            try:
                test = subreddit.fullname
            except (prawcore.exceptions.Redirect, prawcore.exceptions.NotFound):
                subreddit = None
                self.remove_invalid_subreddit.emit(sub)

            if subreddit is not None:
                self.queue.put("%s is valid" % sub.name)
                date_limit = sub.date_limit if self.restrict_date else 1
                post_limit = sub.post_limit
                submissions = self.get_submissions_subreddit(subreddit, date_limit, post_limit)
                sub.get_new_submissions(submissions)
                self.validated_subreddits.append(sub)
            else:
                self.queue.put("%s is not a valid subreddit" % sub.name)
        self.run_subreddit()

    def validate_users_and_subreddits(self):
        """See validate_users"""
        self.status_bar_update.emit('Validating Subreddits...')
        for sub in self.subreddit_list:
            try:
                subreddit = self._r.subreddit(sub.name)
                self.validated_subreddits.append(subreddit.display_name)
                self.queue.put("%s is a valid subreddit" % subreddit.display_name)
            except (prawcore.exceptions.Redirect, prawcore.exceptions.NotFound):
                self.queue.put("%s is not valid" % sub.name)

        self.status_bar_update.emit('Validating Users...')
        for user in self.user_list:
            redditor = self._r.redditor(user.name)
            try:
                test = redditor.fullname
            except prawcore.exceptions.NotFound:
                redditor = None
                self.queue.put('%s is not valid' % user.name)

            if redditor is not None:
                self.queue.put('%s is a valid user' % user.name)
                submissions = [x for x in redditor.get_submitted(limit=self.post_limit) if x.created > user.date_limit
                               and x.subreddit.display_name in self.validated_subreddits]
                user.get_new_submissions(submissions)
                self.validated_users.append(user)
                user.check_save_path()
        self.run_user()

    def run_user(self):
        """
        Handles calling the appropriate functions to extract the content from the users reddit links and download
        the content
        """
        self.status_bar_update.emit('Extracting User Content...')
        for user in self.validated_users:
            user.extract_content()
            if len(user.failed_extracts) > 0:
                for entry in user.failed_extracts:
                    self.queue.put(entry)

        for user in self.validated_users:
            if len(user.content) > 0:
                self.downloaded_users.append(user.name)
            for post in user.content:
                post.install_queue(self.queue)
                self.queued_posts.append(post)

        self.status_bar_update.emit('Downloaded: 0  of  %s' % len(self.queued_posts))
        self.queue.put(' ')  # Adds some small separation in the output box between users being validated and downloaded
        self.download_posts()
        for user in self.validated_users:
            user.clear_download_session_data()
        self.queue.put('\nFinished')
        self.send_unfinished_downloads()
        self.send_downloaded_users()
        self.finished.emit()

    def run_subreddit(self):
        """See run_user"""
        self.status_bar_update.emit('Extracting Subreddit Content...')
        for sub in self.validated_subreddits:
            sub.extract_content()
            if len(sub.failed_extracts) > 0:
                for entry in sub.failed_extracts:
                    self.queue.put(entry)

        for sub in self.validated_subreddits:
            for post in sub.content:
                post.install_queue(self.queue)  # Gives each QRunnable an instance of the main queue to update the GUI
                self.queued_posts.append(post)

        self.status_bar_update.emit('Downloaded: 0  of  %s' % len(self.queued_posts))
        self.queue.put(' ')  # Adds some small separation in the output box between users being validated and downloaded
        self.download_posts()
        for sub in self.validated_subreddits:
            sub.clear_download_session_data()
        self.queue.put('\nFinished')
        self.send_unfinished_downloads()
        self.finished.emit()

    def download_posts(self):
        """Pulls from the list of extracted content and spawns threads to download multiple links simultaneously"""
        for post in self.queued_posts:
            if self.run:
                self.download_pool.start(post)
        self.download_pool.waitForDone()

    def get_submissions_user(self, user, date_limit, post_limit):  # 0 = greater than, 1 = less than
        """Extracts user submissions from reddit if they meet the user provided criteria"""
        if self.restrict_by_score and self.restrict_score_method == 0:
            submissions = [x for x in user.submissions.new(limit=post_limit) if x.created > date_limit and not
                           x.is_self and x.score > self.restrict_score_limit]
        elif self.restrict_by_score and self.restrict_score_method == 1:
            submissions = [x for x in user.submissions.new(limit=post_limit) if x.created > date_limit and not
                           x.is_self and x.score < self.restrict_score_limit]
        else:
            submissions = [x for x in user.submissions.new(limit=post_limit) if x.created > date_limit and not
                           x.is_self]
        return submissions

    def get_submissions_subreddit(self, subreddit, date_limit, post_limit):
        """See get_submissions_user"""
        if self.subreddit_sort_method != 0:
            date_limit = 1
        if self.restrict_by_score and self.restrict_score_method == 0:
            submissions = [x for x in self.sub_sort(subreddit, post_limit) if not x.is_self and x.score >
                           self.restrict_score_limit and x.created > date_limit]
        elif self.restrict_by_score and self.restrict_score_method == 1:
            submissions = [x for x in self.sub_sort(subreddit, post_limit) if not x.is_self and x.score <
                           self.restrict_score_limit and x.created > date_limit]
        else:
            submissions = [x for x in self.sub_sort(subreddit, post_limit) if not x.is_self and x.created > date_limit]
        return submissions

    def sub_sort(self, sub, post_limit):  # new: 0, top: 1, hot: 2, rising: 3, controversial: 4
        sort = self.subreddit_sort_method
        if sort == 0:
            posts = sub.new(limit=post_limit)
        elif sort == 2:
            posts = sub.hot(limit=post_limit)
        elif sort == 3:
            posts = sub.rising(limit=post_limit)
        elif sort == 4:
            posts = sub.controversial(limit=post_limit)
        else:
            top_sort = self.subreddit_sort_top_method
            if top_sort == 0:
                posts = sub.top('hour', limit=post_limit)
            elif top_sort == 1:
                posts = sub.top('day', limit=post_limit)
            elif top_sort == 2:
                posts = sub.top('week', limit=post_limit)
            elif top_sort == 3:
                posts = sub.top('month', limit=post_limit)
            elif top_sort == 4:
                posts = sub.top('year', limit=post_limit)
            else:
                posts = sub.top('all', limit=post_limit)
        return posts

    def send_downloaded_users(self):
        self.downloaded_users_signal.emit(self.downloaded_users)

    def stop_download(self):
        self.run = False
        # print('Active thread count: %s' % self.download_pool.activeThreadCount())
        self.download_pool.clear()
        # print('len of queued posts: %s' % len(self.queued_posts))
        self.queue.put('\nStopped\n')
        # print('queued posts not downloaded: %s' % len([x for x in self.queued_posts if not x.downloaded]))

    def send_unfinished_downloads(self):
        unfinished_list = [x for x in self.queued_posts if not x.downloaded]
        if len(unfinished_list) > 0:
            self.unfinished_downloads_signal.emit(unfinished_list)

    def finish_downloads(self):
        self.queued_posts = self.unfinished_downloads_list
        self.status_bar_update.emit('Downloaded: 0  of  %s' % len(self.queued_posts))
        self.download_posts()
        self.queue.put('\nFinished')
        self.finished.emit()

    def skip_user_validation(self):
        self.validated_users = self.user_list
