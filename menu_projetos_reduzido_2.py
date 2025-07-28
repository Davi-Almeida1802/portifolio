# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teste_projetos.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)
import sprites

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 920)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1280, 720))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.a_barra_lateral = QFrame(self.centralwidget)
        self.a_barra_lateral.setObjectName(u"a_barra_lateral")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(100)
        sizePolicy1.setHeightForWidth(self.a_barra_lateral.sizePolicy().hasHeightForWidth())
        self.a_barra_lateral.setSizePolicy(sizePolicy1)
        self.a_barra_lateral.setMinimumSize(QSize(130, 600))
        self.a_barra_lateral.setMaximumSize(QSize(150, 16777215))
        self.a_barra_lateral.setStyleSheet(u"background-color: #303030;")
        self.a_barra_lateral.setFrameShape(QFrame.NoFrame)
        self.a_barra_lateral.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.a_barra_lateral)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, -1, -1)
        self.a_top_aside = QFrame(self.a_barra_lateral)
        self.a_top_aside.setObjectName(u"a_top_aside")
        self.a_top_aside.setMinimumSize(QSize(120, 200))
        self.a_top_aside.setMaximumSize(QSize(120, 200))
        self.a_top_aside.setFrameShape(QFrame.NoFrame)
        self.a_top_aside.setFrameShadow(QFrame.Raised)
        self.a_perfil = QFrame(self.a_top_aside)
        self.a_perfil.setObjectName(u"a_perfil")
        self.a_perfil.setGeometry(QRect(1, 5, 130, 75))
        self.a_perfil.setMinimumSize(QSize(130, 75))
        self.a_perfil.setMaximumSize(QSize(40, 60))
        self.a_perfil.setStyleSheet(u"border-radius: 5px;")
        self.a_perfil.setFrameShape(QFrame.NoFrame)
        self.a_perfil.setFrameShadow(QFrame.Raised)
        self.a_icone_perfil = QPushButton(self.a_perfil)
        self.a_icone_perfil.setObjectName(u"a_icone_perfil")
        self.a_icone_perfil.setGeometry(QRect(40, 0, 50, 50))
        self.a_icone_perfil.setMinimumSize(QSize(45, 45))
        self.a_icone_perfil.setMaximumSize(QSize(50, 50))
        self.a_icone_perfil.setStyleSheet(u"background-image: url(:/icones/autor.jpg);\n"
"background-repeat: no-repeat;\n"
"border-radius: 25px;\n"
"border: 1px solid black;")
        self.b_nome_usuario = QLabel(self.a_perfil)
        self.b_nome_usuario.setObjectName(u"b_nome_usuario")
        self.b_nome_usuario.setGeometry(QRect(0, 55, 130, 15))
        self.b_nome_usuario.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: white;")
        self.b_nome_usuario.setAlignment(Qt.AlignCenter)
        self.b_botoes_top_aside = QFrame(self.a_top_aside)
        self.b_botoes_top_aside.setObjectName(u"b_botoes_top_aside")
        self.b_botoes_top_aside.setGeometry(QRect(1, 80, 130, 114))
        self.b_botoes_top_aside.setMinimumSize(QSize(130, 0))
        self.b_botoes_top_aside.setMaximumSize(QSize(130, 16777215))
        self.b_botoes_top_aside.setStyleSheet(u"background-color: transparent;\n"
"border: none;\n"
"color: white;")
        self.b_botoes_top_aside.setFrameShape(QFrame.NoFrame)
        self.b_botoes_top_aside.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.b_botoes_top_aside)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 0, 0, -1)
        self.a_linha_horizontal = QFrame(self.b_botoes_top_aside)
        self.a_linha_horizontal.setObjectName(u"a_linha_horizontal")
        self.a_linha_horizontal.setMaximumSize(QSize(105, 1))
        self.a_linha_horizontal.setStyleSheet(u"background-color: #cecece;\n"
"margin-left: 5px;")
        self.a_linha_horizontal.setFrameShape(QFrame.Shape.HLine)
        self.a_linha_horizontal.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.a_linha_horizontal)

        self.b_inicio = QPushButton(self.b_botoes_top_aside)
        self.b_inicio.setObjectName(u"b_inicio")
        self.b_inicio.setMinimumSize(QSize(120, 30))
        self.b_inicio.setMaximumSize(QSize(120, 30))
        self.b_inicio.setCursor(QCursor(Qt.PointingHandCursor))
        self.b_inicio.setLayoutDirection(Qt.LeftToRight)
        self.b_inicio.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/icones/home.svg);\n"
"	background-repeat: no-repeat;\n"
"	background-position: left left;\n"
"	qproperty-alignment: AlignRight;\n"
"	margin-right: 16px;\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(0, 153, 255);\n"
"	\n"
"	font: 11pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.b_inicio)

        self.d_projetos = QPushButton(self.b_botoes_top_aside)
        self.d_projetos.setObjectName(u"d_projetos")
        self.d_projetos.setMinimumSize(QSize(120, 30))
        self.d_projetos.setMaximumSize(QSize(120, 30))
        self.d_projetos.setCursor(QCursor(Qt.PointingHandCursor))
        self.d_projetos.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/icones/workness.svg);\n"
"	background-repeat: no-repeat;\n"
"	background-position: left;\n"
"	qproperty-alignment: AlignRight;\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(52, 152, 219);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(0, 153, 255);\n"
"	\n"
"	font: 11pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.d_projetos)

        self.c_contatos = QPushButton(self.b_botoes_top_aside)
        self.c_contatos.setObjectName(u"c_contatos")
        self.c_contatos.setMinimumSize(QSize(120, 30))
        self.c_contatos.setMaximumSize(QSize(120, 30))
        self.c_contatos.setCursor(QCursor(Qt.PointingHandCursor))
        self.c_contatos.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/icones/contact.svg);\n"
"	background-repeat: no-repeat;\n"
"	background-position: left;\n"
"	qproperty-alignment: AlignRight;\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(0, 153, 255);\n"
"	\n"
"	font: 11pt \"MS Shell Dlg 2\";\n"
"	\n"
"\n"
"}")

        self.verticalLayout_2.addWidget(self.c_contatos)


        self.verticalLayout_4.addWidget(self.a_top_aside)

        self.b_space_aside = QFrame(self.a_barra_lateral)
        self.b_space_aside.setObjectName(u"b_space_aside")
        self.b_space_aside.setFrameShape(QFrame.NoFrame)
        self.b_space_aside.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.b_space_aside)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.verticalSpacer = QSpacerItem(20, 252, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout_4.addWidget(self.b_space_aside)

        self.c_bottom_aside = QFrame(self.a_barra_lateral)
        self.c_bottom_aside.setObjectName(u"c_bottom_aside")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.c_bottom_aside.sizePolicy().hasHeightForWidth())
        self.c_bottom_aside.setSizePolicy(sizePolicy2)
        self.c_bottom_aside.setMinimumSize(QSize(120, 120))
        self.c_bottom_aside.setMaximumSize(QSize(120, 120))
        self.c_bottom_aside.setLayoutDirection(Qt.RightToLeft)
        self.c_bottom_aside.setStyleSheet(u"background-color: transparent;\n"
"border: none;\n"
"color: white;")
        self.c_bottom_aside.setFrameShape(QFrame.NoFrame)
        self.c_bottom_aside.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.c_bottom_aside)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, -1, 0, 0)
        self.a_informacoes = QPushButton(self.c_bottom_aside)
        self.a_informacoes.setObjectName(u"a_informacoes")
        self.a_informacoes.setEnabled(True)
        self.a_informacoes.setMinimumSize(QSize(120, 30))
        self.a_informacoes.setMaximumSize(QSize(120, 30))
        self.a_informacoes.setCursor(QCursor(Qt.PointingHandCursor))
        self.a_informacoes.setLayoutDirection(Qt.RightToLeft)
        self.a_informacoes.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/icones/help.svg);\n"
"	background-repeat: no-repeat;\n"
"	background-position: left;\n"
"	qproperty-alignment: AlignRight;\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(0, 153, 255);\n"
"	\n"
"	font: 11pt \"MS Shell Dlg 2\";\n"
"	\n"
"}")

        self.verticalLayout_3.addWidget(self.a_informacoes)

        self.b_sair = QPushButton(self.c_bottom_aside)
        self.b_sair.setObjectName(u"b_sair")
        self.b_sair.setMinimumSize(QSize(120, 30))
        self.b_sair.setMaximumSize(QSize(120, 16777215))
        self.b_sair.setCursor(QCursor(Qt.PointingHandCursor))
        self.b_sair.setLayoutDirection(Qt.LeftToRight)
        self.b_sair.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/icones/logout.svg);\n"
"	background-repeat: no-repeat;\n"
"	background-position: left;\n"
"	qproperty-alignment: AlignRight;\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"	margin-right: 30px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(0, 153, 255);\n"
"	\n"
"	font: 11pt \"MS Shell Dlg 2\";\n"
"	\n"
"}")

        self.verticalLayout_3.addWidget(self.b_sair)

        self.c_version = QFrame(self.c_bottom_aside)
        self.c_version.setObjectName(u"c_version")
        self.c_version.setMinimumSize(QSize(110, 30))
        self.c_version.setMaximumSize(QSize(110, 30))
        self.c_version.setFrameShape(QFrame.NoFrame)
        self.c_version.setFrameShadow(QFrame.Raised)
        self.version = QLabel(self.c_version)
        self.version.setObjectName(u"version")
        self.version.setGeometry(QRect(0, 0, 110, 30))
        self.version.setMinimumSize(QSize(110, 30))
        self.version.setMaximumSize(QSize(110, 30))
        self.version.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.c_version)


        self.verticalLayout_4.addWidget(self.c_bottom_aside)


        self.horizontalLayout.addWidget(self.a_barra_lateral)

        self.b_conteudo = QFrame(self.centralwidget)
        self.b_conteudo.setObjectName(u"b_conteudo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(100)
        sizePolicy3.setVerticalStretch(100)
        sizePolicy3.setHeightForWidth(self.b_conteudo.sizePolicy().hasHeightForWidth())
        self.b_conteudo.setSizePolicy(sizePolicy3)
        self.b_conteudo.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 230, 255, 255), stop:1 rgba(240, 250, 255, 255));\n"
"")
        self.b_conteudo.setFrameShape(QFrame.NoFrame)
        self.b_conteudo.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.b_conteudo)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.barra_widgets = QTabWidget(self.b_conteudo)
        self.barra_widgets.setObjectName(u"barra_widgets")
        self.barra_widgets.setMinimumSize(QSize(720, 720))
        self.barra_widgets.setStyleSheet(u"")
        self.barra_widgets.setTabShape(QTabWidget.Triangular)
        self.barra_widgets.setIconSize(QSize(16, 16))
        self.barra_widgets.setElideMode(Qt.ElideNone)
        self.a_ProjetoWebSite = QWidget()
        self.a_ProjetoWebSite.setObjectName(u"a_ProjetoWebSite")
        self.a_ProjetoWebSite.setStyleSheet(u"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(155, 89, 182, 255), stop:1 rgba(245, 203, 255, 255));\n"
"")
        self.verticalLayout_17 = QVBoxLayout(self.a_ProjetoWebSite)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.conteudo_2 = QFrame(self.a_ProjetoWebSite)
        self.conteudo_2.setObjectName(u"conteudo_2")
        self.conteudo_2.setMinimumSize(QSize(0, 0))
        self.conteudo_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"\n"
"")
        self.conteudo_2.setFrameShape(QFrame.NoFrame)
        self.conteudo_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.conteudo_2)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.container_2 = QFrame(self.conteudo_2)
        self.container_2.setObjectName(u"container_2")
        self.container_2.setMinimumSize(QSize(360, 328))
        self.container_2.setStyleSheet(u"background-color: none;")
        self.container_2.setFrameShape(QFrame.NoFrame)
        self.container_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.container_2)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.a_top_conteudo_2 = QFrame(self.container_2)
        self.a_top_conteudo_2.setObjectName(u"a_top_conteudo_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.a_top_conteudo_2.sizePolicy().hasHeightForWidth())
        self.a_top_conteudo_2.setSizePolicy(sizePolicy4)
        self.a_top_conteudo_2.setMinimumSize(QSize(1080, 320))
        self.a_top_conteudo_2.setMaximumSize(QSize(1920, 330))
        self.a_top_conteudo_2.setStyleSheet(u"")
        self.a_top_conteudo_2.setFrameShape(QFrame.StyledPanel)
        self.a_top_conteudo_2.setFrameShadow(QFrame.Raised)
        self.frame_11 = QFrame(self.a_top_conteudo_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(393, 10, 350, 320))
        self.frame_11.setMinimumSize(QSize(350, 320))
        self.frame_11.setMaximumSize(QSize(260, 300))
        self.frame_11.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	background-image: url(:/icones/login_web.png);\n"
"	border-radius: 10px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QFrame:clicked{\n"
"	height: 350px;\n"
"}")
        self.frame_22 = QFrame(self.a_top_conteudo_2)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(110, 55, 265, 240))
        sizePolicy4.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy4)
        self.frame_22.setStyleSheet(u"background-image: url(:/icones/pagina_web-1.png);\n"
"background-color: transparent;\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.frame_23 = QFrame(self.a_top_conteudo_2)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(760, 55, 265, 240))
        sizePolicy4.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy4)
        self.frame_23.setStyleSheet(u"background-image: url(:/icones/pagina_web-2.png);\n"
"background-color: transparent;\n"
"border-radius: 10px;\n"
"border: 1px solid black;")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.a_top_conteudo_2)

        self.b_conteudo_central_2 = QFrame(self.container_2)
        self.b_conteudo_central_2.setObjectName(u"b_conteudo_central_2")
        self.b_conteudo_central_2.setStyleSheet(u"background-color: none;")
        self.b_conteudo_central_2.setFrameShape(QFrame.NoFrame)
        self.b_conteudo_central_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.b_conteudo_central_2)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.a_titulo_subtitulo_2 = QFrame(self.b_conteudo_central_2)
        self.a_titulo_subtitulo_2.setObjectName(u"a_titulo_subtitulo_2")
        self.a_titulo_subtitulo_2.setMinimumSize(QSize(1135, 100))
        self.a_titulo_subtitulo_2.setMaximumSize(QSize(16777215, 100))
        self.a_titulo_subtitulo_2.setStyleSheet(u"")
        self.a_titulo_subtitulo_2.setFrameShape(QFrame.NoFrame)
        self.a_titulo_subtitulo_2.setFrameShadow(QFrame.Raised)
        self.a_titulo_2 = QFrame(self.a_titulo_subtitulo_2)
        self.a_titulo_2.setObjectName(u"a_titulo_2")
        self.a_titulo_2.setGeometry(QRect(0, 0, 1144, 48))
        self.a_titulo_2.setStyleSheet(u"background-color: none;")
        self.a_titulo_2.setFrameShape(QFrame.NoFrame)
        self.a_titulo_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.a_titulo_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.titulo_2 = QLabel(self.a_titulo_2)
        self.titulo_2.setObjectName(u"titulo_2")
        sizePolicy4.setHeightForWidth(self.titulo_2.sizePolicy().hasHeightForWidth())
        self.titulo_2.setSizePolicy(sizePolicy4)
        self.titulo_2.setMinimumSize(QSize(1135, 30))
        self.titulo_2.setMaximumSize(QSize(16777215, 16777215))
        self.titulo_2.setStyleSheet(u"color: #222;\n"
"font: 63 italic 16pt \"Segoe UI Semibold\";")
        self.titulo_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.titulo_2)

        self.b_subtitulo_2 = QFrame(self.a_titulo_subtitulo_2)
        self.b_subtitulo_2.setObjectName(u"b_subtitulo_2")
        self.b_subtitulo_2.setGeometry(QRect(0, 54, 1155, 45))
        self.b_subtitulo_2.setMinimumSize(QSize(0, 30))
        self.b_subtitulo_2.setStyleSheet(u"background-color: none;")
        self.b_subtitulo_2.setFrameShape(QFrame.StyledPanel)
        self.b_subtitulo_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.b_subtitulo_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.subtitulo_2 = QLabel(self.b_subtitulo_2)
        self.subtitulo_2.setObjectName(u"subtitulo_2")
        sizePolicy4.setHeightForWidth(self.subtitulo_2.sizePolicy().hasHeightForWidth())
        self.subtitulo_2.setSizePolicy(sizePolicy4)
        self.subtitulo_2.setMinimumSize(QSize(1135, 25))
        self.subtitulo_2.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: #222;")
        self.subtitulo_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_15.addWidget(self.subtitulo_2)


        self.verticalLayout_14.addWidget(self.a_titulo_subtitulo_2)

        self.b_cards_e_descricao_2 = QFrame(self.b_conteudo_central_2)
        self.b_cards_e_descricao_2.setObjectName(u"b_cards_e_descricao_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.b_cards_e_descricao_2.sizePolicy().hasHeightForWidth())
        self.b_cards_e_descricao_2.setSizePolicy(sizePolicy5)
        self.b_cards_e_descricao_2.setStyleSheet(u"background-color: none;")
        self.b_cards_e_descricao_2.setFrameShape(QFrame.NoFrame)
        self.b_cards_e_descricao_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.b_cards_e_descricao_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.a_cards_2 = QWidget(self.b_cards_e_descricao_2)
        self.a_cards_2.setObjectName(u"a_cards_2")
        sizePolicy5.setHeightForWidth(self.a_cards_2.sizePolicy().hasHeightForWidth())
        self.a_cards_2.setSizePolicy(sizePolicy5)
        self.a_cards_2.setMinimumSize(QSize(1130, 140))
        self.a_cards_2.setMaximumSize(QSize(16777215, 250))
        self.a_cards_2.setSizeIncrement(QSize(0, 150))
        self.a_card_esquerdo_2 = QFrame(self.a_cards_2)
        self.a_card_esquerdo_2.setObjectName(u"a_card_esquerdo_2")
        self.a_card_esquerdo_2.setGeometry(QRect(180, 0, 172, 175))
        self.a_card_esquerdo_2.setMinimumSize(QSize(162, 175))
        self.a_card_esquerdo_2.setStyleSheet(u"background-color: #a1c1e1;\n"
"border: 1px solid #7aa6d4;\n"
"border-radius: 10px;")
        self.a_card_esquerdo_2.setFrameShape(QFrame.StyledPanel)
        self.a_card_esquerdo_2.setFrameShadow(QFrame.Raised)
        self.a_icone_top_4 = QLabel(self.a_card_esquerdo_2)
        self.a_icone_top_4.setObjectName(u"a_icone_top_4")
        self.a_icone_top_4.setGeometry(QRect(56, 15, 60, 60))
        self.a_icone_top_4.setStyleSheet(u"image: url(:/icones/photo.svg);\n"
"border: none;")
        self.c_titulo_4 = QLabel(self.a_card_esquerdo_2)
        self.c_titulo_4.setObjectName(u"c_titulo_4")
        self.c_titulo_4.setGeometry(QRect(22, 100, 145, 30))
        self.c_titulo_4.setStyleSheet(u"border: none;\n"
"font: 12pt \"Segoe UI\";\n"
"color: #222;\n"
"border-top: 1px solid #7aa6d4;\n"
"border-radius: none;")
        self.c_titulo_4.setAlignment(Qt.AlignCenter)
        self.d_subtitulo_4 = QLabel(self.a_card_esquerdo_2)
        self.d_subtitulo_4.setObjectName(u"d_subtitulo_4")
        self.d_subtitulo_4.setGeometry(QRect(5, 130, 162, 30))
        self.d_subtitulo_4.setStyleSheet(u"border: none;\n"
"border-radius: none;")
        self.d_subtitulo_4.setAlignment(Qt.AlignCenter)
        self.b_icone_titulo_4 = QLabel(self.a_card_esquerdo_2)
        self.b_icone_titulo_4.setObjectName(u"b_icone_titulo_4")
        self.b_icone_titulo_4.setGeometry(QRect(2, 108, 21, 16))
        self.b_icone_titulo_4.setStyleSheet(u"image: url(:/icones/check.svg);\n"
"image: url(:/icones/shield.svg);\n"
"border: none;")
        self.b_card_centro_2 = QFrame(self.a_cards_2)
        self.b_card_centro_2.setObjectName(u"b_card_centro_2")
        self.b_card_centro_2.setGeometry(QRect(470, 0, 172, 175))
        self.b_card_centro_2.setMinimumSize(QSize(162, 120))
        self.b_card_centro_2.setStyleSheet(u"background-color: #a1c1e1;\n"
"border: 1px solid #7aa6d4;\n"
"border-radius: 10px;")
        self.b_card_centro_2.setFrameShape(QFrame.StyledPanel)
        self.b_card_centro_2.setFrameShadow(QFrame.Raised)
        self.a_icone_top_5 = QLabel(self.b_card_centro_2)
        self.a_icone_top_5.setObjectName(u"a_icone_top_5")
        self.a_icone_top_5.setGeometry(QRect(56, 15, 60, 60))
        self.a_icone_top_5.setStyleSheet(u"image: url(:/icones/camera.svg);\n"
"border: none;")
        self.c_titulo_5 = QLabel(self.b_card_centro_2)
        self.c_titulo_5.setObjectName(u"c_titulo_5")
        self.c_titulo_5.setGeometry(QRect(15, 100, 152, 30))
        self.c_titulo_5.setStyleSheet(u"border: none;\n"
"font: 12pt \"Segoe UI\";\n"
"color: #222;\n"
"border-top: 1px solid #7aa6d4;\n"
"border-radius: none;")
        self.c_titulo_5.setAlignment(Qt.AlignCenter)
        self.d_subtitulo_5 = QLabel(self.b_card_centro_2)
        self.d_subtitulo_5.setObjectName(u"d_subtitulo_5")
        self.d_subtitulo_5.setGeometry(QRect(5, 130, 162, 30))
        self.d_subtitulo_5.setStyleSheet(u"border: none;\n"
"border-radius: none;")
        self.d_subtitulo_5.setAlignment(Qt.AlignCenter)
        self.b_icone_titulo_5 = QLabel(self.b_card_centro_2)
        self.b_icone_titulo_5.setObjectName(u"b_icone_titulo_5")
        self.b_icone_titulo_5.setGeometry(QRect(20, 108, 21, 16))
        self.b_icone_titulo_5.setStyleSheet(u"image: url(:/icones/check.svg);\n"
"image: url(:/icones/shield.svg);\n"
"border: none;")
        self.c_card_direito_2 = QFrame(self.a_cards_2)
        self.c_card_direito_2.setObjectName(u"c_card_direito_2")
        self.c_card_direito_2.setGeometry(QRect(744, 0, 172, 175))
        self.c_card_direito_2.setMinimumSize(QSize(162, 175))
        self.c_card_direito_2.setStyleSheet(u"background-color: #a1c1e1;\n"
"border: 1px solid #7aa6d4;\n"
"border-radius: 10px;")
        self.c_card_direito_2.setFrameShape(QFrame.StyledPanel)
        self.c_card_direito_2.setFrameShadow(QFrame.Raised)
        self.a_icone_top_6 = QLabel(self.c_card_direito_2)
        self.a_icone_top_6.setObjectName(u"a_icone_top_6")
        self.a_icone_top_6.setGeometry(QRect(56, 15, 60, 60))
        self.a_icone_top_6.setStyleSheet(u"image: url(:/icones/globo.svg);\n"
"border: none;")
        self.c_titulo_6 = QLabel(self.c_card_direito_2)
        self.c_titulo_6.setObjectName(u"c_titulo_6")
        self.c_titulo_6.setGeometry(QRect(20, 100, 142, 30))
        self.c_titulo_6.setStyleSheet(u"border: none;\n"
"font: 12pt \"Segoe UI\";\n"
"color: #222;\n"
"border-top: 1px solid #7aa6d4;\n"
"border-radius: none;")
        self.c_titulo_6.setAlignment(Qt.AlignCenter)
        self.d_subtitulo_6 = QLabel(self.c_card_direito_2)
        self.d_subtitulo_6.setObjectName(u"d_subtitulo_6")
        self.d_subtitulo_6.setGeometry(QRect(5, 130, 162, 30))
        self.d_subtitulo_6.setStyleSheet(u"border: none;\n"
"border-radius: none;")
        self.d_subtitulo_6.setAlignment(Qt.AlignCenter)
        self.b_icone_titulo_6 = QLabel(self.c_card_direito_2)
        self.b_icone_titulo_6.setObjectName(u"b_icone_titulo_6")
        self.b_icone_titulo_6.setGeometry(QRect(50, 108, 21, 16))
        self.b_icone_titulo_6.setStyleSheet(u"image: url(:/icones/check.svg);\n"
"image: url(:/icones/shield.svg);\n"
"border: none;")

        self.verticalLayout_16.addWidget(self.a_cards_2)

        self.a_linha_2 = QFrame(self.b_cards_e_descricao_2)
        self.a_linha_2.setObjectName(u"a_linha_2")
        self.a_linha_2.setStyleSheet(u"")
        self.a_linha_2.setFrameShape(QFrame.Shape.HLine)
        self.a_linha_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_16.addWidget(self.a_linha_2)

        self.c_descricao_texto_2 = QFrame(self.b_cards_e_descricao_2)
        self.c_descricao_texto_2.setObjectName(u"c_descricao_texto_2")
        self.c_descricao_texto_2.setFrameShape(QFrame.StyledPanel)
        self.c_descricao_texto_2.setFrameShadow(QFrame.Raised)
        self.descricao_texto_2 = QLabel(self.c_descricao_texto_2)
        self.descricao_texto_2.setObjectName(u"descricao_texto_2")
        self.descricao_texto_2.setGeometry(QRect(1, 32, 1119, 251))
        sizePolicy5.setHeightForWidth(self.descricao_texto_2.sizePolicy().hasHeightForWidth())
        self.descricao_texto_2.setSizePolicy(sizePolicy5)
        self.descricao_texto_2.setMinimumSize(QSize(1080, 220))
        self.descricao_texto_2.setMaximumSize(QSize(16777215, 275))
        self.descricao_texto_2.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.descricao_texto_2.setFrameShadow(QFrame.Plain)
        self.descricao_texto_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.descricao_titulo_2 = QLabel(self.c_descricao_texto_2)
        self.descricao_titulo_2.setObjectName(u"descricao_titulo_2")
        self.descricao_titulo_2.setGeometry(QRect(1, 1, 100, 25))
        self.descricao_titulo_2.setMinimumSize(QSize(100, 25))
        self.descricao_titulo_2.setMaximumSize(QSize(100, 25))
        self.descricao_titulo_2.setStyleSheet(u"color: #222;\n"
"font: 12pt \"Segoe UI\";")

        self.verticalLayout_16.addWidget(self.c_descricao_texto_2)


        self.verticalLayout_14.addWidget(self.b_cards_e_descricao_2)


        self.verticalLayout_13.addWidget(self.b_conteudo_central_2)


        self.verticalLayout_12.addWidget(self.container_2)


        self.verticalLayout_17.addWidget(self.conteudo_2)

        self.barra_widgets.addTab(self.a_ProjetoWebSite, "")
        self.b_ProjetodeSoftware = QWidget()
        self.b_ProjetodeSoftware.setObjectName(u"b_ProjetodeSoftware")
        self.verticalLayout_6 = QVBoxLayout(self.b_ProjetodeSoftware)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.conteudo = QFrame(self.b_ProjetodeSoftware)
        self.conteudo.setObjectName(u"conteudo")
        self.conteudo.setMinimumSize(QSize(0, 0))
        self.conteudo.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.conteudo.setFrameShape(QFrame.NoFrame)
        self.conteudo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.conteudo)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.container = QFrame(self.conteudo)
        self.container.setObjectName(u"container")
        self.container.setMinimumSize(QSize(360, 328))
        self.container.setStyleSheet(u"background-color: none;")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.container)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.a_top_conteudo = QFrame(self.container)
        self.a_top_conteudo.setObjectName(u"a_top_conteudo")
        sizePolicy4.setHeightForWidth(self.a_top_conteudo.sizePolicy().hasHeightForWidth())
        self.a_top_conteudo.setSizePolicy(sizePolicy4)
        self.a_top_conteudo.setMinimumSize(QSize(1080, 320))
        self.a_top_conteudo.setMaximumSize(QSize(1920, 330))
        self.a_top_conteudo.setStyleSheet(u"")
        self.a_top_conteudo.setFrameShape(QFrame.StyledPanel)
        self.a_top_conteudo.setFrameShadow(QFrame.Raised)
        self.frame_10 = QFrame(self.a_top_conteudo)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(393, 10, 350, 320))
        self.frame_10.setMinimumSize(QSize(350, 320))
        self.frame_10.setMaximumSize(QSize(260, 300))
        self.frame_10.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	background-image: url(:/icones/Projeto_1.png);\n"
"	border-radius: 10px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QFrame:clicked{\n"
"	height: 350px;\n"
"}")
        self.frame_20 = QFrame(self.a_top_conteudo)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(110, 55, 265, 240))
        sizePolicy4.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy4)
        self.frame_20.setStyleSheet(u"background-image: url(:/icones/Projeto_2.png);\n"
"background-color: transparent;\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.frame_21 = QFrame(self.a_top_conteudo)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(760, 55, 265, 240))
        sizePolicy4.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy4)
        self.frame_21.setStyleSheet(u"background-image: url(:/icones/projeto_3.png);\n"
"background-color: transparent;\n"
"border-radius: 10px;\n"
"border: 1px solid black;")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.a_top_conteudo)

        self.b_conteudo_central = QFrame(self.container)
        self.b_conteudo_central.setObjectName(u"b_conteudo_central")
        self.b_conteudo_central.setStyleSheet(u"background-color: none;")
        self.b_conteudo_central.setFrameShape(QFrame.NoFrame)
        self.b_conteudo_central.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.b_conteudo_central)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.a_titulo_subtitulo = QFrame(self.b_conteudo_central)
        self.a_titulo_subtitulo.setObjectName(u"a_titulo_subtitulo")
        self.a_titulo_subtitulo.setMinimumSize(QSize(1135, 100))
        self.a_titulo_subtitulo.setMaximumSize(QSize(16777215, 100))
        self.a_titulo_subtitulo.setStyleSheet(u"")
        self.a_titulo_subtitulo.setFrameShape(QFrame.NoFrame)
        self.a_titulo_subtitulo.setFrameShadow(QFrame.Raised)
        self.a_titulo = QFrame(self.a_titulo_subtitulo)
        self.a_titulo.setObjectName(u"a_titulo")
        self.a_titulo.setGeometry(QRect(0, 0, 1144, 48))
        self.a_titulo.setStyleSheet(u"background-color: none;")
        self.a_titulo.setFrameShape(QFrame.NoFrame)
        self.a_titulo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.a_titulo)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.titulo = QLabel(self.a_titulo)
        self.titulo.setObjectName(u"titulo")
        sizePolicy4.setHeightForWidth(self.titulo.sizePolicy().hasHeightForWidth())
        self.titulo.setSizePolicy(sizePolicy4)
        self.titulo.setMinimumSize(QSize(1135, 30))
        self.titulo.setMaximumSize(QSize(16777215, 16777215))
        self.titulo.setStyleSheet(u"font: 63 italic 16pt \"Segoe UI Semibold\";\n"
"color: #222;")
        self.titulo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.titulo)

        self.b_subtitulo = QFrame(self.a_titulo_subtitulo)
        self.b_subtitulo.setObjectName(u"b_subtitulo")
        self.b_subtitulo.setGeometry(QRect(0, 54, 1155, 45))
        self.b_subtitulo.setMinimumSize(QSize(0, 30))
        self.b_subtitulo.setStyleSheet(u"background-color: none;")
        self.b_subtitulo.setFrameShape(QFrame.StyledPanel)
        self.b_subtitulo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.b_subtitulo)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.subtitulo = QLabel(self.b_subtitulo)
        self.subtitulo.setObjectName(u"subtitulo")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.subtitulo.sizePolicy().hasHeightForWidth())
        self.subtitulo.setSizePolicy(sizePolicy6)
        self.subtitulo.setMinimumSize(QSize(1135, 25))
        self.subtitulo.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: #222;")
        self.subtitulo.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_11.addWidget(self.subtitulo)


        self.verticalLayout_8.addWidget(self.a_titulo_subtitulo)

        self.b_cards_e_descricao = QFrame(self.b_conteudo_central)
        self.b_cards_e_descricao.setObjectName(u"b_cards_e_descricao")
        self.b_cards_e_descricao.setStyleSheet(u"background-color: none;")
        self.b_cards_e_descricao.setFrameShape(QFrame.NoFrame)
        self.b_cards_e_descricao.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.b_cards_e_descricao)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(9, 9, 9, 0)
        self.a_cards = QWidget(self.b_cards_e_descricao)
        self.a_cards.setObjectName(u"a_cards")
        self.a_cards.setMinimumSize(QSize(1800, 140))
        self.a_cards.setMaximumSize(QSize(16777215, 250))
        self.a_cards.setSizeIncrement(QSize(0, 150))
        self.a_card_esquerdo = QFrame(self.a_cards)
        self.a_card_esquerdo.setObjectName(u"a_card_esquerdo")
        self.a_card_esquerdo.setGeometry(QRect(180, 0, 192, 220))
        self.a_card_esquerdo.setMinimumSize(QSize(180, 220))
        self.a_card_esquerdo.setStyleSheet(u"background-color: #a1c1e1;\n"
"border: 1px solid #7aa6d4;\n"
"border-radius: 10px;")
        self.a_card_esquerdo.setFrameShape(QFrame.StyledPanel)
        self.a_card_esquerdo.setFrameShadow(QFrame.Raised)
        self.a_icone_top = QLabel(self.a_card_esquerdo)
        self.a_icone_top.setObjectName(u"a_icone_top")
        self.a_icone_top.setGeometry(QRect(66, 15, 60, 60))
        self.a_icone_top.setStyleSheet(u"image: url(:/icones/store.svg);\n"
"border: none;")
        self.c_titulo = QLabel(self.a_card_esquerdo)
        self.c_titulo.setObjectName(u"c_titulo")
        self.c_titulo.setGeometry(QRect(10, 150, 171, 30))
        self.c_titulo.setStyleSheet(u"border: none;\n"
"font: 12pt \"Segoe UI\";\n"
"color: #222;\n"
"border-top: 1px solid #7aa6d4;\n"
"border-radius: none;")
        self.c_titulo.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.d_subtitulo = QLabel(self.a_card_esquerdo)
        self.d_subtitulo.setObjectName(u"d_subtitulo")
        self.d_subtitulo.setGeometry(QRect(5, 175, 180, 41))
        self.d_subtitulo.setStyleSheet(u"border: none;\n"
"border-radius: none;")
        self.d_subtitulo.setAlignment(Qt.AlignCenter)
        self.b_icone_titulo = QLabel(self.a_card_esquerdo)
        self.b_icone_titulo.setObjectName(u"b_icone_titulo")
        self.b_icone_titulo.setGeometry(QRect(5, 160, 21, 16))
        self.b_icone_titulo.setStyleSheet(u"image: url(:/icones/check.svg);\n"
"image: url(:/icones/shield.svg);\n"
"border: none;")
        self.b_card_centro = QFrame(self.a_cards)
        self.b_card_centro.setObjectName(u"b_card_centro")
        self.b_card_centro.setGeometry(QRect(470, 0, 192, 220))
        self.b_card_centro.setMinimumSize(QSize(192, 220))
        self.b_card_centro.setStyleSheet(u"background-color: #a1c1e1;\n"
"border: 1px solid #7aa6d4;\n"
"border-radius: 10px;")
        self.b_card_centro.setFrameShape(QFrame.StyledPanel)
        self.b_card_centro.setFrameShadow(QFrame.Raised)
        self.a_icone_top_2 = QLabel(self.b_card_centro)
        self.a_icone_top_2.setObjectName(u"a_icone_top_2")
        self.a_icone_top_2.setGeometry(QRect(66, 15, 60, 60))
        self.a_icone_top_2.setStyleSheet(u"image: url(:/icones/ads_click.svg);\n"
"border: none;")
        self.c_titulo_2 = QLabel(self.b_card_centro)
        self.c_titulo_2.setObjectName(u"c_titulo_2")
        self.c_titulo_2.setGeometry(QRect(10, 150, 171, 30))
        self.c_titulo_2.setStyleSheet(u"border: none;\n"
"font: 12pt \"Segoe UI\";\n"
"color: #222;\n"
"border-top: 1px solid #7aa6d4;\n"
"border-radius: none;")
        self.c_titulo_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.d_subtitulo_2 = QLabel(self.b_card_centro)
        self.d_subtitulo_2.setObjectName(u"d_subtitulo_2")
        self.d_subtitulo_2.setGeometry(QRect(5, 175, 180, 41))
        self.d_subtitulo_2.setStyleSheet(u"border: none;\n"
"border-radius: none;")
        self.d_subtitulo_2.setAlignment(Qt.AlignCenter)
        self.b_icone_titulo_2 = QLabel(self.b_card_centro)
        self.b_icone_titulo_2.setObjectName(u"b_icone_titulo_2")
        self.b_icone_titulo_2.setGeometry(QRect(40, 160, 21, 16))
        self.b_icone_titulo_2.setStyleSheet(u"image: url(:/icones/check.svg);\n"
"image: url(:/icones/shield.svg);\n"
"border: none;")
        self.c_card_direito = QFrame(self.a_cards)
        self.c_card_direito.setObjectName(u"c_card_direito")
        self.c_card_direito.setGeometry(QRect(744, 0, 192, 220))
        self.c_card_direito.setMinimumSize(QSize(192, 220))
        self.c_card_direito.setStyleSheet(u"background-color: #a1c1e1;\n"
"border: 1px solid #7aa6d4;\n"
"border-radius: 10px;")
        self.c_card_direito.setFrameShape(QFrame.StyledPanel)
        self.c_card_direito.setFrameShadow(QFrame.Raised)
        self.a_icone_top_3 = QLabel(self.c_card_direito)
        self.a_icone_top_3.setObjectName(u"a_icone_top_3")
        self.a_icone_top_3.setGeometry(QRect(66, 15, 60, 60))
        self.a_icone_top_3.setStyleSheet(u"image: url(:/icones/finance.svg);\n"
"border: none;")
        self.c_titulo_3 = QLabel(self.c_card_direito)
        self.c_titulo_3.setObjectName(u"c_titulo_3")
        self.c_titulo_3.setGeometry(QRect(10, 150, 175, 30))
        self.c_titulo_3.setStyleSheet(u"border: none;\n"
"font: 12pt \"Segoe UI\";\n"
"color: #222;\n"
"border-top: 1px solid #7aa6d4;\n"
"border-radius: none;")
        self.c_titulo_3.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.d_subtitulo_3 = QLabel(self.c_card_direito)
        self.d_subtitulo_3.setObjectName(u"d_subtitulo_3")
        self.d_subtitulo_3.setGeometry(QRect(5, 175, 180, 41))
        self.d_subtitulo_3.setStyleSheet(u"border: none;\n"
"border-radius: none;")
        self.d_subtitulo_3.setAlignment(Qt.AlignCenter)
        self.b_icone_titulo_3 = QLabel(self.c_card_direito)
        self.b_icone_titulo_3.setObjectName(u"b_icone_titulo_3")
        self.b_icone_titulo_3.setGeometry(QRect(5, 160, 21, 16))
        self.b_icone_titulo_3.setStyleSheet(u"image: url(:/icones/check.svg);\n"
"image: url(:/icones/shield.svg);\n"
"border: none;")

        self.verticalLayout_10.addWidget(self.a_cards)

        self.a_linha = QFrame(self.b_cards_e_descricao)
        self.a_linha.setObjectName(u"a_linha")
        self.a_linha.setStyleSheet(u"")
        self.a_linha.setFrameShape(QFrame.Shape.HLine)
        self.a_linha.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_10.addWidget(self.a_linha)

        self.b_descricao_titulo = QFrame(self.b_cards_e_descricao)
        self.b_descricao_titulo.setObjectName(u"b_descricao_titulo")
        self.b_descricao_titulo.setMinimumSize(QSize(0, 25))
        self.b_descricao_titulo.setMaximumSize(QSize(16777215, 25))
        self.b_descricao_titulo.setFrameShape(QFrame.NoFrame)
        self.b_descricao_titulo.setFrameShadow(QFrame.Raised)
        self.descricao_titulo = QLabel(self.b_descricao_titulo)
        self.descricao_titulo.setObjectName(u"descricao_titulo")
        self.descricao_titulo.setGeometry(QRect(0, 0, 101, 25))
        sizePolicy4.setHeightForWidth(self.descricao_titulo.sizePolicy().hasHeightForWidth())
        self.descricao_titulo.setSizePolicy(sizePolicy4)
        self.descricao_titulo.setMinimumSize(QSize(0, 25))
        self.descricao_titulo.setMaximumSize(QSize(16777215, 25))
        self.descricao_titulo.setStyleSheet(u"color: #222;\n"
"font: 12pt \"Segoe UI\";")

        self.verticalLayout_10.addWidget(self.b_descricao_titulo)

        self.c_descricao_texto = QFrame(self.b_cards_e_descricao)
        self.c_descricao_texto.setObjectName(u"c_descricao_texto")
        self.c_descricao_texto.setFrameShape(QFrame.StyledPanel)
        self.c_descricao_texto.setFrameShadow(QFrame.Raised)
        self.descricao_texto = QLabel(self.c_descricao_texto)
        self.descricao_texto.setObjectName(u"descricao_texto")
        self.descricao_texto.setGeometry(QRect(0, 0, 1130, 300))
        self.descricao_texto.setMinimumSize(QSize(1080, 300))
        self.descricao_texto.setMaximumSize(QSize(16777215, 275))
        self.descricao_texto.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.descricao_texto.setFrameShadow(QFrame.Plain)
        self.descricao_texto.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_10.addWidget(self.c_descricao_texto)


        self.verticalLayout_8.addWidget(self.b_cards_e_descricao)


        self.verticalLayout_9.addWidget(self.b_conteudo_central)


        self.verticalLayout_7.addWidget(self.container)


        self.verticalLayout_6.addWidget(self.conteudo)

        self.barra_widgets.addTab(self.b_ProjetodeSoftware, "")

        self.verticalLayout.addWidget(self.barra_widgets)


        self.horizontalLayout.addWidget(self.b_conteudo)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.barra_widgets.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.a_icone_perfil.setText("")
        self.b_nome_usuario.setText(QCoreApplication.translate("MainWindow", u"Davi Almeida", None))
        self.b_inicio.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.d_projetos.setText(QCoreApplication.translate("MainWindow", u"Projetos", None))
        self.c_contatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.a_informacoes.setText(QCoreApplication.translate("MainWindow", u"    Informa\u00e7\u00f5es", None))
        self.b_sair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"Vers\u00e3o 0.1.4", None))
        self.titulo_2.setText(QCoreApplication.translate("MainWindow", u"PIXEL PHOTO", None))
        self.subtitulo_2.setText(QCoreApplication.translate("MainWindow", u"CONHECENDO AS MARAVILHAS DO MUNDO!", None))
        self.a_icone_top_4.setText("")
        self.c_titulo_4.setText(QCoreApplication.translate("MainWindow", u"Cole\u00e7\u00e3o de Registros", None))
        self.d_subtitulo_4.setText(QCoreApplication.translate("MainWindow", u"     Pequenas Lojas e Autonomos", None))
        self.b_icone_titulo_4.setText("")
        self.a_icone_top_5.setText("")
        self.c_titulo_5.setText(QCoreApplication.translate("MainWindow", u"Fotos Incr\u00edveis", None))
        self.d_subtitulo_5.setText(QCoreApplication.translate("MainWindow", u"   Pequenas Lojas e Autonomos", None))
        self.b_icone_titulo_5.setText("")
        self.a_icone_top_6.setText("")
        self.c_titulo_6.setText(QCoreApplication.translate("MainWindow", u"Maps", None))
        self.d_subtitulo_6.setText(QCoreApplication.translate("MainWindow", u"Pequenas Lojas e Autonomos", None))
        self.b_icone_titulo_6.setText("")
        self.descricao_texto_2.setText(QCoreApplication.translate("MainWindow", u"     Descubra, conecte e compartilhe com o Espa\u00e7o Digital Infinito. Desenvolvido para criadores, exploradores e inovadores, este ambiente oferece uma forma moderna de organizar e apresentar conte\u00fados diversos. \n"
"\n"
"Personalize sua \u00e1rea, convide outros usu\u00e1rios e crie experi\u00eancias \u00fanicas que refletem sua ess\u00eancia.\n"
"\n"
"Destaques da plataforma:\n"
"\n"
"     -Cria\u00e7\u00e3o ilimitada de cole\u00e7\u00f5es personalizadas\n"
"\n"
"     -Organiza\u00e7\u00e3o por tags, t\u00f3picos e categorias din\u00e2micas\n"
"\n"
"     -Layout responsivo com navega\u00e7\u00e3o fluida\n"
"\n"
"     -Integra\u00e7\u00e3o com redes e canais de comunica\u00e7\u00e3o\n"
"\n"
"     -Painel de estat\u00edsticas detalhadas para monitoramento de atividades", None))
        self.descricao_titulo_2.setText(QCoreApplication.translate("MainWindow", u"DESCRI\u00c7\u00c3O", None))
        self.barra_widgets.setTabText(self.barra_widgets.indexOf(self.a_ProjetoWebSite), QCoreApplication.translate("MainWindow", u"Projeto Web Site", None))
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"LOGMARKET", None))
        self.subtitulo.setText(QCoreApplication.translate("MainWindow", u"TERMINAL DE CONSULTA E CONTROLE DE ESTOQUE", None))
        self.a_icone_top.setText("")
        self.c_titulo.setText(QCoreApplication.translate("MainWindow", u"     Ideal para o Com\u00e9rcio", None))
        self.d_subtitulo.setText(QCoreApplication.translate("MainWindow", u"Pequenas Lojas e Autonomos", None))
        self.b_icone_titulo.setText("")
        self.a_icone_top_2.setText("")
        self.c_titulo_2.setText(QCoreApplication.translate("MainWindow", u"       Poucos Clicks", None))
        self.d_subtitulo_2.setText(QCoreApplication.translate("MainWindow", u"Pequenas Lojas e Autonomos", None))
        self.b_icone_titulo_2.setText("")
        self.a_icone_top_3.setText("")
        self.c_titulo_3.setText(QCoreApplication.translate("MainWindow", u"     Impulsionando Vendas", None))
        self.d_subtitulo_3.setText(QCoreApplication.translate("MainWindow", u"Pequenas Lojas e Autonomos", None))
        self.b_icone_titulo_3.setText("")
        self.descricao_titulo.setText(QCoreApplication.translate("MainWindow", u"DESCRI\u00c7\u00c3O", None))
        self.descricao_texto.setText(QCoreApplication.translate("MainWindow", u"     O LOGMARKET \u00e9 uma solu\u00e7\u00e3o completa para gest\u00e3o comercial, desenvolvida especialmente para empresas que desejam otimizar o processo de cadastro, consulta e venda de produtos.\n"
"Com uma interface intuitiva, o sistema permite que voc\u00ea registre novos itens rapidamente, mantenha o controle detalhado do seu cat\u00e1logo e realize vendas de maneira pr\u00e1tica e segura.\n"
"Principais recursos:\n"
"\n"
"     -Cadastro de produtos com informa\u00e7\u00f5es detalhadas, imagens e categorias personalizadas.\n"
"\n"
"     -Consulta avan\u00e7ada por filtros, c\u00f3digos ou descri\u00e7\u00f5es, facilitando a localiza\u00e7\u00e3o de produtos no estoque.\n"
"\n"
"     -Processo de vendas integrado, com emiss\u00e3o de comprovantes e relat\u00f3rios de transa\u00e7\u00f5es.\n"
"\n"
"     -Controle de estoque atualizado em tempo real.\n"
"\n"
"     -Gera\u00e7\u00e3o de relat\u00f3rios gerenciais e indicadores de desempenho.\n"
"\n"
"Voltado para com\u00e9rcios de diferentes portes, o LOGMA"
                        "RKET proporciona mais agilidade no atendimento, redu\u00e7\u00e3o de erros operacionais e maior controle sobre todas as opera\u00e7\u00f5es comerciais.", None))
        self.barra_widgets.setTabText(self.barra_widgets.indexOf(self.b_ProjetodeSoftware), QCoreApplication.translate("MainWindow", u"Projeto de Software", None))
    # retranslateUi

