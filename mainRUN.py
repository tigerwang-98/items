# 导入必要的模块封装
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import \
    QApplication, QWidget, QInputDialog,QTableWidget,  \
    QLabel, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5.QtGui import QImage, QIcon, QPixmap
from PyQt5.QtCore import QTimer, QDateTime, QCoreApplication, Qt
import keras.models as md
#from imutils.video import VideoStream
import threading
import sys, os, time
import cv2,numpy
from PIL import Image,ImageFont,ImageDraw
from datetime import datetime
import csv
# 导入UI主界面
import mainui,infoUI
from connectDB import Database
from trainModel import Model,Dataset

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = mainui.Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle('四川轻化工大学人脸识别考勤系统')
        self.setWindowIcon(QIcon('../imgs/icon.jpg'))
        self.logopixmap = QPixmap('../imgs/icon.jpg')
        #self.camerapixmap = QPixmap('background1.png')
        self.ui.label_logo.setPixmap(self.logopixmap)
        #self.ui.label_camera.setPixmap(self.camerapixmap)

        # 在label_time上显示系统时间
        timer = QTimer(self)
        timer.timeout.connect(self.showTimeText)
        timer.start()

        # 设置摄像头按键连接函数
        self.ui.bt_openCamera.clicked.connect(self.openCamera)
        #设置更新人脸数据按键连接函数
        self.ui.bt_generator.clicked.connect(self.trainModel)
        # 设置开始考勤按键的回调函数
        self.ui.bt_startCheck.clicked.connect(self.startCheck)
        #设置查询班级人数按键的连接函数
        self.ui.bt_check.clicked.connect(self.lcdDisplay)
        #设置请假按钮的函数
        self.ui.bt_leave.clicked.connect(self.leaveButton)
        #设置欧签补签的函数
        self.ui.bt_Supplement.clicked.connect(self.supplementButton)
        #设置对输入内容的删除提示
        self.ui.lineEdit.setClearButtonEnabled(True)
        self.ui.lineEdit_2.setClearButtonEnabled(True)
        #设置查看结果（显示迟到和缺席）按钮的函数
        self.ui.bt_view.clicked.connect(self.showLateAbsence)
        #设置导出结果按钮的函数
        self.ui.bt_getResult.clicked.connect(self.outPutToCsv)
        # 设置“退出系统”按键事件, 按下之后退出主界面
        self.ui.bt_exit.clicked.connect(self.quit)

        self.db = Database()
        self.dataset = Dataset()
        self.model = Model(self.dataset)
        # 设置区分打开摄像头还是人脸识别的标识符,0打开摄像头或者开始考勤
        self.switch_bt = 0
        # 初始化摄像头
        self.cap = cv2.VideoCapture()
        self.standard_time = {}

    def quit(self):
        if self.cap.isOpened():
            self.openCamera()
        sys.exit(0)

    def showTimeText(self):
        datetime = QDateTime.currentDateTime().toString()
        temptime = datetime.split(' ')
        #datetime:[星期，月份，日期，时间，年份]
        datetime = temptime[-1] + "年" + temptime[1] + temptime[2] + "日" + temptime[0] + temptime[-2]
        self.ui.label_time.setText(datetime)

    def openCamera(self):
        # 判断摄像头是否打开，如果打开则为true，反之为false
        flag = self.cap.isOpened()
        if flag == False:
            self.ui.label_logo.clear()
            self.cap.open(0)
            self.ui.bt_openCamera.setText('关闭相机')
            self.showCamera()
        else:
            self.cap.release()
            self.ui.label_logo.setPixmap(self.logopixmap)
            self.ui.label_camera.clear()
            self.ui.bt_openCamera.setText('打开相机')

    # 进入考勤模式，通过switch_bt进行控制的函数
    def startCheck(self):
        if self.cap.isOpened():
            if self.switch_bt == 0:
                self.switch_bt = 1
                self.ui.bt_startCheck.setText('退出考勤')
                items = ['上午第一节', '上午第三节', '下午第一节', '下午第三节']
                value, ok = QInputDialog.getItem(self, "提示", "请选择打卡时间", items, 1, False)
                self.standard_time = self.valueToTime(value)
                self.showCamera()
            elif self.switch_bt == 1:
                self.switch_bt = 0
                self.ui.bt_startCheck.setText('开始考勤')
                self.showCamera()
        else:
            QMessageBox.warning(self, '提示', '请先打开摄像头', QMessageBox.Ok)

    def valueToTime(self, value):
        date = datetime.now().strftime('%Y-%m-%d')
        d = {
            '上午第一节': "%s 08:50:00"%date,
            '上午第三节': '%s 10:30:00'%date,
            '下午第一节': '%s 14:30:00'%date,
            '下午第三节': '%s 23:45:00'%date
        }
        return d[value]

    def trainModel(self):
        model_path = "../models/face_model.h5"
        self.dataset.load()
        self.model.build_model()
        self.model.train()
        self.model.save_model(model_path)
        self.model.evaluate(self.dataset)
        QMessageBox.information(self, "提示", "更新成功", QMessageBox.Ok)

    def showCamera(self):
        # 如果按键按下
        if self.switch_bt == 0:
            self.ui.label_logo.clear()
            self.ui.bt_openCamera.setText('关闭相机')
            while (self.cap.isOpened()):
                # 以BGR格式读取图像
                ret, image = self.cap.read()
                QApplication.processEvents()  # 防止UI界面卡顿
                # 将图像转换为RGB格式
                show = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 这里指的是显示原图
                # opencv 读取图片的样式，不能通过Qlabel进行显示，需要转换为Qimage QImage(uchar * data, int width,
                showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
                self.ui.label_camera.setScaledContents(True)
                self.ui.label_camera.setPixmap(QPixmap.fromImage(showImage))
            # 因为最后会存留一张图像在lable上，需要对lable进行清理
            self.ui.label_camera.clear()
            self.ui.bt_openCamera.setText('打开相机')

        elif self.switch_bt == 1:
            self.ui.label_logo.clear()
            self.ui.bt_startCheck.setText('退出考勤')
            self.setAllAbsencs()

            classifier_path = "A:\\graduate design\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
            model_path = "../models/face_model.h5"
            if not os.path.exists(model_path):
                QMessageBox.information(self, "提示", "请先更新人脸库", QMessageBox.Ok)
            else:
                self.model.load_model(model_path)
                while (self.cap.isOpened()):
                    ret, image = self.cap.read()
                    QApplication.processEvents()  # 防止UI界面卡顿
                    if ret is True:
                        grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    else:
                        continue
                    classfier = cv2.CascadeClassifier(classifier_path)
                    faces = classfier.detectMultiScale(grey_image, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
                    if len(faces) > 0:
                        face = faces[0]
                        x, y, w, h = face
                        img = image[y-10: y+h+10, x-10: x+w+10]
                        result = self.model.face_predict(img)
                        if result != None:
                            name = self.dataset.d[result].split('-')
                            cv2.rectangle(image, (x - 10, y - 10), (x + w + 10, y + h + 10), (0, 255, 0), 2)
                            image = self.cv2ImgAddText(image, name[-1], x+30, y+30)
                            show = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 这里指的是显示原图
                            showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
                            self.ui.label_camera.setPixmap(QPixmap.fromImage(showImage))
                            if self.recordName(name[0], self.standard_time) == "正常":
                                self.refresh(name[0])
                        else:
                            cv2.putText(image, 'unknown', (x+30, y+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
                            show = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 这里指的是显示原图
                            showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
                            self.ui.label_camera.setPixmap(QPixmap.fromImage(showImage))
                    else:
                        show = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 这里指的是显示原图
                        # opencv 读取图片的样式，不能通过Qlabel进行显示，需要转换为Qimage QImage(uchar * data, int width,
                        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
                        self.ui.label_camera.setPixmap(QPixmap.fromImage(showImage))
                self.ui.label_camera.clear()

    def cv2ImgAddText(self, img, text, left, top, textColor=(0, 255, 0), textSize=20):
        if (isinstance(img, numpy.ndarray)):  # 判断是否OpenCV图片类型
            img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        # 创建一个可以在给定图像上绘图的对象
        draw = ImageDraw.Draw(img)
        # 字体的格式
        fontStyle = ImageFont.truetype("font/simsun.ttc", textSize, encoding="utf-8")
        # 绘制文本
        draw.text((left, top), text, textColor, font=fontStyle)
        # 转换回OpenCV格式
        return cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)

    def lcdDisplay(self):
        tempinfo = []
        input_class = self.ui.comboBox.currentText()
        tempinfo.append(input_class[:2])
        tempinfo.append(input_class[3:-2])
        tempinfo.append(input_class[-2])
        result = self.db.selectClass(tempinfo)
        self.ui.lcd_1.display(result[0])
        self.ui.lcd_2.display(result[1])

    def recordName(self, ID, st):
        description = self.db.record(ID, st)
        self.lcdDisplay()
        return description

    def leaveButton(self):
        self.leaveStudents(1)
    def supplementButton(self):
        self.leaveStudents(2)
    def leaveStudents(self, button):
        description = ""
        info = []
        id = ""
        if self.ui.lineEdit.isModified() or self.ui.lineEdit_2.isModified():
            currentTime = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            if button == 1:
                description = "请假"
                id = self.ui.lineEdit.text()
            elif button == 2:
                description = "补签"
                id = self.ui.lineEdit_2.text()
            checkInfo = self.db.useIdGetInfo(id)
            if len(checkInfo) > 0:
                info.append(checkInfo[0][3])
                info.append(checkInfo[0][0])
                info.append(checkInfo[0][1])
                info.append(checkInfo[0][2])
                info.append(currentTime)
                info.append(description)
                info.append(checkInfo[0][4])
                if self.db.qingjia(info) == 1:
                    QMessageBox.information(self, "提示", "签到成功!请勿重复操作", QMessageBox.Ok)
                else:
                    QMessageBox.information(self, "提示", "签到失败！请重试", QMessageBox.Ok)
            else:
                QMessageBox.information(self, "提示", "没有此人！请检查学号", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "warning", "学号不能为空，请输入后重试！", QMessageBox.Ok)
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()

    def showLateAbsence(self):
        clas = self.ui.comboBox.currentText()
        latestu, absenstu = self.db.selectLate(clas)
        model1 = QtGui.QStandardItemModel(len(latestu), 0)
        model1.setHorizontalHeaderLabels(['学号', '姓名'])
        for row in range(len(latestu)):
            id_item = QtGui.QStandardItem(latestu[row][0])
            name_item =QtGui.QStandardItem(latestu[row][1])
            model1.setItem(row, 0, id_item)
            model1.setItem(row, 1, name_item)
        self.ui.tableView_late.setModel(model1)

        model2 = QtGui.QStandardItemModel(len(absenstu), 0)
        model2.setHorizontalHeaderLabels(['学号', '姓名'])
        for row in range(len(absenstu)):
            id_item = QtGui.QStandardItem(absenstu[row][0])
            name_item = QtGui.QStandardItem(absenstu[row][1])
            model2.setItem(row, 0, id_item)
            model2.setItem(row, 1, name_item)
        self.ui.tableView_escape.setModel(model2)

    def setAllAbsencs(self):
        self.db.setAbsense()

    def outPutToCsv(self):
        clas = self.ui.comboBox.currentText()
        place = self.ui.comboBox_2.currentText()
        time = self.standard_time
        title = ['迟到']
        label = ['学号', '姓名']
        latestu, absensestu = self.db.selectLate(clas)
        count = 1
        csv_path = '../models/'

        for dir in os.listdir(csv_path):
            if dir.endswith('.csv'):
                count += 1
        if not len(time) > 0:
            QMessageBox.information(self, '提示', '请完成所有操作后导出', QMessageBox.Ok)
        else:
            csv_path = csv_path + 'result' + '-' + str(count) + '.csv'
            f = open(csv_path, 'a', newline='')
            writer = csv.writer(f, dialect='excel')
            writer.writerow(['考勤地点', place])
            writer.writerow(['考勤时间', time])
            writer.writerow(title)
            writer.writerow(label)
            for i in latestu:
                writer.writerow(i)
            title = ['缺席']
            writer.writerow(title)
            writer.writerow(label)
            for i in absensestu:
                writer.writerow(i)
            QMessageBox.information(self, "提示", "导出成功！", QMessageBox.Ok)

    def refresh(self, ID):
        result = self.db.refresh(ID)
        model1 = QtGui.QStandardItemModel(len(result), 0)
        model1.setHorizontalHeaderLabels(['学号', '姓名'])
        for row in range(len(result)):
            id_item = QtGui.QStandardItem(result[row][0])
            name_item = QtGui.QStandardItem(result[row][1])
            model1.setItem(row, 0, id_item)
            model1.setItem(row, 1, name_item)
        self.ui.tableView_work.setModel(model1)

class infoDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.Dialog = infoUI.Ui_Form()
        self.Dialog.setupUi(self)

        self.setWindowTitle('学生信息采集')
        self.setWindowIcon(QIcon('../imgs/icon.jpg'))
        self.pixmap = QPixmap('../imgs/background.png')
        self.Dialog.label_capture.setPixmap(self.pixmap)

        # 设置信息采集按键连接函数
        self.Dialog.bt_collectInfo.clicked.connect(self.openCam)
        # 设置删除连接函数
        self.Dialog.bt_rmvinfo.clicked.connect(self.rmvInfo)
        # 设置修改信息按键连接函数
        self.Dialog.bt_changeInfo.clicked.connect(self.changeInfo)
        # 设置查询信息按键连接函数
        self.Dialog.bt_checkInfo.clicked.connect(self.checkInfo)

        self.db = Database()
        self.users = []
        self.cap = cv2.VideoCapture()
        self.photos = 0

    def handle_click(self):
        if not self.isVisible():
            self.show()
    def handle_close(self):
        self.close()

    def openCam(self):
        flag = self.cap.isOpened()
        if not flag:
            self.users.clear()
            if self.getUserInfo():
                ID = self.users[-1]
                name = self.users[-3]
                num = 1
                classfier_path = "A:\\graduate design\\venv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml"
                filepath = "../dataset/" + ID + "-" + name
                classfier = cv2.CascadeClassifier(classfier_path)
                if not os.path.exists(filepath):
                    os.makedirs(filepath)
                if not self.insertInfo():
                    QMessageBox.warning(self, "提示", "已有此人！请重试", QMessageBox.Ok)
                else:
                    self.cap.open(0)
                    self.Dialog.label_capture.clear()
                    self.Dialog.bt_collectInfo.setText('退出采集')
                    self.showCapture(classfier, num, filepath)
            else:
                QMessageBox.warning(self, "warning", "请完整输入信息！", QMessageBox.Ok)
                self.clearEditInfo()
        else:
            self.cap.release()
            #self.Dialog.label_capture.clear()
            self.Dialog.label_capture.setPixmap(self.pixmap)
            self.Dialog.bt_collectInfo.setText('开始采集')

    # 获得采集信息，ID在最后
    def getUserInfo(self):
        grade = self.Dialog.lineEdit_grade.text()
        self.users.append(grade)
        major = self.Dialog.lineEdit_major.text()
        self.users.append(major)
        Class = self.Dialog.lineEdit_class.text()
        self.users.append(Class)
        name = self.Dialog.lineEdit_name.text()
        self.users.append(name)
        ID = self.Dialog.lineEdit_id.text()
        sex = self.Dialog.lineEdit_sex.text()
        self.users.append(sex)
        self.users.append(ID)
        for item in self.users:
            if item == '':
                self.users.clear()
                return False
        if len(self.users) < 6:
            self.users.clear()
            return False
        return True

    def showCapture(self,classfier, photonum, filepath):
        num = photonum
        while (self.cap.isOpened()):
            ret, image = self.cap.read()
            QApplication.processEvents()  # 防止UI界面卡顿
            if ret is True:
                grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            else:
                continue
            faces = classfier.detectMultiScale(grey_image, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
            if len(faces) > 0:
                face = faces[0]
                x, y, w, h = face
                img_name = '%s/%d.jpg' % (filepath, num)
                img = image[y - 10: y + h + 10, x - 10: x + w + 10]
                if not img.all():
                    cv2.imencode('.jpg', img)[1].tofile(img_name)  # cv2保存路径中有中文
                    num += 1
                if num > 20:
                    break
                cv2.rectangle(image, (x-10, y-10), (x+w+10, y+h+10), (0, 0, 255), 1)
                # 将图像转换为RGB格式
                show = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 这里指的是显示原图
                # opencv 读取图片的样式，不能通过Qlabel进行显示，需要转换为Qimage
                showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
                self.Dialog.label_capture.setPixmap(QPixmap.fromImage(showImage))
            else:
                img = QImage(image, image.shape[1], image.shape[0], QImage.Format_RGB888)
                self.Dialog.label_capture.setPixmap(QPixmap.fromImage(img))

        if os.path.getsize(filepath) > 0:
            QMessageBox.information(self, "提示", "注册成功！", QMessageBox.Ok)
        # 因为最后会存留一张图像在lable上，需要对lable进行清理
        self.Dialog.label_capture.clear()
        self.Dialog.label_capture.setPixmap(self.pixmap)
        self.Dialog.bt_collectInfo.setText('开始采集')
        self.cap.release()

    def clearEditInfo(self):
        self.Dialog.lineEdit_grade.clear()
        self.Dialog.lineEdit_major.clear()
        self.Dialog.lineEdit_class.clear()
        self.Dialog.lineEdit_name.clear()
        self.Dialog.lineEdit_id.clear()
        self.Dialog.lineEdit_sex.clear()
        self.Dialog.label_capture.setPixmap(self.pixmap)
        self.Dialog.bt_collectInfo.setText('信息采集')

    def rmvInfo(self):
        self.users.clear()
        if self.getUserInfo():
            statuscode = self.db.rmvInfo(self.users[-1])
            print("statuscode:",statuscode)

            if statuscode:
                QMessageBox.information(self, "提示", "删除成功", QMessageBox.Ok)
            else:
                QMessageBox.information(self, "提示", "失败!查无此人!", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "warning", "请输入完整信息", QMessageBox.Ok)

        self.clearEditInfo()

    # 信息采集页面查询
    def checkInfo(self):
        input_ID = self.Dialog.lineEdit_id.text()
        if input_ID != '':
            result = self.db.checkInfo(input_ID)
            if len(result) == 0:
                QMessageBox.warning(self, "warning", "人脸数据库中无此人信息，请马上录入！", QMessageBox.Ok)
            else:
                result = list(result[0])
                # 设置显示数据层次结构，5行2列(包含行表头)
                self.model = QtGui.QStandardItemModel(len(result), 0)
                    # 设置数据行标题
                self.model.setHorizontalHeaderLabels(['值'])
                self.model.setVerticalHeaderLabels(['年级', '专业', '班级', '姓名', '学号', '性别'])

                # 设置填入数据内容
                for row in range(len(result)):
                    item = QtGui.QStandardItem(result[row])
                    # 设置每个位置的文本值
                    self.model.setItem(row, 0, item)
                # 指定显示的tableView控件，实例化表格视图
                self.View = self.Dialog.tableView
                self.View.setModel(self.model)
            self.clearEditInfo()
        else:
            QMessageBox.warning(self, "warning", "请输入学号", QMessageBox.Ok)

    def insertInfo(self):
        return self.db.insertInfo(self.users)

    def changeInfo(self):
        self.users.clear()
        if self.getUserInfo():
            #print(self.users)
            status = self.db.changeInfo(self.users)
            if status == 1:
                QMessageBox.warning(self, "warning", "录入成功，请勿重复操作！", QMessageBox.Ok)
            elif status == 0:
                QMessageBox.warning(self, "warning", "录入失败，请检查学号是否正确！", QMessageBox.Ok)
            elif status == -1:
                QMessageBox.warning(self, "warning", "录入失败，学号不能为空！", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "warning", "请完整输入信息！", QMessageBox.Ok)
        self.clearEditInfo()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建并显示窗口
    mainWindow = MainWindow()
    infoWindow = infoDialog()
    mainWindow.ui.bt_gathering.clicked.connect(infoWindow.handle_click)
    mainWindow.show()

    sys.exit(app.exec_())




