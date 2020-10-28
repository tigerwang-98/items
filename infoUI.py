from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(762, 565)
        # 输年级标签
        self.label_grade = QtWidgets.QLabel(Form)
        self.label_grade.setGeometry(QtCore.QRect(530, 20, 91, 16))
        self.label_grade.setObjectName("label_grade")
        # 输年级
        self.lineEdit_grade = QtWidgets.QLineEdit(Form)
        self.lineEdit_grade.setGeometry(QtCore.QRect(630, 10, 121, 31))
        self.lineEdit_grade.setObjectName("lineEdit_grade")
        #输专业标签
        self.label_major = QtWidgets.QLabel(Form)
        self.label_major.setGeometry(QtCore.QRect(530, 60, 91, 16))
        self.label_major.setObjectName("label_major")
        # 输专业
        self.lineEdit_major = QtWidgets.QLineEdit(Form)
        self.lineEdit_major.setGeometry(QtCore.QRect(630, 50, 121, 31))
        self.lineEdit_major.setObjectName("lineEdit_major")
        #输班级标签
        self.label_class = QtWidgets.QLabel(Form)
        self.label_class.setGeometry(QtCore.QRect(530, 100, 91, 16))
        self.label_class.setObjectName("label_class")
        # 班级输入框
        self.lineEdit_class = QtWidgets.QLineEdit(Form)
        self.lineEdit_class.setGeometry(QtCore.QRect(630, 90, 121, 31))
        self.lineEdit_class.setObjectName("lineEdit_class")
        #输入姓名
        self.label_name = QtWidgets.QLabel(Form)
        self.label_name.setGeometry(QtCore.QRect(530, 140, 91, 16))
        self.label_name.setObjectName("label_sex")
        #输姓名
        self.lineEdit_name = QtWidgets.QLineEdit(Form)
        self.lineEdit_name.setGeometry(QtCore.QRect(630, 130, 121, 31))
        self.lineEdit_name.setObjectName("lineEdit_name")
        #学号标签
        self.label_id = QtWidgets.QLabel(Form)
        self.label_id.setGeometry(QtCore.QRect(530, 180, 91, 16))
        self.label_id.setObjectName("label_id")
        # 学号输入框
        self.lineEdit_id = QtWidgets.QLineEdit(Form)
        self.lineEdit_id.setGeometry(QtCore.QRect(630, 170, 121, 31))
        self.lineEdit_id.setObjectName("lineEdit_id")
        # 性别标签
        self.label_sex = QtWidgets.QLabel(Form)
        self.label_sex.setGeometry(QtCore.QRect(530, 220, 91, 16))
        self.label_sex.setObjectName("label_sex")
        # 性别输入框
        self.lineEdit_sex = QtWidgets.QLineEdit(Form)
        self.lineEdit_sex.setGeometry(QtCore.QRect(630, 210, 121, 31))
        self.lineEdit_sex.setObjectName("lineEdit_sex")

        # 显示查询个人信息结果
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(530, 245, 220, 240))
        self.tableView.setObjectName("tableView")
        #界面内标题
        self.label_title = QtWidgets.QLabel(Form)
        self.label_title.setGeometry(QtCore.QRect(150, 10, 270, 15))
        self.label_title.setObjectName("label_title")
        #摄像头视频位置
        self.label_capture = QtWidgets.QLabel(Form)
        self.label_capture.setGeometry(QtCore.QRect(10, 40, 500, 440))
        self.label_capture.setText("")
        self.label_capture.setObjectName("label_capture")
        #开始采集按钮
        self.bt_collectInfo = QtWidgets.QPushButton(Form)
        self.bt_collectInfo.setGeometry(QtCore.QRect(10, 490, 250, 60))
        self.bt_collectInfo.setObjectName("bt_collectInfo")
        #拍照按钮
        self.bt_rmvinfo = QtWidgets.QPushButton(Form)
        self.bt_rmvinfo.setGeometry(QtCore.QRect(270, 490, 80, 60))
        self.bt_rmvinfo.setObjectName("bt_rmvinfo")
        #修改进本信息按钮
        self.bt_changeInfo = QtWidgets.QPushButton(Form)
        self.bt_changeInfo.setGeometry(QtCore.QRect(360, 490, 160, 60))
        self.bt_changeInfo.setObjectName("bt_changeInfo")
        #查询个人信息按钮
        self.bt_checkInfo = QtWidgets.QPushButton(Form)
        self.bt_checkInfo.setGeometry(QtCore.QRect(529, 490, 220, 60))
        self.bt_checkInfo.setObjectName("bt_checkInfo")

        self.label_name.raise_()
        self.label_class.raise_()
        self.label_id.raise_()
        self.bt_collectInfo.raise_()
        self.label_title.raise_()
        self.bt_checkInfo.raise_()
        self.label_major.raise_()
        self.label_grade.raise_()
        self.bt_changeInfo.raise_()
        self.label_capture.raise_()
        self.bt_rmvinfo.raise_()
        self.lineEdit_id.raise_()
        self.lineEdit_name.raise_()
        self.lineEdit_class.raise_()
        self.lineEdit_name.raise_()
        self.lineEdit_major.raise_()
        self.tableView.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_grade.setText(_translate("Form", "请输入年级："))
        self.label_major.setText(_translate("Form", "请输入专业:"))
        self.label_class.setText(_translate("Form", "请输入班级："))
        self.label_name.setText(_translate("Form", "请输入姓名："))
        self.label_id.setText(_translate("Form", "请输入学号:"))
        self.label_sex.setText(_translate("Form", "请输入性别："))

        self.bt_collectInfo.setText(_translate("Form", "开始采集"))
        self.bt_rmvinfo.setText(_translate("Form", "删除学生"))
        self.bt_changeInfo.setText(_translate("Form", "修改基本信息"))
        self.bt_checkInfo.setText(_translate("Form", "查询个人信息（仅输入学号）"))
        self.label_title.setText(_translate("Form", "四川轻化工大学人脸识别系统信息采集"))


