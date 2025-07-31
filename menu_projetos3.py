# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teste_projetos_atualizado_2.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
        MainWindow.resize(1367, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1367, 768))
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
        self.b_inicio.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
        self.d_projetos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
        self.c_contatos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
        self.verticalSpacer = QSpacerItem(20, 240, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

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
        self.a_informacoes = QPushButton(self.c_bottom_aside)
        self.a_informacoes.setObjectName(u"a_informacoes")
        self.a_informacoes.setEnabled(True)
        self.a_informacoes.setMinimumSize(QSize(120, 30))
        self.a_informacoes.setMaximumSize(QSize(120, 30))
        self.a_informacoes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
        self.b_sair.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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

        self.version = QLabel(self.c_bottom_aside)
        self.version.setObjectName(u"version")
        self.version.setMinimumSize(QSize(110, 30))
        self.version.setMaximumSize(QSize(110, 30))
        self.version.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.version)


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
        self.barra_widgets.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 230, 255, 255), stop:1 rgba(240, 250, 255, 255));\n"
"color: black;\n"
"")
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
        self.b_conteudo_central_2 = QFrame(self.container_2)
        self.b_conteudo_central_2.setObjectName(u"b_conteudo_central_2")
        self.b_conteudo_central_2.setGeometry(QRect(1, 303, 1230, 440))
        self.b_conteudo_central_2.setStyleSheet(u"background-color: none;")
        self.b_conteudo_central_2.setFrameShape(QFrame.NoFrame)
        self.b_conteudo_central_2.setFrameShadow(QFrame.Raised)
        self.b_cards_e_descricao_2 = QFrame(self.b_conteudo_central_2)
        self.b_cards_e_descricao_2.setObjectName(u"b_cards_e_descricao_2")
        self.b_cards_e_descricao_2.setGeometry(QRect(0, 45, 1230, 190))
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.b_cards_e_descricao_2.sizePolicy().hasHeightForWidth())
        self.b_cards_e_descricao_2.setSizePolicy(sizePolicy4)
        self.b_cards_e_descricao_2.setMinimumSize(QSize(1230, 190))
        self.b_cards_e_descricao_2.setMaximumSize(QSize(16777215, 190))
        self.b_cards_e_descricao_2.setStyleSheet(u"background-color: none;")
        self.b_cards_e_descricao_2.setFrameShape(QFrame.NoFrame)
        self.b_cards_e_descricao_2.setFrameShadow(QFrame.Raised)
        self.a_cards_2 = QWidget(self.b_cards_e_descricao_2)
        self.a_cards_2.setObjectName(u"a_cards_2")
        self.a_cards_2.setGeometry(QRect(1, 0, 1230, 162))
        sizePolicy4.setHeightForWidth(self.a_cards_2.sizePolicy().hasHeightForWidth())
        self.a_cards_2.setSizePolicy(sizePolicy4)
        self.a_cards_2.setMinimumSize(QSize(1130, 160))
        self.a_cards_2.setMaximumSize(QSize(16777215, 180))
        self.a_cards_2.setSizeIncrement(QSize(0, 150))
        self.a_card_esquerdo_2 = QFrame(self.a_cards_2)
        self.a_card_esquerdo_2.setObjectName(u"a_card_esquerdo_2")
        self.a_card_esquerdo_2.setGeometry(QRect(275, 0, 175, 160))
        self.a_card_esquerdo_2.setMinimumSize(QSize(150, 160))
        self.a_card_esquerdo_2.setStyleSheet(u"background-color: #a1c1e1;\n"
"border: 1px solid #7aa6d4;\n"
"border-radius: 10px;")
        self.a_card_esquerdo_2.setFrameShape(QFrame.StyledPanel)
        self.a_card_esquerdo_2.setFrameShadow(QFrame.Raised)
        self.a_icone_top_4 = QLabel(self.a_card_esquerdo_2)
        self.a_icone_top_4.setObjectName(u"a_icone_top_4")
        self.a_icone_top_4.setGeometry(QRect(57, 15, 60, 60))
        self.a_icone_top_4.setStyleSheet(u"image: url(:/icones/photo.svg);\n"
"border: none;")
        self.c_titulo_4 = QLabel(self.a_card_esquerdo_2)
        self.c_titulo_4.setObjectName(u"c_titulo_4")
        self.c_titulo_4.setGeometry(QRect(10, 100, 155, 30))
        self.c_titulo_4.setStyleSheet(u"border: none;\n"
"font: 12pt \"Segoe UI\";\n"
"color: #222;\n"
"border-top: 1px solid #7aa6d4;\n"
"border-radius: none;")
        self.c_titulo_4.setAlignment(Qt.AlignCenter)
        self.d_subtitulo_4 = QLabel(self.a_card_esquerdo_2)
        self.d_subtitulo_4.setObjectName(u"d_subtitulo_4")
        self.d_subtitulo_4.setGeometry(QRect(7, 130, 160, 20))
        self.d_subtitulo_4.setStyleSheet(u"border: none;\n"
"border-radius: none;")
        self.d_subtitulo_4.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.b_icone_titulo_4 = QLabel(self.a_card_esquerdo_2)
        self.b_icone_titulo_4.setObjectName(u"b_icone_titulo_4")
        self.b_icone_titulo_4.setGeometry(QRect(32, 108, 21, 16))
        self.b_icone_titulo_4.setStyleSheet(u"image: url(:/icones/check.svg);\n"
"image: url(:/icones/shield.svg);\n"
"border: none;")
        self.b_card_centro_2 = QFrame(self.a_cards_2)
        self.b_card_centro_2.setObjectName(u"b_card_centro_2")
        self.b_card_centro_2.setGeometry(QRect(540, 0, 175, 160))
        self.b_card_centro_2.setMinimumSize(QSize(160, 160))
        self.b_card_centro_2.setStyleSheet(u"background-color: #a1c1e1;\n"
"border: 1px solid #7aa6d4;\n"
"border-radius: 10px;")
        self.b_card_centro_2.setFrameShape(QFrame.StyledPanel)
        self.b_card_centro_2.setFrameShadow(QFrame.Raised)
        self.a_icone_top_5 = QLabel(self.b_card_centro_2)
        self.a_icone_top_5.setObjectName(u"a_icone_top_5")
        self.a_icone_top_5.setGeometry(QRect(57, 15, 60, 60))
        self.a_icone_top_5.setStyleSheet(u"image: url(:/icones/camera.svg);\n"
"border: none;")
        self.c_titulo_5 = QLabel(self.b_card_centro_2)
        self.c_titulo_5.setObjectName(u"c_titulo_5")
        self.c_titulo_5.setGeometry(QRect(10, 100, 155, 30))
        self.c_titulo_5.setStyleSheet(u"border: none;\n"
"font: 12pt \"Segoe UI\";\n"
"color: #222;\n"
"border-top: 1px solid #7aa6d4;\n"
"border-radius: none;")
        self.c_titulo_5.setAlignment(Qt.AlignCenter)
        self.d_subtitulo_5 = QLabel(self.b_card_centro_2)
        self.d_subtitulo_5.setObjectName(u"d_subtitulo_5")
        self.d_subtitulo_5.setGeometry(QRect(7, 130, 160, 20))
        self.d_subtitulo_5.setStyleSheet(u"border: none;\n"
"border-radius: none;")
        self.d_subtitulo_5.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.b_icone_titulo_5 = QLabel(self.b_card_centro_2)
        self.b_icone_titulo_5.setObjectName(u"b_icone_titulo_5")
        self.b_icone_titulo_5.setGeometry(QRect(22, 108, 21, 16))
        self.b_icone_titulo_5.setStyleSheet(u"image: url(:/icones/check.svg);\n"
"image: url(:/icones/shield.svg);\n"
"border: none;")
        self.c_card_direito_2 = QFrame(self.a_cards_2)
        self.c_card_direito_2.setObjectName(u"c_card_direito_2")
        self.c_card_direito_2.setGeometry(QRect(795, 0, 175, 160))
        self.c_card_direito_2.setMinimumSize(QSize(160, 160))
        self.c_card_direito_2.setStyleSheet(u"background-color: #a1c1e1;\n"
"border: 1px solid #7aa6d4;\n"
"border-radius: 10px;")
        self.c_card_direito_2.setFrameShape(QFrame.StyledPanel)
        self.c_card_direito_2.setFrameShadow(QFrame.Raised)
        self.a_icone_top_6 = QLabel(self.c_card_direito_2)
        self.a_icone_top_6.setObjectName(u"a_icone_top_6")
        self.a_icone_top_6.setGeometry(QRect(57, 15, 60, 60))
        self.a_icone_top_6.setStyleSheet(u"image: url(:/icones/globo.svg);\n"
"border: none;")
        self.c_titulo_6 = QLabel(self.c_card_direito_2)
        self.c_titulo_6.setObjectName(u"c_titulo_6")
        self.c_titulo_6.setGeometry(QRect(10, 100, 155, 30))
        self.c_titulo_6.setStyleSheet(u"border: none;\n"
"font: 12pt \"Segoe UI\";\n"
"color: #222;\n"
"border-top: 1px solid #7aa6d4;\n"
"border-radius: none;")
        self.c_titulo_6.setAlignment(Qt.AlignCenter)
        self.d_subtitulo_6 = QLabel(self.c_card_direito_2)
        self.d_subtitulo_6.setObjectName(u"d_subtitulo_6")
        self.d_subtitulo_6.setGeometry(QRect(7, 130, 160, 20))
        self.d_subtitulo_6.setStyleSheet(u"border: none;\n"
"border-radius: none;")
        self.d_subtitulo_6.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.b_icone_titulo_6 = QLabel(self.c_card_direito_2)
        self.b_icone_titulo_6.setObjectName(u"b_icone_titulo_6")
        self.b_icone_titulo_6.setGeometry(QRect(47, 108, 21, 16))
        self.b_icone_titulo_6.setStyleSheet(u"image: url(:/icones/check.svg);\n"
"image: url(:/icones/shield.svg);\n"
"border: none;")
        self.subtitulo_2 = QLabel(self.b_conteudo_central_2)
        self.subtitulo_2.setObjectName(u"subtitulo_2")
        self.subtitulo_2.setGeometry(QRect(0, 0, 1230, 25))
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.subtitulo_2.sizePolicy().hasHeightForWidth())
        self.subtitulo_2.setSizePolicy(sizePolicy5)
        self.subtitulo_2.setMinimumSize(QSize(1135, 25))
        self.subtitulo_2.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: #222;")
        self.subtitulo_2.setAlignment(Qt.AlignCenter)
        self.descricao_texto_2 = QLabel(self.b_conteudo_central_2)
        self.descricao_texto_2.setObjectName(u"descricao_texto_2")
        self.descricao_texto_2.setGeometry(QRect(0, 233, 1130, 175))
        self.descricao_texto_2.setMinimumSize(QSize(1080, 175))
        self.descricao_texto_2.setMaximumSize(QSize(16777215, 280))
        self.descricao_texto_2.setStyleSheet(u"font: 9pt \"Segoe UI\";\n"
"color: black;")
        self.descricao_texto_2.setFrameShadow(QFrame.Plain)
        self.descricao_texto_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label = QLabel(self.b_conteudo_central_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1, 210, 101, 30))
        self.label.setStyleSheet(u"color: #222;\n"
"font: 12pt \"Segoe UI\";")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.a_titulo_2 = QFrame(self.container_2)
        self.a_titulo_2.setObjectName(u"a_titulo_2")
        self.a_titulo_2.setGeometry(QRect(1, 270, 1230, 40))
        self.a_titulo_2.setMinimumSize(QSize(0, 40))
        self.a_titulo_2.setMaximumSize(QSize(16777215, 40))
        self.a_titulo_2.setStyleSheet(u"background-color: none;")
        self.a_titulo_2.setFrameShape(QFrame.NoFrame)
        self.a_titulo_2.setFrameShadow(QFrame.Raised)
        self.titulo_2 = QLabel(self.a_titulo_2)
        self.titulo_2.setObjectName(u"titulo_2")
        self.titulo_2.setGeometry(QRect(1, 1, 1230, 30))
        sizePolicy5.setHeightForWidth(self.titulo_2.sizePolicy().hasHeightForWidth())
        self.titulo_2.setSizePolicy(sizePolicy5)
        self.titulo_2.setMinimumSize(QSize(1135, 30))
        self.titulo_2.setMaximumSize(QSize(16777215, 16777215))
        self.titulo_2.setStyleSheet(u"color: #222;\n"
"font: 63 italic 16pt \"Segoe UI Semibold\";")
        self.titulo_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.a_top_conteudo_2 = QFrame(self.container_2)
        self.a_top_conteudo_2.setObjectName(u"a_top_conteudo_2")
        self.a_top_conteudo_2.setGeometry(QRect(1, 1, 1230, 270))
        sizePolicy5.setHeightForWidth(self.a_top_conteudo_2.sizePolicy().hasHeightForWidth())
        self.a_top_conteudo_2.setSizePolicy(sizePolicy5)
        self.a_top_conteudo_2.setMinimumSize(QSize(1080, 270))
        self.a_top_conteudo_2.setMaximumSize(QSize(1920, 250))
        self.a_top_conteudo_2.setStyleSheet(u"")
        self.a_top_conteudo_2.setFrameShape(QFrame.NoFrame)
        self.a_top_conteudo_2.setFrameShadow(QFrame.Raised)
        self.frame_11 = QFrame(self.a_top_conteudo_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(455, 10, 300, 250))
        self.frame_11.setMinimumSize(QSize(300, 250))
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
        self.frame_22.setGeometry(QRect(215, 40, 215, 190))
        sizePolicy5.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy5)
        self.frame_22.setStyleSheet(u"background-image: url(:/icones/pagina_web-1.png);\n"
"background-color: transparent;\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.frame_23 = QFrame(self.a_top_conteudo_2)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(780, 40, 215, 190))
        sizePolicy5.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy5)
        self.frame_23.setStyleSheet(u"background-image: url(:/icones/pagina_web-2.png);\n"
"background-color: transparent;\n"
"border-radius: 10px;\n"
"border: 1px solid black;")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)

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
        self.a_top_conteudo = QFrame(self.container)
        self.a_top_conteudo.setObjectName(u"a_top_conteudo")
        self.a_top_conteudo.setGeometry(QRect(0, 0, 1231, 270))
        sizePolicy5.setHeightForWidth(self.a_top_conteudo.sizePolicy().hasHeightForWidth())
        self.a_top_conteudo.setSizePolicy(sizePolicy5)
        self.a_top_conteudo.setMinimumSize(QSize(1080, 270))
        self.a_top_conteudo.setMaximumSize(QSize(1920, 270))
        self.a_top_conteudo.setStyleSheet(u"background-color: transparent;")
        self.a_top_conteudo.setFrameShape(QFrame.NoFrame)
        self.a_top_conteudo.setFrameShadow(QFrame.Raised)
        self.frame_12 = QFrame(self.a_top_conteudo)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(455, 10, 300, 250))
        self.frame_12.setMinimumSize(QSize(300, 250))
        self.frame_12.setMaximumSize(QSize(260, 300))
        self.frame_12.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	background-image: url(:/icones/login_web.png);\n"
"	border-radius: 10px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QFrame:clicked{\n"
"	height: 350px;\n"
"}")
        self.frame_24 = QFrame(self.a_top_conteudo)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setGeometry(QRect(215, 40, 215, 190))
        sizePolicy5.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy5)
        self.frame_24.setStyleSheet(u"background-image: url(:/icones/pagina_web-1.png);\n"
"background-color: transparent;\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.frame_25 = QFrame(self.a_top_conteudo)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setGeometry(QRect(780, 40, 215, 190))
        sizePolicy5.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy5)
        self.frame_25.setStyleSheet(u"background-image: url(:/icones/pagina_web-2.png);\n"
"background-color: transparent;\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.b_conteudo_central = QFrame(self.container)
        self.b_conteudo_central.setObjectName(u"b_conteudo_central")
        self.b_conteudo_central.setGeometry(QRect(0, 306, 1231, 441))
        self.b_conteudo_central.setStyleSheet(u"background-color: transparent;")
        self.b_conteudo_central.setFrameShape(QFrame.NoFrame)
        self.b_conteudo_central.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.b_conteudo_central)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.b_conteudo_central)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.subtitulo_3 = QLabel(self.frame)
        self.subtitulo_3.setObjectName(u"subtitulo_3")
        self.subtitulo_3.setGeometry(QRect(0, 0, 1230, 40))
        sizePolicy5.setHeightForWidth(self.subtitulo_3.sizePolicy().hasHeightForWidth())
        self.subtitulo_3.setSizePolicy(sizePolicy5)
        self.subtitulo_3.setMinimumSize(QSize(1135, 25))
        self.subtitulo_3.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: #222;\n"
"background-color: transparent;")
        self.subtitulo_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.a_cards_3 = QWidget(self.frame)
        self.a_cards_3.setObjectName(u"a_cards_3")
        self.a_cards_3.setGeometry(QRect(0, 40, 1230, 162))
        sizePolicy4.setHeightForWidth(self.a_cards_3.sizePolicy().hasHeightForWidth())
        self.a_cards_3.setSizePolicy(sizePolicy4)
        self.a_cards_3.setMinimumSize(QSize(1130, 160))
        self.a_cards_3.setMaximumSize(QSize(16777215, 180))
        self.a_cards_3.setSizeIncrement(QSize(0, 150))
        self.a_cards_3.setStyleSheet(u"background-color: transparent;")
        self.a_card_esquerdo_3 = QFrame(self.a_cards_3)
        self.a_card_esquerdo_3.setObjectName(u"a_card_esquerdo_3")
        self.a_card_esquerdo_3.setGeometry(QRect(275, 0, 175, 160))
        self.a_card_esquerdo_3.setMinimumSize(QSize(150, 160))
        self.a_card_esquerdo_3.setStyleSheet(u"background-color: #a1c1e1;\n"
"border: 1px solid #7aa6d4;\n"
"border-radius: 10px;")
        self.a_card_esquerdo_3.setFrameShape(QFrame.StyledPanel)
        self.a_card_esquerdo_3.setFrameShadow(QFrame.Raised)
        self.a_icone_top_7 = QLabel(self.a_card_esquerdo_3)
        self.a_icone_top_7.setObjectName(u"a_icone_top_7")
        self.a_icone_top_7.setGeometry(QRect(55, 15, 60, 60))
        self.a_icone_top_7.setStyleSheet(u"image: url(:/icones/photo.svg);\n"
"border: none;")
        self.c_titulo_7 = QLabel(self.a_card_esquerdo_3)
        self.c_titulo_7.setObjectName(u"c_titulo_7")
        self.c_titulo_7.setGeometry(QRect(10, 100, 150, 30))
        self.c_titulo_7.setStyleSheet(u"border: none;\n"
"font: 12pt \"Segoe UI\";\n"
"color: #222;\n"
"border-top: 1px solid #7aa6d4;\n"
"border-radius: none;")
        self.c_titulo_7.setAlignment(Qt.AlignCenter)
        self.d_subtitulo_7 = QLabel(self.a_card_esquerdo_3)
        self.d_subtitulo_7.setObjectName(u"d_subtitulo_7")
        self.d_subtitulo_7.setGeometry(QRect(7, 130, 160, 20))
        self.d_subtitulo_7.setStyleSheet(u"border: none;\n"
"border-radius: none;")
        self.d_subtitulo_7.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.b_icone_titulo_7 = QLabel(self.a_card_esquerdo_3)
        self.b_icone_titulo_7.setObjectName(u"b_icone_titulo_7")
        self.b_icone_titulo_7.setGeometry(QRect(30, 108, 21, 16))
        self.b_icone_titulo_7.setStyleSheet(u"image: url(:/icones/check.svg);\n"
"image: url(:/icones/shield.svg);\n"
"border: none;")
        self.b_card_centro_3 = QFrame(self.a_cards_3)
        self.b_card_centro_3.setObjectName(u"b_card_centro_3")
        self.b_card_centro_3.setGeometry(QRect(535, 0, 175, 160))
        self.b_card_centro_3.setMinimumSize(QSize(160, 160))
        self.b_card_centro_3.setStyleSheet(u"background-color: #a1c1e1;\n"
"border: 1px solid #7aa6d4;\n"
"border-radius: 10px;")
        self.b_card_centro_3.setFrameShape(QFrame.StyledPanel)
        self.b_card_centro_3.setFrameShadow(QFrame.Raised)
        self.a_icone_top_8 = QLabel(self.b_card_centro_3)
        self.a_icone_top_8.setObjectName(u"a_icone_top_8")
        self.a_icone_top_8.setGeometry(QRect(55, 15, 60, 60))
        self.a_icone_top_8.setStyleSheet(u"image: url(:/icones/camera.svg);\n"
"border: none;")
        self.c_titulo_8 = QLabel(self.b_card_centro_3)
        self.c_titulo_8.setObjectName(u"c_titulo_8")
        self.c_titulo_8.setGeometry(QRect(10, 100, 150, 30))
        self.c_titulo_8.setStyleSheet(u"border: none;\n"
"font: 12pt \"Segoe UI\";\n"
"color: #222;\n"
"border-top: 1px solid #7aa6d4;\n"
"border-radius: none;")
        self.c_titulo_8.setAlignment(Qt.AlignCenter)
        self.d_subtitulo_8 = QLabel(self.b_card_centro_3)
        self.d_subtitulo_8.setObjectName(u"d_subtitulo_8")
        self.d_subtitulo_8.setGeometry(QRect(7, 130, 160, 20))
        self.d_subtitulo_8.setStyleSheet(u"border: none;\n"
"border-radius: none;")
        self.d_subtitulo_8.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.b_icone_titulo_8 = QLabel(self.b_card_centro_3)
        self.b_icone_titulo_8.setObjectName(u"b_icone_titulo_8")
        self.b_icone_titulo_8.setGeometry(QRect(20, 108, 21, 16))
        self.b_icone_titulo_8.setStyleSheet(u"image: url(:/icones/check.svg);\n"
"image: url(:/icones/shield.svg);\n"
"border: none;")
        self.c_card_direito_3 = QFrame(self.a_cards_3)
        self.c_card_direito_3.setObjectName(u"c_card_direito_3")
        self.c_card_direito_3.setGeometry(QRect(795, 0, 175, 160))
        self.c_card_direito_3.setMinimumSize(QSize(160, 160))
        self.c_card_direito_3.setStyleSheet(u"background-color: #a1c1e1;\n"
"border: 1px solid #7aa6d4;\n"
"border-radius: 10px;")
        self.c_card_direito_3.setFrameShape(QFrame.StyledPanel)
        self.c_card_direito_3.setFrameShadow(QFrame.Raised)
        self.a_icone_top_9 = QLabel(self.c_card_direito_3)
        self.a_icone_top_9.setObjectName(u"a_icone_top_9")
        self.a_icone_top_9.setGeometry(QRect(55, 15, 60, 60))
        self.a_icone_top_9.setStyleSheet(u"image: url(:/icones/globo.svg);\n"
"border: none;")
        self.c_titulo_9 = QLabel(self.c_card_direito_3)
        self.c_titulo_9.setObjectName(u"c_titulo_9")
        self.c_titulo_9.setGeometry(QRect(10, 100, 150, 30))
        self.c_titulo_9.setStyleSheet(u"border: none;\n"
"font: 12pt \"Segoe UI\";\n"
"color: #222;\n"
"border-top: 1px solid #7aa6d4;\n"
"border-radius: none;")
        self.c_titulo_9.setAlignment(Qt.AlignCenter)
        self.d_subtitulo_9 = QLabel(self.c_card_direito_3)
        self.d_subtitulo_9.setObjectName(u"d_subtitulo_9")
        self.d_subtitulo_9.setGeometry(QRect(7, 130, 160, 20))
        self.d_subtitulo_9.setStyleSheet(u"border: none;\n"
"border-radius: none;")
        self.d_subtitulo_9.setAlignment(Qt.AlignCenter)
        self.b_icone_titulo_9 = QLabel(self.c_card_direito_3)
        self.b_icone_titulo_9.setObjectName(u"b_icone_titulo_9")
        self.b_icone_titulo_9.setGeometry(QRect(43, 108, 21, 16))
        self.b_icone_titulo_9.setStyleSheet(u"image: url(:/icones/check.svg);\n"
"image: url(:/icones/shield.svg);\n"
"border: none;")
        self.descricao_texto_3 = QLabel(self.frame)
        self.descricao_texto_3.setObjectName(u"descricao_texto_3")
        self.descricao_texto_3.setGeometry(QRect(1, 233, 1130, 175))
        self.descricao_texto_3.setMinimumSize(QSize(1080, 175))
        self.descricao_texto_3.setMaximumSize(QSize(16777215, 280))
        self.descricao_texto_3.setStyleSheet(u"font: 9pt \"Segoe UI\";\n"
"color: black;\n"
"background-color: transparent;")
        self.descricao_texto_3.setFrameShadow(QFrame.Plain)
        self.descricao_texto_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(2, 210, 101, 30))
        self.label_3.setStyleSheet(u"color: #222;\n"
"font: 12pt \"Segoe UI\";")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_8.addWidget(self.frame)

        self.a_titulo = QFrame(self.container)
        self.a_titulo.setObjectName(u"a_titulo")
        self.a_titulo.setGeometry(QRect(1, 270, 1230, 40))
        self.a_titulo.setStyleSheet(u"background-color: transparent;")
        self.a_titulo.setFrameShape(QFrame.NoFrame)
        self.a_titulo.setFrameShadow(QFrame.Raised)
        self.titulo = QLabel(self.a_titulo)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(1, 1, 1230, 30))
        sizePolicy5.setHeightForWidth(self.titulo.sizePolicy().hasHeightForWidth())
        self.titulo.setSizePolicy(sizePolicy5)
        self.titulo.setMinimumSize(QSize(1230, 30))
        self.titulo.setMaximumSize(QSize(1230, 30))
        self.titulo.setStyleSheet(u"font: 63 italic 16pt \"Segoe UI Semibold\";\n"
"color: #222;")
        self.titulo.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_7.addWidget(self.container)


        self.verticalLayout_6.addWidget(self.conteudo)

        self.barra_widgets.addTab(self.b_ProjetodeSoftware, "")

        self.verticalLayout.addWidget(self.barra_widgets)


        self.horizontalLayout.addWidget(self.b_conteudo)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.barra_widgets.setCurrentIndex(1)


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
        self.a_icone_top_4.setText("")
        self.c_titulo_4.setText(QCoreApplication.translate("MainWindow", u"Registros", None))
        self.d_subtitulo_4.setText(QCoreApplication.translate("MainWindow", u" Pequenas Lojas e Autonomos", None))
        self.b_icone_titulo_4.setText("")
        self.a_icone_top_5.setText("")
        self.c_titulo_5.setText(QCoreApplication.translate("MainWindow", u"    Fotos Incr\u00edveis", None))
        self.d_subtitulo_5.setText(QCoreApplication.translate("MainWindow", u"   Pequenas Lojas e Autonomos", None))
        self.b_icone_titulo_5.setText("")
        self.a_icone_top_6.setText("")
        self.c_titulo_6.setText(QCoreApplication.translate("MainWindow", u" Maps", None))
        self.d_subtitulo_6.setText(QCoreApplication.translate("MainWindow", u"Pequenas Lojas e Autonomos", None))
        self.b_icone_titulo_6.setText("")
        self.subtitulo_2.setText(QCoreApplication.translate("MainWindow", u"CONHECENDO AS MARAVILHAS DO MUNDO!", None))
        self.descricao_texto_2.setText(QCoreApplication.translate("MainWindow", u"     O LOGMARKET \u00e9 uma solu\u00e7\u00e3o completa para gest\u00e3o comercial, desenvolvida especialmente para empresas que desejam otimizar o processo de cadastro, consulta e venda de produtos.\n"
"Com uma interface intuitiva, o sistema permite que voc\u00ea registre novos itens rapidamente, mantenha o controle detalhado do seu cat\u00e1logo e realize vendas de maneira pr\u00e1tica e segura.\n"
"Principais recursos:\n"
"     -Cadastro de produtos com informa\u00e7\u00f5es detalhadas, imagens e categorias personalizadas.\n"
"     -Consulta avan\u00e7ada por filtros, c\u00f3digos ou descri\u00e7\u00f5es, facilitando a localiza\u00e7\u00e3o de produtos no estoque.\n"
"     -Processo de vendas integrado, com emiss\u00e3o de comprovantes e relat\u00f3rios de transa\u00e7\u00f5es.\n"
"     -Controle de estoque atualizado em tempo real.\n"
"Voltado para com\u00e9rcios de diferentes portes, o LOGMARKET proporciona mai"
                        "s agilidade no atendimento, redu\u00e7\u00e3o de erros operacionais e maior controle sobre todas as opera\u00e7\u00f5es comerciais.", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"    DESCRI\u00c7\u00c3O", None))
        self.titulo_2.setText(QCoreApplication.translate("MainWindow", u"PIXEL PHOTO", None))
        self.barra_widgets.setTabText(self.barra_widgets.indexOf(self.a_ProjetoWebSite), QCoreApplication.translate("MainWindow", u"Projeto Web Site", None))
        self.subtitulo_3.setText(QCoreApplication.translate("MainWindow", u"CONHECENDO AS MARAVILHAS DO MUNDO!", None))
        self.a_icone_top_7.setText("")
        self.c_titulo_7.setText(QCoreApplication.translate("MainWindow", u"Registros", None))
        self.d_subtitulo_7.setText(QCoreApplication.translate("MainWindow", u" Pequenas Lojas e Autonomos", None))
        self.b_icone_titulo_7.setText("")
        self.a_icone_top_8.setText("")
        self.c_titulo_8.setText(QCoreApplication.translate("MainWindow", u"    Fotos Incr\u00edveis", None))
        self.d_subtitulo_8.setText(QCoreApplication.translate("MainWindow", u"Pequenas Lojas e Autonomos", None))
        self.b_icone_titulo_8.setText("")
        self.a_icone_top_9.setText("")
        self.c_titulo_9.setText(QCoreApplication.translate("MainWindow", u"Maps", None))
        self.d_subtitulo_9.setText(QCoreApplication.translate("MainWindow", u"Pequenas Lojas e Autonomos", None))
        self.b_icone_titulo_9.setText("")
        self.descricao_texto_3.setText(QCoreApplication.translate("MainWindow", u"     O LOGMARKET \u00e9 uma solu\u00e7\u00e3o completa para gest\u00e3o comercial, desenvolvida especialmente para empresas que desejam otimizar o processo de cadastro, consulta e venda de produtos.\n"
"Com uma interface intuitiva, o sistema permite que voc\u00ea registre novos itens rapidamente, mantenha o controle detalhado do seu cat\u00e1logo e realize vendas de maneira pr\u00e1tica e segura.\n"
"Principais recursos:\n"
"     -Cadastro de produtos com informa\u00e7\u00f5es detalhadas, imagens e categorias personalizadas.\n"
"     -Consulta avan\u00e7ada por filtros, c\u00f3digos ou descri\u00e7\u00f5es, facilitando a localiza\u00e7\u00e3o de produtos no estoque.\n"
"     -Processo de vendas integrado, com emiss\u00e3o de comprovantes e relat\u00f3rios de transa\u00e7\u00f5es.\n"
"     -Controle de estoque atualizado em tempo real.\n"
"Voltado para com\u00e9rcios de diferentes portes, o LOGMARKET proporciona mais agilidade no atendimento, redu\u00e7\u00e3o de erros operacionais e maior controle sobre todas "
                        "as opera\u00e7\u00f5es comerciais.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"    DESCRI\u00c7\u00c3O", None))
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"LOGMARKET", None))
        self.barra_widgets.setTabText(self.barra_widgets.indexOf(self.b_ProjetodeSoftware), QCoreApplication.translate("MainWindow", u"Projeto de Software", None))
    # retranslateUi

