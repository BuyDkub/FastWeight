# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/B/Documents/maya/2019/scripts/fast_weight_gui/GUI/fast_weight_beta02.ui'
#
# Created: Fri Dec 18 16:47:22 2020
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(461, 767)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -20, 461, 801))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 441, 761))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.object_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.object_label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.object_label.setObjectName("object_label")
        self.horizontalLayout_8.addWidget(self.object_label)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox)
        self.Add_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Add_pushButton.setMinimumSize(QtCore.QSize(50, 10))
        self.Add_pushButton.setObjectName("Add_pushButton")
        self.horizontalLayout_8.addWidget(self.Add_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setContentsMargins(10, -1, 10, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.hideDup_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hideDup_pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.hideDup_pushButton.setObjectName("hideDup_pushButton")
        self.horizontalLayout_11.addWidget(self.hideDup_pushButton)
        self.hideModel_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hideModel_pushButton.setObjectName("hideModel_pushButton")
        self.horizontalLayout_11.addWidget(self.hideModel_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 160))
        self.groupBox.setObjectName("groupBox")
        self.treeWidget = QtWidgets.QTreeWidget(self.groupBox)
        self.treeWidget.setGeometry(QtCore.QRect(10, 20, 421, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setObjectName("treeWidget")
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(7)
        self.horizontalLayout_12.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.clear_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.clear_pushButton.setObjectName("clear_pushButton")
        self.horizontalLayout_12.addWidget(self.clear_pushButton)
        self.takeOut_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.takeOut_pushButton.setObjectName("takeOut_pushButton")
        self.horizontalLayout_12.addWidget(self.takeOut_pushButton)
        self.delete_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.delete_pushButton.setObjectName("delete_pushButton")
        self.horizontalLayout_12.addWidget(self.delete_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 350))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.tab_4)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 431, 411))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Create_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.Create_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.Create_pushButton.setObjectName("Create_pushButton")
        self.verticalLayout_5.addWidget(self.Create_pushButton)
        self.duplicate_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.duplicate_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.duplicate_pushButton.setObjectName("duplicate_pushButton")
        self.verticalLayout_5.addWidget(self.duplicate_pushButton)
        self.transfer_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.transfer_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.transfer_pushButton.setObjectName("transfer_pushButton")
        self.verticalLayout_5.addWidget(self.transfer_pushButton)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Create_blog_pushButton = QtWidgets.QPushButton(self.tab)
        self.Create_blog_pushButton.setGeometry(QtCore.QRect(10, 120, 411, 61))
        self.Create_blog_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.Create_blog_pushButton.setObjectName("Create_blog_pushButton")
        self.joint_comboBox = QtWidgets.QComboBox(self.tab)
        self.joint_comboBox.setGeometry(QtCore.QRect(150, 60, 181, 22))
        self.joint_comboBox.setObjectName("joint_comboBox")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(90, 60, 71, 21))
        self.label.setObjectName("label")
        self.cut_pushButton = QtWidgets.QPushButton(self.tab)
        self.cut_pushButton.setGeometry(QtCore.QRect(10, 210, 411, 41))
        self.cut_pushButton.setObjectName("cut_pushButton")
        self.setWeight_pushButton = QtWidgets.QPushButton(self.tab)
        self.setWeight_pushButton.setGeometry(QtCore.QRect(10, 270, 411, 41))
        self.setWeight_pushButton.setObjectName("setWeight_pushButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.duplicate2_pushButton = QtWidgets.QPushButton(self.tab_2)
        self.duplicate2_pushButton.setGeometry(QtCore.QRect(10, 50, 411, 50))
        self.duplicate2_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.duplicate2_pushButton.setObjectName("duplicate2_pushButton")
        self.setting_groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.setting_groupBox.setGeometry(QtCore.QRect(0, 120, 431, 281))
        self.setting_groupBox.setObjectName("setting_groupBox")
        self.reset_Button = QtWidgets.QPushButton(self.setting_groupBox)
        self.reset_Button.setGeometry(QtCore.QRect(320, 240, 93, 28))
        self.reset_Button.setObjectName("reset_Button")
        self.Outward_Constraint_lineEdit = QtWidgets.QLineEdit(self.setting_groupBox)
        self.Outward_Constraint_lineEdit.setGeometry(QtCore.QRect(140, 190, 61, 22))
        self.Outward_Constraint_lineEdit.setObjectName("Outward_Constraint_lineEdit")
        self.Envelope_setting_label = QtWidgets.QLabel(self.setting_groupBox)
        self.Envelope_setting_label.setGeometry(QtCore.QRect(70, 30, 81, 21))
        self.Envelope_setting_label.setObjectName("Envelope_setting_label")
        self.Inward_constraint_lineEdit = QtWidgets.QLineEdit(self.setting_groupBox)
        self.Inward_constraint_lineEdit.setGeometry(QtCore.QRect(140, 150, 61, 22))
        self.Inward_constraint_lineEdit.setObjectName("Inward_constraint_lineEdit")
        self.Envelope_setting_lineEdit = QtWidgets.QLineEdit(self.setting_groupBox)
        self.Envelope_setting_lineEdit.setGeometry(QtCore.QRect(140, 30, 61, 22))
        self.Envelope_setting_lineEdit.setObjectName("Envelope_setting_lineEdit")
        self.Smoothing_Interations_lineEdit = QtWidgets.QLineEdit(self.setting_groupBox)
        self.Smoothing_Interations_lineEdit.setGeometry(QtCore.QRect(140, 70, 61, 22))
        self.Smoothing_Interations_lineEdit.setObjectName("Smoothing_Interations_lineEdit")
        self.Smoothing_Interations_label = QtWidgets.QLabel(self.setting_groupBox)
        self.Smoothing_Interations_label.setGeometry(QtCore.QRect(0, 70, 161, 21))
        self.Smoothing_Interations_label.setObjectName("Smoothing_Interations_label")
        self.Outward_Constraint_label = QtWidgets.QLabel(self.setting_groupBox)
        self.Outward_Constraint_label.setGeometry(QtCore.QRect(10, 190, 151, 21))
        self.Outward_Constraint_label.setObjectName("Outward_Constraint_label")
        self.Smoothing_step_setting_label = QtWidgets.QLabel(self.setting_groupBox)
        self.Smoothing_step_setting_label.setGeometry(QtCore.QRect(30, 110, 121, 21))
        self.Smoothing_step_setting_label.setObjectName("Smoothing_step_setting_label")
        self.Inward_constraint_label = QtWidgets.QLabel(self.setting_groupBox)
        self.Inward_constraint_label.setGeometry(QtCore.QRect(20, 150, 131, 21))
        self.Inward_constraint_label.setObjectName("Inward_constraint_label")
        self.Smoothing_step_setting_lineEdit = QtWidgets.QLineEdit(self.setting_groupBox)
        self.Smoothing_step_setting_lineEdit.setGeometry(QtCore.QRect(140, 110, 61, 22))
        self.Smoothing_step_setting_lineEdit.setObjectName("Smoothing_step_setting_lineEdit")
        self.envelope_Slider = QtWidgets.QSlider(self.setting_groupBox)
        self.envelope_Slider.setGeometry(QtCore.QRect(210, 30, 201, 22))
        self.envelope_Slider.setMaximum(1)
        self.envelope_Slider.setProperty("value", 1)
        self.envelope_Slider.setSliderPosition(1)
        self.envelope_Slider.setTracking(True)
        self.envelope_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.envelope_Slider.setObjectName("envelope_Slider")
        self.smooothing_interations_Slider = QtWidgets.QSlider(self.setting_groupBox)
        self.smooothing_interations_Slider.setGeometry(QtCore.QRect(210, 70, 201, 22))
        self.smooothing_interations_Slider.setMaximum(200)
        self.smooothing_interations_Slider.setProperty("value", 25)
        self.smooothing_interations_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.smooothing_interations_Slider.setObjectName("smooothing_interations_Slider")
        self.smooothing_step_Slider = QtWidgets.QSlider(self.setting_groupBox)
        self.smooothing_step_Slider.setGeometry(QtCore.QRect(210, 110, 201, 22))
        self.smooothing_step_Slider.setMaximum(1)
        self.smooothing_step_Slider.setSliderPosition(1)
        self.smooothing_step_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.smooothing_step_Slider.setObjectName("smooothing_step_Slider")
        self.inward_Slider = QtWidgets.QSlider(self.setting_groupBox)
        self.inward_Slider.setGeometry(QtCore.QRect(210, 150, 201, 22))
        self.inward_Slider.setMaximum(1)
        self.inward_Slider.setPageStep(10)
        self.inward_Slider.setProperty("value", 1)
        self.inward_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.inward_Slider.setObjectName("inward_Slider")
        self.outward_Slider = QtWidgets.QSlider(self.setting_groupBox)
        self.outward_Slider.setGeometry(QtCore.QRect(210, 190, 201, 22))
        self.outward_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.outward_Slider.setObjectName("outward_Slider")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.transform_pushButton = QtWidgets.QPushButton(self.tab_3)
        self.transform_pushButton.setGeometry(QtCore.QRect(10, 80, 411, 50))
        self.transform_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.transform_pushButton.setObjectName("transform_pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 190, 431, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.transfer2_pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.transfer2_pushButton.setGeometry(QtCore.QRect(10, 90, 411, 50))
        self.transfer2_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.transfer2_pushButton.setObjectName("transfer2_pushButton")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 25, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.weight_comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.weight_comboBox.setGeometry(QtCore.QRect(80, 30, 331, 31))
        self.weight_comboBox.setObjectName("weight_comboBox")
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 461, 26))
        self.menubar.setObjectName("menubar")
        self.menuedit = QtWidgets.QMenu(self.menubar)
        self.menuedit.setObjectName("menuedit")
        self.menusetting = QtWidgets.QMenu(self.menubar)
        self.menusetting.setObjectName("menusetting")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionReset_Tool = QtWidgets.QAction(MainWindow)
        self.actionReset_Tool.setObjectName("actionReset_Tool")
        self.menuedit.addAction(self.actionReset_Tool)
        self.menubar.addAction(self.menuedit.menuAction())
        self.menubar.addAction(self.menusetting.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.object_label.setText(QtWidgets.QApplication.translate("MainWindow", "Object : >>", None, -1))
        self.comboBox.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "All", None, -1))
        self.comboBox.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Model", None, -1))
        self.comboBox.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "Extent Box", None, -1))
        self.comboBox.setItemText(3, QtWidgets.QApplication.translate("MainWindow", "Joint", None, -1))
        self.comboBox.setItemText(4, QtWidgets.QApplication.translate("MainWindow", "Model Duplicated", None, -1))
        self.comboBox.setItemText(5, QtWidgets.QApplication.translate("MainWindow", "Model Cut", None, -1))
        self.comboBox.setItemText(6, QtWidgets.QApplication.translate("MainWindow", "Joint Duplicated", None, -1))
        self.Add_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Add", None, -1))
        self.hideDup_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "hide Model_dup", None, -1))
        self.hideModel_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "hide model", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", " List Object", None, -1))
        self.treeWidget.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "All", None, -1))
        self.clear_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "clear", None, -1))
        self.takeOut_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "take out", None, -1))
        self.delete_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "delete", None, -1))
        self.Create_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Create Extent Box", None, -1))
        self.duplicate_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Duplicate", None, -1))
        self.transfer_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Transfer", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtWidgets.QApplication.translate("MainWindow", "Fast Weight", None, -1))
        self.Create_blog_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Create Extent Box", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Joint >>", None, -1))
        self.cut_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Calculate", None, -1))
        self.setWeight_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Set Skin Weight", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("MainWindow", "Blogging", None, -1))
        self.duplicate2_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Duplicate", None, -1))
        self.setting_groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "setting Oftions", None, -1))
        self.reset_Button.setText(QtWidgets.QApplication.translate("MainWindow", "Reset", None, -1))
        self.Outward_Constraint_lineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.Envelope_setting_label.setText(QtWidgets.QApplication.translate("MainWindow", " Envelope :", None, -1))
        self.Inward_constraint_lineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.Envelope_setting_lineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.Smoothing_Interations_lineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "25", None, -1))
        self.Smoothing_Interations_label.setText(QtWidgets.QApplication.translate("MainWindow", " Smoothing Interations :", None, -1))
        self.Outward_Constraint_label.setText(QtWidgets.QApplication.translate("MainWindow", " Outward Constraint :", None, -1))
        self.Smoothing_step_setting_label.setText(QtWidgets.QApplication.translate("MainWindow", " Smoothing Step : ", None, -1))
        self.Inward_constraint_label.setText(QtWidgets.QApplication.translate("MainWindow", " Inward Constraint :", None, -1))
        self.Smoothing_step_setting_lineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "0.35", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("MainWindow", "Duplicate", None, -1))
        self.transform_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Transform", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "Transfer", None, -1))
        self.transfer2_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Transfer", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "weight :", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtWidgets.QApplication.translate("MainWindow", "Transfer", None, -1))
        self.menuedit.setTitle(QtWidgets.QApplication.translate("MainWindow", "Edit", None, -1))
        self.menusetting.setTitle(QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))
        self.actionReset_Tool.setText(QtWidgets.QApplication.translate("MainWindow", "Reset Tool", None, -1))

