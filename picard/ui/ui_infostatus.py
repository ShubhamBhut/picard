# Form implementation generated from reading ui file 'ui/infostatus.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# Automatically generated - do not edit.
# Use `python setup.py build_ui` to update it.

from PyQt6 import (
    QtCore,
    QtGui,
    QtWidgets,
)

from picard.i18n import gettext as _


class Ui_InfoStatus(object):
    def setupUi(self, InfoStatus):
        InfoStatus.setObjectName("InfoStatus")
        InfoStatus.resize(683, 145)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(InfoStatus.sizePolicy().hasHeightForWidth())
        InfoStatus.setSizePolicy(sizePolicy)
        InfoStatus.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalLayout = QtWidgets.QHBoxLayout(InfoStatus)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.val1 = QtWidgets.QLabel(parent=InfoStatus)
        self.val1.setMinimumSize(QtCore.QSize(40, 0))
        self.val1.setText("")
        self.val1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.val1.setObjectName("val1")
        self.horizontalLayout.addWidget(self.val1)
        self.label1 = QtWidgets.QLabel(parent=InfoStatus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label1.sizePolicy().hasHeightForWidth())
        self.label1.setSizePolicy(sizePolicy)
        self.label1.setMinimumSize(QtCore.QSize(0, 0))
        self.label1.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label1.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label1.setScaledContents(False)
        self.label1.setObjectName("label1")
        self.horizontalLayout.addWidget(self.label1)
        self.val2 = QtWidgets.QLabel(parent=InfoStatus)
        self.val2.setMinimumSize(QtCore.QSize(40, 0))
        self.val2.setText("")
        self.val2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.val2.setObjectName("val2")
        self.horizontalLayout.addWidget(self.val2)
        self.label2 = QtWidgets.QLabel(parent=InfoStatus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label2.sizePolicy().hasHeightForWidth())
        self.label2.setSizePolicy(sizePolicy)
        self.label2.setText("")
        self.label2.setObjectName("label2")
        self.horizontalLayout.addWidget(self.label2)
        self.val3 = QtWidgets.QLabel(parent=InfoStatus)
        self.val3.setMinimumSize(QtCore.QSize(40, 0))
        self.val3.setText("")
        self.val3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.val3.setObjectName("val3")
        self.horizontalLayout.addWidget(self.val3)
        self.label3 = QtWidgets.QLabel(parent=InfoStatus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label3.sizePolicy().hasHeightForWidth())
        self.label3.setSizePolicy(sizePolicy)
        self.label3.setText("")
        self.label3.setObjectName("label3")
        self.horizontalLayout.addWidget(self.label3)
        self.val4 = QtWidgets.QLabel(parent=InfoStatus)
        self.val4.setMinimumSize(QtCore.QSize(40, 0))
        self.val4.setText("")
        self.val4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.val4.setObjectName("val4")
        self.horizontalLayout.addWidget(self.val4)
        self.label4 = QtWidgets.QLabel(parent=InfoStatus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label4.sizePolicy().hasHeightForWidth())
        self.label4.setSizePolicy(sizePolicy)
        self.label4.setText("")
        self.label4.setScaledContents(False)
        self.label4.setObjectName("label4")
        self.horizontalLayout.addWidget(self.label4)
        self.val5 = QtWidgets.QLabel(parent=InfoStatus)
        self.val5.setMinimumSize(QtCore.QSize(40, 0))
        self.val5.setText("")
        self.val5.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.val5.setObjectName("val5")
        self.horizontalLayout.addWidget(self.val5)
        self.label5 = QtWidgets.QLabel(parent=InfoStatus)
        self.label5.setMinimumSize(QtCore.QSize(0, 0))
        self.label5.setText("")
        self.label5.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label5.setObjectName("label5")
        self.horizontalLayout.addWidget(self.label5)

        self.retranslateUi(InfoStatus)
        QtCore.QMetaObject.connectSlotsByName(InfoStatus)

    def retranslateUi(self, InfoStatus):
        InfoStatus.setWindowTitle(_("Form"))
