# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGraphicsView, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget, QTabWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 700)
        self.actionAbrirPdf = QAction(MainWindow)
        self.actionAbrirPdf.setObjectName(u"actionAbrirPdf")
        self.actionGuardarFirmado = QAction(MainWindow)
        self.actionGuardarFirmado.setObjectName(u"actionGuardarFirmado")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionAcercaDe = QAction(MainWindow)
        self.actionAcercaDe.setObjectName(u"actionAcercaDe")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        # --- Bloque PDF ---
        self.widget_pdf = QWidget(self.centralwidget)
        self.widget_pdf.setObjectName(u"widget_pdf")
        self.horizontalLayout = QHBoxLayout(self.widget_pdf)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_pdf = QLabel(self.widget_pdf)
        self.label_pdf.setObjectName(u"label_pdf")
        self.horizontalLayout.addWidget(self.label_pdf)

        self.leRutaPdf = QLineEdit(self.widget_pdf)
        self.leRutaPdf.setObjectName(u"leRutaPdf")
        self.leRutaPdf.setReadOnly(True)
        self.horizontalLayout.addWidget(self.leRutaPdf)

        self.btnExaminar = QPushButton(self.widget_pdf)
        self.btnExaminar.setObjectName(u"btnExaminar")
        self.horizontalLayout.addWidget(self.btnExaminar)
        self.verticalLayout.addWidget(self.widget_pdf)

        # --- Bloque Hash ---
        self.lblHash = QLabel(self.centralwidget)
        self.lblHash.setObjectName(u"lblHash")
        self.lblHash.setText(u"SHA256: -")
        self.lblHash.setStyleSheet(u"color: gray; font-size: 10px;")
        self.verticalLayout.addWidget(self.lblHash)

        # --- Bloque Preview ---
        self.gvPreview = QGraphicsView(self.centralwidget)
        self.gvPreview.setObjectName(u"gvPreview")
        self.verticalLayout.addWidget(self.gvPreview)

        # --- Bloque Firma (Tabs) ---
        self.groupFirma = QGroupBox(self.centralwidget)
        self.groupFirma.setObjectName(u"groupFirma")
        self.verticalLayoutFirma = QVBoxLayout(self.groupFirma)
        
        self.tabWidget = QTabWidget(self.groupFirma)
        self.tabWidget.setObjectName(u"tabWidget")

        # Tab 1: Texto
        self.tabTexto = QWidget()
        self.tabTexto.setObjectName(u"tabTexto")
        self.formLayout = QFormLayout(self.tabTexto)
        self.label_firmante = QLabel(self.tabTexto)
        self.label_firmante.setObjectName(u"label_firmante")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_firmante)
        self.leFirmante = QLineEdit(self.tabTexto)
        self.leFirmante.setObjectName(u"leFirmante")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.leFirmante)
        self.label_motivo = QLabel(self.tabTexto)
        self.label_motivo.setObjectName(u"label_motivo")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_motivo)
        self.leMotivo = QLineEdit(self.tabTexto)
        self.leMotivo.setObjectName(u"leMotivo")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.leMotivo)
        self.tabWidget.addTab(self.tabTexto, "")

        # Tab 2: Imagen
        self.tabImagen = QWidget()
        self.tabImagen.setObjectName(u"tabImagen")
        self.verticalLayoutImagen = QVBoxLayout(self.tabImagen)
        
        self.btnSeleccionarImagen = QPushButton(self.tabImagen)
        self.btnSeleccionarImagen.setObjectName(u"btnSeleccionarImagen")
        self.verticalLayoutImagen.addWidget(self.btnSeleccionarImagen)
        
        self.lblPreviewImagen = QLabel(self.tabImagen)
        self.lblPreviewImagen.setObjectName(u"lblPreviewImagen")
        self.lblPreviewImagen.setAlignment(Qt.AlignCenter)
        self.lblPreviewImagen.setText(u"Sin imagen seleccionada")
        self.lblPreviewImagen.setStyleSheet(u"border: 1px dashed gray; min-height: 100px;")
        self.verticalLayoutImagen.addWidget(self.lblPreviewImagen)
        
        self.tabWidget.addTab(self.tabImagen, "")

        self.verticalLayoutFirma.addWidget(self.tabWidget)

        # Botón Firmar (común)
        self.btnFirmar = QPushButton(self.groupFirma)
        self.btnFirmar.setObjectName(u"btnFirmar")
        self.verticalLayoutFirma.addWidget(self.btnFirmar)

        self.verticalLayout.addWidget(self.groupFirma)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuArchivo.addAction(self.actionAbrirPdf)
        self.menuArchivo.addAction(self.actionGuardarFirmado)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menuAyuda.addAction(self.actionAcercaDe)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Firma Digital - DocuSecure Pro", None))
        self.actionAbrirPdf.setText(QCoreApplication.translate("MainWindow", u"Abrir PDF", None))
        self.actionGuardarFirmado.setText(QCoreApplication.translate("MainWindow", u"Guardar PDF firmado", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.actionAcercaDe.setText(QCoreApplication.translate("MainWindow", u"Acerca de...", None))
        self.label_pdf.setText(QCoreApplication.translate("MainWindow", u"Archivo PDF:", None))
        self.btnExaminar.setText(QCoreApplication.translate("MainWindow", u"Examinar...", None))
        self.groupFirma.setTitle(QCoreApplication.translate("MainWindow", u"Datos de firma", None))
        self.label_firmante.setText(QCoreApplication.translate("MainWindow", u"Nombre del firmante:", None))
        self.label_motivo.setText(QCoreApplication.translate("MainWindow", u"Motivo de la firma:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTexto), QCoreApplication.translate("MainWindow", u"Firma Texto", None))
        self.btnSeleccionarImagen.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Imagen de Firma...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabImagen), QCoreApplication.translate("MainWindow", u"Firma Imagen", None))
        self.btnFirmar.setText(QCoreApplication.translate("MainWindow", u"Aplicar firma al PDF", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
    # retranslateUi
