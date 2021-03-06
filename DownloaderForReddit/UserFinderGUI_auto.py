# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserFinder.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_user_finder_widget(object):
    def setupUi(self, user_finder_widget):
        user_finder_widget.setObjectName("user_finder_widget")
        user_finder_widget.resize(494, 492)
        user_finder_widget.setMinimumSize(QtCore.QSize(494, 492))
        font = QtGui.QFont()
        font.setPointSize(10)
        user_finder_widget.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/magnifying_glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        user_finder_widget.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(user_finder_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.page_change_left_button = QtWidgets.QToolButton(user_finder_widget)
        self.page_change_left_button.setText("")
        self.page_change_left_button.setArrowType(QtCore.Qt.LeftArrow)
        self.page_change_left_button.setObjectName("page_change_left_button")
        self.gridLayout.addWidget(self.page_change_left_button, 0, 0, 1, 1)
        self.close_dialog_button = QtWidgets.QPushButton(user_finder_widget)
        self.close_dialog_button.setObjectName("close_dialog_button")
        self.gridLayout.addWidget(self.close_dialog_button, 0, 2, 1, 1)
        self.stacked_widget = QtWidgets.QStackedWidget(user_finder_widget)
        self.stacked_widget.setObjectName("stacked_widget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.page)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.watchlist_add_subreddit_button_2 = QtWidgets.QToolButton(self.page)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.watchlist_add_subreddit_button_2.setFont(font)
        self.watchlist_add_subreddit_button_2.setObjectName("watchlist_add_subreddit_button_2")
        self.horizontalLayout.addWidget(self.watchlist_add_subreddit_button_2)
        self.watchlist_remove_subreddit_button_2 = QtWidgets.QToolButton(self.page)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.watchlist_remove_subreddit_button_2.setFont(font)
        self.watchlist_remove_subreddit_button_2.setObjectName("watchlist_remove_subreddit_button_2")
        self.horizontalLayout.addWidget(self.watchlist_remove_subreddit_button_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.blacklist_user_add_button_2 = QtWidgets.QToolButton(self.page)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.blacklist_user_add_button_2.setFont(font)
        self.blacklist_user_add_button_2.setObjectName("blacklist_user_add_button_2")
        self.horizontalLayout_2.addWidget(self.blacklist_user_add_button_2)
        self.blacklist_user_remove_button_2 = QtWidgets.QToolButton(self.page)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.blacklist_user_remove_button_2.setFont(font)
        self.blacklist_user_remove_button_2.setObjectName("blacklist_user_remove_button_2")
        self.horizontalLayout_2.addWidget(self.blacklist_user_remove_button_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.sub_watchlist_listview = QtWidgets.QListWidget(self.page)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.sub_watchlist_listview.setFont(font)
        self.sub_watchlist_listview.setObjectName("sub_watchlist_listview")
        self.gridLayout_2.addWidget(self.sub_watchlist_listview, 1, 0, 1, 1)
        self.blacklist_users_listview = QtWidgets.QListWidget(self.page)
        self.blacklist_users_listview.setObjectName("blacklist_users_listview")
        self.gridLayout_2.addWidget(self.blacklist_users_listview, 1, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_2, 0, 0, 3, 2)
        self.run_finder_button_2 = QtWidgets.QPushButton(self.page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.run_finder_button_2.setFont(font)
        self.run_finder_button_2.setObjectName("run_finder_button_2")
        self.gridLayout_7.addWidget(self.run_finder_button_2, 2, 2, 1, 3)
        self.line_3 = QtWidgets.QFrame(self.page)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_7.addWidget(self.line_3, 3, 0, 1, 5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.page)
        self.groupBox_6.setMaximumSize(QtCore.QSize(16777215, 115))
        self.groupBox_6.setObjectName("groupBox_6")
        self.automatically_add_user_checkbox = QtWidgets.QCheckBox(self.groupBox_6)
        self.automatically_add_user_checkbox.setGeometry(QtCore.QRect(10, 30, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.automatically_add_user_checkbox.setFont(font)
        self.automatically_add_user_checkbox.setObjectName("automatically_add_user_checkbox")
        self.watchlist_download_sample_spinbox_2 = QtWidgets.QSpinBox(self.groupBox_6)
        self.watchlist_download_sample_spinbox_2.setGeometry(QtCore.QRect(150, 80, 42, 20))
        self.watchlist_download_sample_spinbox_2.setObjectName("watchlist_download_sample_spinbox_2")
        self.label_9 = QtWidgets.QLabel(self.groupBox_6)
        self.label_9.setGeometry(QtCore.QRect(200, 70, 47, 31))
        self.label_9.setObjectName("label_9")
        self.line_4 = QtWidgets.QFrame(self.groupBox_6)
        self.line_4.setGeometry(QtCore.QRect(250, 20, 20, 81))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.watchlist_when_run_checkbox_2 = QtWidgets.QCheckBox(self.groupBox_6)
        self.watchlist_when_run_checkbox_2.setGeometry(QtCore.QRect(270, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.watchlist_when_run_checkbox_2.setFont(font)
        self.watchlist_when_run_checkbox_2.setObjectName("watchlist_when_run_checkbox_2")
        self.watchlist_add_to_list_combo_2 = QtWidgets.QComboBox(self.groupBox_6)
        self.watchlist_add_to_list_combo_2.setGeometry(QtCore.QRect(270, 70, 181, 21))
        self.watchlist_add_to_list_combo_2.setObjectName("watchlist_add_to_list_combo_2")
        self.label_10 = QtWidgets.QLabel(self.groupBox_6)
        self.label_10.setGeometry(QtCore.QRect(270, 50, 211, 20))
        self.label_10.setObjectName("label_10")
        self.label = QtWidgets.QLabel(self.groupBox_6)
        self.label.setGeometry(QtCore.QRect(10, 80, 131, 16))
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.groupBox_6, 5, 0, 1, 5)
        self.watchlist_score_spinbox_2 = QtWidgets.QSpinBox(self.page)
        self.watchlist_score_spinbox_2.setMaximum(1000000000)
        self.watchlist_score_spinbox_2.setObjectName("watchlist_score_spinbox_2")
        self.gridLayout_7.addWidget(self.watchlist_score_spinbox_2, 4, 1, 1, 1)
        self.top_sort_groupbox = QtWidgets.QGroupBox(self.page)
        self.top_sort_groupbox.setObjectName("top_sort_groupbox")
        self.sub_sort_day_radio = QtWidgets.QRadioButton(self.top_sort_groupbox)
        self.sub_sort_day_radio.setGeometry(QtCore.QRect(10, 50, 131, 17))
        self.sub_sort_day_radio.setObjectName("sub_sort_day_radio")
        self.sub_sort_week_radio = QtWidgets.QRadioButton(self.top_sort_groupbox)
        self.sub_sort_week_radio.setGeometry(QtCore.QRect(10, 70, 151, 17))
        self.sub_sort_week_radio.setObjectName("sub_sort_week_radio")
        self.sub_sort_month_radio = QtWidgets.QRadioButton(self.top_sort_groupbox)
        self.sub_sort_month_radio.setGeometry(QtCore.QRect(10, 90, 82, 17))
        self.sub_sort_month_radio.setObjectName("sub_sort_month_radio")
        self.sub_sort_year_radio = QtWidgets.QRadioButton(self.top_sort_groupbox)
        self.sub_sort_year_radio.setGeometry(QtCore.QRect(10, 110, 82, 17))
        self.sub_sort_year_radio.setObjectName("sub_sort_year_radio")
        self.sub_sort_all_raido = QtWidgets.QRadioButton(self.top_sort_groupbox)
        self.sub_sort_all_raido.setGeometry(QtCore.QRect(10, 130, 82, 17))
        self.sub_sort_all_raido.setObjectName("sub_sort_all_raido")
        self.sub_sort_hour_radio = QtWidgets.QRadioButton(self.top_sort_groupbox)
        self.sub_sort_hour_radio.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.sub_sort_hour_radio.setObjectName("sub_sort_hour_radio")
        self.gridLayout_7.addWidget(self.top_sort_groupbox, 0, 3, 2, 1)
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 4, 0, 1, 1)
        self.stacked_widget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.found_user_list = QtWidgets.QListWidget(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.found_user_list.sizePolicy().hasHeightForWidth())
        self.found_user_list.setSizePolicy(sizePolicy)
        self.found_user_list.setMaximumSize(QtCore.QSize(119, 16777215))
        self.found_user_list.setObjectName("found_user_list")
        self.gridLayout_8.addWidget(self.found_user_list, 2, 0, 1, 1)
        self.add_selected_button = QtWidgets.QPushButton(self.page_2)
        self.add_selected_button.setObjectName("add_selected_button")
        self.gridLayout_8.addWidget(self.add_selected_button, 0, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.content_display_list = QtWidgets.QListWidget(self.page_2)
        self.content_display_list.setResizeMode(QtWidgets.QListView.Adjust)
        self.content_display_list.setViewMode(QtWidgets.QListView.IconMode)
        self.content_display_list.setWordWrap(True)
        self.content_display_list.setObjectName("content_display_list")
        self.gridLayout_9.addWidget(self.content_display_list, 0, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 1, 1, 1)
        self.stacked_widget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.progress_bar = QtWidgets.QProgressBar(self.page_3)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.gridLayout_3.addWidget(self.progress_bar, 0, 0, 1, 1)
        self.found_user_output = QtWidgets.QTextBrowser(self.page_3)
        self.found_user_output.setObjectName("found_user_output")
        self.gridLayout_3.addWidget(self.found_user_output, 2, 0, 1, 1)
        self.found_users_label = QtWidgets.QLabel(self.page_3)
        self.found_users_label.setObjectName("found_users_label")
        self.gridLayout_3.addWidget(self.found_users_label, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.stacked_widget.addWidget(self.page_3)
        self.gridLayout.addWidget(self.stacked_widget, 2, 0, 1, 3)
        self.page_change_right_button = QtWidgets.QToolButton(user_finder_widget)
        self.page_change_right_button.setText("")
        self.page_change_right_button.setIconSize(QtCore.QSize(16, 16))
        self.page_change_right_button.setArrowType(QtCore.Qt.RightArrow)
        self.page_change_right_button.setObjectName("page_change_right_button")
        self.gridLayout.addWidget(self.page_change_right_button, 0, 1, 1, 1)
        self.button_box = QtWidgets.QDialogButtonBox(user_finder_widget)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.gridLayout.addWidget(self.button_box, 3, 2, 1, 1)

        self.retranslateUi(user_finder_widget)
        self.stacked_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(user_finder_widget)

    def retranslateUi(self, user_finder_widget):
        _translate = QtCore.QCoreApplication.translate
        user_finder_widget.setWindowTitle(_translate("user_finder_widget", "User Finder"))
        self.close_dialog_button.setToolTip(_translate("user_finder_widget", "Add any of the found users to the main window list or make any other changes you would like and then close this dialog to proceed with the download"))
        self.close_dialog_button.setText(_translate("user_finder_widget", "Close This Dialog to Continue Download"))
        self.label_7.setText(_translate("user_finder_widget", "Subreddit Watchlist"))
        self.label_8.setText(_translate("user_finder_widget", "User Blacklist"))
        self.watchlist_add_subreddit_button_2.setText(_translate("user_finder_widget", "+"))
        self.watchlist_remove_subreddit_button_2.setText(_translate("user_finder_widget", "-"))
        self.blacklist_user_add_button_2.setText(_translate("user_finder_widget", "+"))
        self.blacklist_user_remove_button_2.setText(_translate("user_finder_widget", "-"))
        self.run_finder_button_2.setText(_translate("user_finder_widget", "Run User Finder Only"))
        self.groupBox_6.setTitle(_translate("user_finder_widget", "When Criteria Met"))
        self.automatically_add_user_checkbox.setText(_translate("user_finder_widget", "Automatically add found users to list"))
        self.label_9.setText(_translate("user_finder_widget", "posts"))
        self.watchlist_when_run_checkbox_2.setToolTip(_translate("user_finder_widget", "<html><head/><body><p><span style=\" font-size:10pt;\">If this is checked, this portion of the program will run when whenever the main program is run</span></p></body></html>"))
        self.watchlist_when_run_checkbox_2.setText(_translate("user_finder_widget", "Run when main app runs"))
        self.label_10.setText(_translate("user_finder_widget", "Main window user list to add to"))
        self.label.setText(_translate("user_finder_widget", "Download Sample of:"))
        self.top_sort_groupbox.setTitle(_translate("user_finder_widget", "Sort Top Posts By"))
        self.sub_sort_day_radio.setText(_translate("user_finder_widget", "Day"))
        self.sub_sort_week_radio.setText(_translate("user_finder_widget", "Week"))
        self.sub_sort_month_radio.setText(_translate("user_finder_widget", "Month"))
        self.sub_sort_year_radio.setText(_translate("user_finder_widget", "Year"))
        self.sub_sort_all_raido.setText(_translate("user_finder_widget", "All Time"))
        self.sub_sort_hour_radio.setText(_translate("user_finder_widget", "Hour"))
        self.label_2.setText(_translate("user_finder_widget", "Posts must meet this score:"))
        self.add_selected_button.setToolTip(_translate("user_finder_widget", "Adds the selected users to the main window list defined on page one (the users will be removed from the list)"))
        self.add_selected_button.setText(_translate("user_finder_widget", "Add Selected"))
        self.found_users_label.setText(_translate("user_finder_widget", "TextLabel"))

