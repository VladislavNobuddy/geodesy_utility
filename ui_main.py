# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(472, 183)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(472, 183))
        MainWindow.setMaximumSize(QSize(472, 183))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 473, 184))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.First_x = QLineEdit(self.layoutWidget)
        self.First_x.setObjectName(u"First_x")

        self.horizontalLayout_2.addWidget(self.First_x)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.First_y = QLineEdit(self.layoutWidget)
        self.First_y.setObjectName(u"First_y")

        self.horizontalLayout_2.addWidget(self.First_y)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)

        self.Clear_first = QPushButton(self.layoutWidget)
        self.Clear_first.setObjectName(u"Clear_first")

        self.horizontalLayout_6.addWidget(self.Clear_first)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)


        self.gridLayout.addLayout(self.horizontalLayout_8, 0, 0, 1, 2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.Second_x = QLineEdit(self.layoutWidget)
        self.Second_x.setObjectName(u"Second_x")

        self.horizontalLayout_3.addWidget(self.Second_x)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.Second_y = QLineEdit(self.layoutWidget)
        self.Second_y.setObjectName(u"Second_y")

        self.horizontalLayout_3.addWidget(self.Second_y)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.Clear_second = QPushButton(self.layoutWidget)
        self.Clear_second.setObjectName(u"Clear_second")

        self.horizontalLayout_5.addWidget(self.Clear_second)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_5)


        self.gridLayout.addLayout(self.horizontalLayout_9, 1, 0, 1, 2)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout.addWidget(self.label_9)

        self.length_first = QLineEdit(self.layoutWidget)
        self.length_first.setObjectName(u"length_first")

        self.horizontalLayout.addWidget(self.length_first)


        self.horizontalLayout_12.addLayout(self.horizontalLayout)

        self.Clear_first_length = QPushButton(self.layoutWidget)
        self.Clear_first_length.setObjectName(u"Clear_first_length")

        self.horizontalLayout_12.addWidget(self.Clear_first_length)


        self.gridLayout.addLayout(self.horizontalLayout_12, 2, 0, 1, 2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.lenght_second = QLineEdit(self.layoutWidget)
        self.lenght_second.setObjectName(u"lenght_second")

        self.horizontalLayout_10.addWidget(self.lenght_second)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)

        self.Clear_second_length = QPushButton(self.layoutWidget)
        self.Clear_second_length.setObjectName(u"Clear_second_length")

        self.horizontalLayout_11.addWidget(self.Clear_second_length)


        self.gridLayout.addLayout(self.horizontalLayout_11, 3, 0, 1, 2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.angle = QDoubleSpinBox(self.layoutWidget)
        self.angle.setObjectName(u"angle")

        self.horizontalLayout_4.addWidget(self.angle)


        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)

        self.Count = QPushButton(self.layoutWidget)
        self.Count.setObjectName(u"Count")

        self.gridLayout.addWidget(self.Count, 4, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.Result_x = QLabel(self.layoutWidget)
        self.Result_x.setObjectName(u"Result_x")

        self.horizontalLayout_7.addWidget(self.Result_x)

        self.Result_y = QLabel(self.layoutWidget)
        self.Result_y.setObjectName(u"Result_y")

        self.horizontalLayout_7.addWidget(self.Result_y)


        self.gridLayout.addLayout(self.horizontalLayout_7, 5, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0432\u0430\u044f \u0442\u043e\u0447\u043a\u0430", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.Clear_first.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0442\u043e\u0440\u0430\u044f \u0442\u043e\u0447\u043a\u0430", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.Clear_second.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430 \u043e\u0442 \u043f\u0435\u0440\u0432\u043e\u0439 \u0442\u043e\u0447\u043a\u0438 \u0434\u043e \u0432\u044b\u043d\u043e\u0441\u043d\u043e\u0439", None))
        self.Clear_first_length.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430 \u043e\u0442 \u0432\u0442\u043e\u0440\u043e\u0439 \u0442\u043e\u0447\u043a\u0438 \u0434\u043e \u0432\u044b\u043d\u043e\u0441\u043d\u043e\u0439", None))
        self.Clear_second_length.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043e\u043b", None))
        self.Count.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043d\u043e\u0441 \u0442\u043e\u0447\u043a\u0438", None))
        self.Result_x.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 1", None))
        self.Result_y.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 2", None))
    # retranslateUi

