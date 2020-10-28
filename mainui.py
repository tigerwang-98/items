from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(960, 780)
        Form.setMaximumSize(QtCore.QSize(1000, 800))
        #标签时间初始化
        self.label_time = QtWidgets.QLabel(Form)
        self.label_time.setGeometry(QtCore.QRect(750, 10, 200, 41))
        self.label_time.setStyleSheet("""
                                    QLabel{color:rgb(300,300,300,120); font-size:14px; 
                                    font-weight:bold; font-family:宋体;}
                                    """)
        self.label_time.setObjectName("label_time")
        # 考勤班级标签初始化
        self.label_class = QtWidgets.QLabel(Form)
        self.label_class.setGeometry(QtCore.QRect(750, 60, 71, 16))
        self.label_class.setObjectName("label_class")
        # 考勤地点标签初始化
        self.label_location = QtWidgets.QLabel(Form)
        self.label_location.setGeometry(QtCore.QRect(750, 100, 72, 15))
        self.label_location.setObjectName("label_location")
        # 考勤班级选择框
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(820, 50, 131, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        # 考勤地点选择框
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(820, 90, 131, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        #标签显示应到初始化
        self.label_lcdName1 = QtWidgets.QLabel(Form)
        self.label_lcdName1.setGeometry(QtCore.QRect(750, 150, 41, 16))
        self.label_lcdName1.setObjectName("label_lcdName1")
        #标签显示实到初始化
        self.label_lcdName2 = QtWidgets.QLabel(Form)
        self.label_lcdName2.setGeometry(QtCore.QRect(750, 200, 41, 16))
        self.label_lcdName2.setObjectName("label_lcdName2")
        # LCD显示应到
        self.lcd_1 = QtWidgets.QLCDNumber(Form)
        self.lcd_1.setGeometry(QtCore.QRect(790, 140, 70, 40))
        self.lcd_1.setObjectName("lcd_1")
        # LCD显示实到
        self.lcd_2 = QtWidgets.QLCDNumber(Form)
        self.lcd_2.setGeometry(QtCore.QRect(790, 190, 70, 40))
        self.lcd_2.setObjectName("lcd_2")
        # 查询按钮初始化
        self.bt_check = QtWidgets.QPushButton(Form)
        self.bt_check.setGeometry(QtCore.QRect(870, 140, 81, 91))
        self.bt_check.setObjectName("bt_check")
        # 请假登记输入框
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(750, 240, 91, 31))
        self.lineEdit.setObjectName("lineEdit")
        # 漏签补签输入框
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(750, 280, 91, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        #请假登记按钮初始化
        self.bt_leave = QtWidgets.QPushButton(Form)
        self.bt_leave.setGeometry(QtCore.QRect(850, 240, 101, 31))
        self.bt_leave.setObjectName("bt_leave")
        # 漏签补签按钮
        self.bt_Supplement = QtWidgets.QPushButton(Form)
        self.bt_Supplement.setGeometry(QtCore.QRect(850, 280, 101, 31))
        self.bt_Supplement.setObjectName("bt_Supplement")
        # 未到标签初始化
        self.label_listName1 = QtWidgets.QLabel(Form)
        self.label_listName1.setGeometry(QtCore.QRect(750, 320, 41, 16))
        self.label_listName1.setObjectName("label_listName1")
        # 迟到标签初始化
        self.label_listName2 = QtWidgets.QLabel(Form)
        self.label_listName2.setGeometry(QtCore.QRect(750, 470, 41, 16))
        self.label_listName2.setObjectName("label_listName2")
        # 迟到人数（查询数据库结果）
        self.tableView_escape = QtWidgets.QTableView(Form)
        self.tableView_escape.setGeometry(QtCore.QRect(450, 490, 450, 131))
        self.tableView_escape.setObjectName("tableView_escape")
        # 缺席人数（查询数据库结果）
        self.tableView_late = QtWidgets.QTableView(Form)
        self.tableView_late.setGeometry(QtCore.QRect(450, 340, 450, 121))
        self.tableView_late.setObjectName("tableView_late")
        # 查看结果按钮初始化
        self.bt_view = QtWidgets.QPushButton(Form)
        self.bt_view.setGeometry(QtCore.QRect(750, 630, 201, 61))
        self.bt_view.setObjectName("bt_view")
        # 退出按钮初始化
        self.bt_exit = QtWidgets.QPushButton(Form)
        self.bt_exit.setGeometry(QtCore.QRect(750, 700, 201, 71))
        self.bt_exit.setObjectName("bt_exit")
        # 标题标签栏初始化
        self.label_title = QtWidgets.QLabel(Form)
        self.label_title.setGeometry(QtCore.QRect(160, 20, 500, 40))
        self.label_title.setStyleSheet("QLabel{font-size:30px; font-weight:bold; font-family:宋体;}")
        self.label_title.setText("四川轻化工大学人脸识别考勤系统")
        self.label_title.setObjectName("label_title")
        # 摄像头获取的视频帧标签初始化
        self.label_camera = QtWidgets.QLabel(Form)
        self.label_camera.setGeometry(QtCore.QRect(10, 160, 500, 400))
        self.label_camera.setText("")
        self.label_camera.setObjectName("label_camera")
        # 主页面logo标签初始化
        self.label_logo = QtWidgets.QLabel(Form)
        self.label_logo.setGeometry(QtCore.QRect(20, 70, 700, 600))
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        #应到标签
        self.label_work = QtWidgets.QLabel(Form)
        self.label_work.setGeometry(QtCore.QRect(520, 60, 71, 51))
        self.label_work.setObjectName('label_work')
        #应到
        #self.tableView_work = QtWidgets.QTableView(Form)
        #self.tableView_work.setGeometry(QtCore.QRect(520, 100, 201, 588))
        #self.tableView_work.setObjectName("tableView_work")
        #信息采集按钮初始化
        self.bt_gathering = QtWidgets.QPushButton(Form)
        self.bt_gathering.setGeometry(QtCore.QRect(10, 700, 181, 71))
        self.bt_gathering.setObjectName("bt_gathering")
        #更换人脸库按钮
        self.bt_generator = QtWidgets.QPushButton(Form)
        self.bt_generator.setGeometry(QtCore.QRect(200, 700, 111, 71))
        self.bt_generator.setObjectName("bt_generator")
        #打开摄像头按钮初始化
        self.bt_openCamera = QtWidgets.QPushButton(Form)
        self.bt_openCamera.setGeometry(QtCore.QRect(330, 700, 101, 71))
        self.bt_openCamera.setObjectName("bt_openCamera")
        #开始考勤按钮初始化
        self.bt_startCheck = QtWidgets.QPushButton(Form)
        self.bt_startCheck.setGeometry(QtCore.QRect(440, 700, 171, 71))
        self.bt_startCheck.setObjectName("bt_startCheck")
        #导出结果按钮初始化
        self.bt_getResult = QtWidgets.QPushButton(Form)
        self.bt_getResult.setGeometry(QtCore.QRect(621, 700, 101, 71))
        self.bt_getResult.setObjectName("bt_getResult")

        self.setUiText(Form)


    def setUiText(self, Form):
        self.label_lcdName1.setText('应到')
        self.label_lcdName2.setText("实到")
        self.label_listName1.setText("迟到")
        self.label_listName2.setText("缺席")
        self.bt_view.setText("查看结果")
        self.bt_leave.setText("请假登记")
        self.bt_exit.setText("退出系统")
        self.label_class.setText("考勤班级")
        self.label_location.setText("考勤地点")
        self.comboBox.setItemText(0, "16级物联网工程1班")
        self.comboBox.setItemText(1, "16级物联网工程2班")
        self.comboBox.setItemText(2, "16级物联网工程3班")
        self.comboBox.setItemText(3, "16级物联网工程4班")
        self.comboBox_2.setItemText(0, "致远楼206")
        self.comboBox_2.setItemText(1, "逸夫楼312")
        self.comboBox_2.setItemText(2, "连心楼518")
        self.comboBox_2.setItemText(3, "None")
        self.bt_check.setText("查询")
        self.bt_gathering.setText("信息采集")
        self.bt_startCheck.setText("开始考勤")
        self.bt_openCamera.setText("打开相机")
        self.bt_generator.setText("更新人脸库")
        self.bt_getResult.setText("导出结果")
        self.bt_Supplement.setText("漏签补签")
        self.label_work.setText('已到')