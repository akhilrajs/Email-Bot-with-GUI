# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'email_bot.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
import smtplib
import ssl
import time
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from gtts import gTTS
from playsound import playsound

if not os.path.exists('temp_data'):
        os.makedirs('temp_data')  
folder = 'temp_data'
directory = os.getcwd() 
SAVE_PATH = os.path.join(directory, folder)


global sender_mail_id_
class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(1791, 849)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main.sizePolicy().hasHeightForWidth())
        main.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(main)
        self.label.setGeometry(QtCore.QRect(10, 819, 181, 31))
        self.label.setObjectName("label")
        self.sender_mail_id_label = QtWidgets.QLabel(main)
        self.sender_mail_id_label.setGeometry(QtCore.QRect(20, 70, 101, 21))
        self.sender_mail_id_label.setObjectName("sender_mail_id_label")
        self.sender_mail_id = QtWidgets.QLineEdit(main)
        self.sender_mail_id.setGeometry(QtCore.QRect(120, 70, 231, 21))
        self.sender_mail_id.setObjectName("sender_mail_id")
        self.sender_mail_password_label = QtWidgets.QLabel(main)
        self.sender_mail_password_label.setGeometry(QtCore.QRect(380, 70, 141, 21))
        self.sender_mail_password_label.setObjectName("sender_mail_password_label")
        self.sender_mail_password = QtWidgets.QLineEdit(main)
        self.sender_mail_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sender_mail_password.setGeometry(QtCore.QRect(520, 70, 251, 22))
        self.sender_mail_password.setObjectName("sender_mail_password")
        self.line = QtWidgets.QFrame(main)
        self.line.setGeometry(QtCore.QRect(-3, 100, 1211, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(main)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 121, 21))
        self.label_2.setStyleSheet("font: 75 14pt \"Coves\";")
        self.label_2.setObjectName("label_2")
        self.subject_label = QtWidgets.QLabel(main)
        self.subject_label.setGeometry(QtCore.QRect(120, 180, 71, 16))
        self.subject_label.setStyleSheet("font: 75 8pt \"Nirmala UI\";")
        self.subject_label.setObjectName("subject_label")
        self.body_label = QtWidgets.QLabel(main)
        self.body_label.setGeometry(QtCore.QRect(130, 250, 55, 16))
        self.body_label.setObjectName("body_label")
        self.body = QtWidgets.QTextEdit(main)
        self.body.setGeometry(QtCore.QRect(180, 250, 601, 181))
        self.body.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.body.setObjectName("body")
        self.label_3 = QtWidgets.QLabel(main)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 171, 21))
        self.label_3.setStyleSheet("font: 75 14pt \"Coves\";")
        self.label_3.setObjectName("label_3")
        self.note_label = QtWidgets.QLabel(main)
        self.note_label.setGeometry(QtCore.QRect(180, 20, 521, 21))
        self.note_label.setObjectName("note_label")
        self.attachment_location_label = QtWidgets.QLabel(main)
        self.attachment_location_label.setGeometry(QtCore.QRect(40, 450, 131, 21))
        self.attachment_location_label.setObjectName("attachment_location_label")
        
        self.attachment_name_label = QtWidgets.QLabel(main)
        self.attachment_name_label.setGeometry(QtCore.QRect(55, 480, 131, 21))
        self.attachment_name_label.setObjectName("attachment_name_label")
        
        self.a_label = QtWidgets.QLabel(main)
        self.a_label.setGeometry(QtCore.QRect(55, 510, 281, 23))
        self.a_label.setObjectName("a_label")
        
        self.attachment_address = QtWidgets.QTextEdit(main)
        self.attachment_address.setGeometry(QtCore.QRect(180, 450, 601, 27))
        self.attachment_address.setObjectName("attachment_address")
        
        self.attachment_name = QtWidgets.QTextEdit(main)
        self.attachment_name.setGeometry(QtCore.QRect(180, 480, 242, 27))
        self.attachment_name.setObjectName("attachment_name")
        self.subject = QtWidgets.QTextEdit(main)
        self.subject.setGeometry(QtCore.QRect(180, 180, 601, 51))
        self.subject.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.subject.setObjectName("subject")
        self.line_2 = QtWidgets.QFrame(main)
        self.line_2.setGeometry(QtCore.QRect(0, 530, 1791, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.send_emails = QtWidgets.QPushButton(main)
        self.send_emails.setGeometry(QtCore.QRect(680, 500, 101, 28))
        self.send_emails.setObjectName("send_emails")
        self.send_emails.clicked.connect(self.pass_to_send_emails)
        self.show_preveiw = QtWidgets.QPushButton(main)
        self.show_preveiw.setGeometry(QtCore.QRect(560, 500, 111, 28))
        self.show_preveiw.setObjectName("show preveiw")
        self.show_preveiw.clicked.connect(self.pass_to_show_preveiw)
        
        self.load_attachment = QtWidgets.QPushButton(main)
        self.load_attachment.setGeometry(QtCore.QRect(425, 500, 121, 28))
        self.load_attachment.setObjectName("load_attchment")
        self.load_attachment.clicked.connect(self.pass_to_load_attachment)
        self.email_preveiw = QtWidgets.QTextBrowser(main)
        self.email_preveiw.setGeometry(QtCore.QRect(1220, 40, 561, 481))
        self.email_preveiw.setObjectName("email_preveiw")
        self.email_preveiw.ensureCursorVisible()
        self.preveiw_label = QtWidgets.QLabel(main)
        self.preveiw_label.setGeometry(QtCore.QRect(1220, 20, 71, 16))
        self.preveiw_label.setObjectName("preveiw_label")
        self.check_connection = QtWidgets.QPushButton(main)
        self.check_connection.setGeometry(QtCore.QRect(810, 70, 131, 28))
        self.check_connection.setObjectName("check_connection")
        self.check_connection.clicked.connect(self.pass_to_check_connection)
        self.line_3 = QtWidgets.QFrame(main)
        self.line_3.setGeometry(QtCore.QRect(800, 110, 20, 741))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_4 = QtWidgets.QLabel(main)
        self.label_4.setGeometry(QtCore.QRect(830, 120, 181, 21))
        self.label_4.setStyleSheet("font: 75 14pt \"Coves\";")
        self.label_4.setObjectName("label_4")
        self.line_4 = QtWidgets.QFrame(main)
        self.line_4.setGeometry(QtCore.QRect(1200, 0, 20, 851))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.load_details = QtWidgets.QPushButton(main)
        self.load_details.setGeometry(QtCore.QRect(1040, 120, 131, 28))
        self.load_details.setObjectName("Load details")
        self.load_details.clicked.connect(self.pass_to_load_details)
        self.mailid_list = QtWidgets.QTextEdit(main)
        self.mailid_list.setGeometry(QtCore.QRect(830, 180, 171, 341))
        self.mailid_list.setObjectName("mailid_list")
        self.names_list = QtWidgets.QTextEdit(main)
        self.names_list.setGeometry(QtCore.QRect(1020, 180, 171, 341))
        self.names_list.setObjectName("names_list")
        self.enter_mail_id_label = QtWidgets.QLabel(main)
        self.enter_mail_id_label.setGeometry(QtCore.QRect(830, 150, 161, 21))
        self.enter_mail_id_label.setObjectName("enter_mail_id_label")
        self.enter_list_names_label = QtWidgets.QLabel(main)
        self.enter_list_names_label.setGeometry(QtCore.QRect(1020, 150, 161, 21))
        self.enter_list_names_label.setObjectName("enter_list_names_label")
        self.label_5 = QtWidgets.QLabel(main)
        self.label_5.setGeometry(QtCore.QRect(10, 540, 121, 41))
        self.label_5.setStyleSheet("font: 75 14pt \"Coves\";")
        self.label_5.setObjectName("label_5")
        self.textBrowser = QtWidgets.QTextBrowser(main)
        self.textBrowser.setGeometry(QtCore.QRect(10, 580, 771, 241))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.ensureCursorVisible()
        self.label_6 = QtWidgets.QLabel(main)
        self.label_6.setGeometry(QtCore.QRect(830, 540, 181, 31))
        self.label_6.setStyleSheet("font: 75 14pt \"Coves\";")
        self.label_6.setObjectName("label_6")
        self.total_mails_send_label = QtWidgets.QLabel(main)
        self.total_mails_send_label.setGeometry(QtCore.QRect(880, 590, 131, 16))
        self.total_mails_send_label.setObjectName("total_mails_send_label")
        self.send_status_label = QtWidgets.QLabel(main)
        self.send_status_label.setGeometry(QtCore.QRect(880, 620, 131, 16))
        self.send_status_label.setObjectName("send_status_label")
        self.senders_address_label = QtWidgets.QLabel(main)
        self.senders_address_label.setGeometry(QtCore.QRect(880, 650, 131, 16))
        self.senders_address_label.setObjectName("senders_address_label")
        self.attachment_label = QtWidgets.QLabel(main)
        self.attachment_label.setGeometry(QtCore.QRect(880, 680, 121, 16))
        self.attachment_label.setObjectName("attachment_label")
        self.total_mails_no_label = QtWidgets.QLabel(main)
        self.total_mails_no_label.setGeometry(QtCore.QRect(1010, 590, 91, 16))
        self.total_mails_no_label.setObjectName("total_mails_no_label")
        self.status_label = QtWidgets.QLabel(main)
        self.status_label.setGeometry(QtCore.QRect(1010, 620, 200, 16))
        self.status_label.setObjectName("status_label")
        self.senders_address_here_label = QtWidgets.QLabel(main)
        self.senders_address_here_label.setGeometry(QtCore.QRect(1010, 650, 181, 16))
        self.senders_address_here_label.setObjectName("senders_address_here_label")
        self.attachment_status_label = QtWidgets.QLabel(main)
        self.attachment_status_label.setGeometry(QtCore.QRect(1010, 680, 55, 16))
        self.attachment_status_label.setObjectName("attachment_status_label")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(main)
        self.webEngineView.setGeometry(QtCore.QRect(1220, 570, 561, 271))
        self.webEngineView.setUrl(QtCore.QUrl("https://music.youtube.com/"))
        self.webEngineView.setObjectName("webEngineView")
        self.label_7 = QtWidgets.QLabel(main)
        self.label_7.setGeometry(QtCore.QRect(1230, 535, 271, 31))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        global _translate
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Email bot"))
        self.label.setText(_translate("main", "created by akhil raj s "))
        self.sender_mail_id_label.setText(_translate("main", "Sender mail ID :"))
        self.sender_mail_id.setText(_translate("main", "Put_Mail_ID_Here_@gmail.com"))
        self.sender_mail_password_label.setText(_translate("main", "Sender mail Password :"))
        self.sender_mail_password.setText(_translate("main", ""))
        self.label_2.setText(_translate("main", "Email Details"))
        self.subject_label.setText(_translate("main", "Subject : "))
        self.body_label.setText(_translate("main", "Body :"))
        self.body.setHtml(_translate("main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">type the body of the email here.</p></body></html>"))
        self.label_3.setText(_translate("main", "Sender\'s Details"))
        self.note_label.setText(_translate("main", "Note : switch on third party access in Google Gmail account Security Settings."))
        self.attachment_location_label.setText(_translate("main", "Attachment Location : "))        
        self.attachment_name_label.setText(_translate("main", "Attachment Name : "))
        self.subject.setHtml(_translate("main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">type the SUBJECT of the email here it will be automatically converted to capital letters.</p></body></html>"))
        self.send_emails.setText(_translate("main", "Send Emails"))
        self.show_preveiw.setText(_translate("main", "Show Preveiw"))
        self.load_attachment.setText(_translate("main", "Load Attachment"))        
        self.load_details.setText(_translate("main", "Load details"))
        self.preveiw_label.setText(_translate("main", "preveiw "))
        self.check_connection.setText(_translate("main", "Check Connection"))
        self.label_4.setText(_translate("main", "Receipients\' Details"))
        self.enter_mail_id_label.setText(_translate("main", "enter the list of mail ID here"))
        self.enter_list_names_label.setText(_translate("main", "enter the list of names here"))
        self.label_5.setText(_translate("main", "Activity log"))
        self.label_6.setText(_translate("main", "Report"))
        self.total_mails_send_label.setText(_translate("main", "Total emails send :"))
        self.send_status_label.setText(_translate("main", "Status of process  :"))
        self.senders_address_label.setText(_translate("main", "Sender Address  :"))
        self.attachment_label.setText(_translate("main", "Attachment        :"))
        self.total_mails_no_label.setText(_translate("main", "0"))
        self.status_label.setText(_translate("main", "No emails send yet"))
        self.senders_address_here_label.setText(_translate("main", "nil@gmail.com"))
        self.attachment_status_label.setText(_translate("main", "nil"))
        self.label_7.setText(_translate("main", "hear some music while i send the mails"))
        self.attachment_name.setText(_translate("main", "For example : image.jpg"))
        self.a_label.setText(_translate("main","GIVE THE EXTENSION ALSO (.png, .pdf ...)"))
        
    def pass_to_check_connection(self):
        cc = threading.Thread(target = lambda:check_connection(self))
        cs = threading.Thread(target = lambda:construct_sample_mail(self))
        cc.start()
        cs.start()
        
    def pass_to_show_preveiw(self):
        sp = threading.Thread(target = lambda:show_preveiw(self))
        sp.start()
        
    def pass_to_load_details(self):
        lmi = threading.Thread(target = lambda:load_mail_ids(self))
        ln = threading.Thread(target = lambda:load_names(self))
        ln.start()
        lmi.start()
        
    def pass_to_load_attachment(self):
        la = threading.Thread(target = lambda:load_attachment(self))
        la.start()
        
    def pass_to_send_emails(self):
        se = threading.Thread(target = lambda:check(self))
        se.start()
        
        


def check(self):
    sender_email_id_ = str(self.sender_mail_id.text())
    self.textBrowser.append("# sender Email ID " + sender_email_id_ + " loaded")
    self.textBrowser.ensureCursorVisible()
    sender_email_password_ = (self.sender_mail_password.text())
    self.textBrowser.append("# checking connection ...")
    self.textBrowser.ensureCursorVisible()
    print("\n\nCHECKING CONNECTION...\n")
    connected = connection_checking(self)
    if connected:
        print("\nCONNECTED\n")
        self.textBrowser.append("# Connected to account " + sender_email_id_)
        self.textBrowser.ensureCursorVisible()
        global names_list_
        global body_
        names_list_ = (self.names_list.toPlainText().splitlines())
        self.textBrowser.append("# Name list loaded")
        self.textBrowser.ensureCursorVisible()
        subject_ = self.subject.toPlainText()
        self.textBrowser.append("# Subject loaded")
        self.textBrowser.ensureCursorVisible()
        subject_ = subject_.upper()
        body_ = self.body.toPlainText()
        self.textBrowser.append("# Body loaded loaded")
        self.textBrowser.ensureCursorVisible()
        global mailid_list_
        mailid_list_ = (self.mailid_list.toPlainText().splitlines())
        self.textBrowser.append("# Email list loaded")
        self.textBrowser.ensureCursorVisible()
        global attachment
        attachment = self.attachment_address.toPlainText()
        attachment = attachment[8:]
        self.textBrowser.append("# attachment file : " + attachment)
        self.textBrowser.ensureCursorVisible()
        if not os.path.exists(attachment):
            self.textBrowser.append("# attachment file not found")
            self.textBrowser.append("# sending email ( No Attachment included )")
            self.textBrowser.ensureCursorVisible()
            sewa = threading.Thread(target = lambda:send_emails_without_attachments(self))
            sewa.start()
        else :
            self.textBrowser.append("# attachment file loaded")
            self.textBrowser.append("# sending email (attachment included )")
            self.textBrowser.ensureCursorVisible()
            sena = threading.Thread(target = lambda:send_emails_with_attachments(self))
            sena.start()
      

    else:
        print("oops!  your login credentials are incorrect")
        self.textBrowser.append("# oops!  your login credentials are incorrect ")
        self.textBrowser.ensureCursorVisible()
    


  
def load_attachment(self):
    global attachment
    attachment = self.attachment_address.toPlainText()
    attachment = attachment[8:]
    self.textBrowser.append("# attachment file : " + attachment)
    self.textBrowser.ensureCursorVisible()
    if not os.path.exists(attachment):
          self.textBrowser.append("# attachment file not found")
          self.textBrowser.ensureCursorVisible()
    else :
        self.textBrowser.append("# attachment file loaded")
        self.textBrowser.ensureCursorVisible()
    

def load_mail_ids(self):
    global mailid_list_
    mailid_list_ = (self.mailid_list.toPlainText().splitlines())
    self.textBrowser.append("# List of Emial IDs has been loaded")
    self.textBrowser.ensureCursorVisible()


def load_names(self):
    global names_list_
    global body_
    names_list_ = (self.names_list.toPlainText().splitlines())
    self.textBrowser.append("# List of Names has been loaded")
    self.textBrowser.ensureCursorVisible()
    self.email_preveiw.append('''
                
this is just the preview using the first name in the list 
 ______________________________________________________________________________                             
''')
    sample_email = ''''''
    intro = "Hello " + names_list_[0]
    subject_ = self.subject.toPlainText()
    subject_ = subject_.upper()
    body_ = self.body.toPlainText()
    sample_email = intro + '''
    
''' + subject_ + '''
    
''' + body_ 
    self.email_preveiw.append(sample_email)
    self.email_preveiw.ensureCursorVisible()

    
def show_preveiw(self):
    self.email_preveiw.append('''
 ______________________________________________________________________________                             
''')
    sample_email = ''''''
    intro = "Hello %NAME WILL GO HERE% "
    subject_ = self.subject.toPlainText()
    subject_ = subject_.upper()
    body_ = self.body.toPlainText()
    sample_email = intro + '''
    
''' + subject_ + '''
    
''' + body_ 
    self.email_preveiw.append(sample_email)
    self.email_preveiw.ensureCursorVisible()


def construct_sample_mail(self):
    self.email_preveiw.append('''
 ______________________________________________________________________________                             
''')
    sample_email = ''''''
    intro = "Hello %NAME WILL GO HERE% "
    subject_ = self.subject.toPlainText()
    subject_ = subject_.upper()
    body_ = self.body.toPlainText()
    sample_email = intro + '''
    
''' + subject_ + '''
    
''' + body_ 
    self.email_preveiw.append(sample_email)
    self.email_preveiw.ensureCursorVisible()
    
def check_connection(self):
    sender_email_id_ = str(self.sender_mail_id.text())
    self.textBrowser.append("# sender Email ID " + sender_email_id_ + " loaded")
    self.textBrowser.ensureCursorVisible()
    sender_email_password_ = (self.sender_mail_password.text())
    self.textBrowser.append("# checking connection ...")
    self.textBrowser.ensureCursorVisible()
    print("\n\nCHECKING CONNECTION...\n")
    connected = connection_checking(self)
    if connected:
        print("\nCONNECTED\n")
        self.textBrowser.append("# Connected to account " + sender_email_id_)
        self.textBrowser.ensureCursorVisible()

    else:
        print("oops!  your login credentials are incorrect")
        self.textBrowser.append("# oops!  your login credentials are incorrect ")
        self.textBrowser.ensureCursorVisible()
    
def connection_checking(self):
    flag = True
    global sender
    global auth_code
    sender = self.sender_mail_id.text()
    auth_code = self.sender_mail_password.text()
    smtp_server = "smtp.gmail.com"
    port = 465  # for SSL
    con = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=con) as server:
            server.login(sender, auth_code)

    except Exception as e:
        flag = False
        error = str(e)
        if ("Username and Password not accepted" in error):
            print("\n   Incorrect Login Credentials :-( \n")
            self.textBrowser.append("# Incorrect Login Credentials ")
            self.textBrowser.ensureCursorVisible()
        else:
            print("\nSOME UNKNOWN ERROR OCCURED :-( SEE DETAILS BELOW \n\n", e)
            self.textBrowser.append('# some unknown error occured see details below \n \n ' + e)
            self.textBrowser.ensureCursorVisible()

    finally:
        return flag

def send_emails_without_attachments(self):
    no = 1
    self.senders_address_here_label.setText(_translate("main", sender))
    self.attachment_status_label.setText(_translate("main", "No"))
    self.status_label.setText(_translate("main", "Sending Emails"))
    self.textBrowser.append("# sending emails without attachments")
    self.textBrowser.append("# please wait")
    self.textBrowser.ensureCursorVisible
    i = 0 
    for email_id in mailid_list_ :
         mail_content = '''Hello ''' + names_list_[i].upper() + '''
''' + body_
         #The mail addresses and password
         sender_address = sender
         sender_pass = auth_code
         receiver_address = email_id 
         #Setup the MIME
         message = MIMEMultipart()
         message['From'] = sender_address
         message['To'] = receiver_address
         message['Subject'] = 'ENTER THE SUBJECT HERE .'
         #The subject line
         #The body and the attachments for the mail
         message.attach(MIMEText(mail_content, 'plain'))
         #Create SMTP session for sending the mail
         session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
         session.starttls() #enable security
         session.login(sender_address, sender_pass) #login with mail_id and password
         text = message.as_string()
         session.sendmail(sender_address, receiver_address, text)
         session.quit()
         i += 1
         self.textBrowser.append('# email has been send to ' + email_id)
         self.textBrowser.ensureCursorVisible()
         self.total_mails_no_label.setText(_translate("main", str(no)))
         no += 1
    self.textBrowser.append("# ")
    self.status_label.setText(_translate("main", "Sending Complete"))
    self.textBrowser.append("# Email sending complete ")
    self.textBrowser.append("# Total number of emails send : " + str(no))
    self.textBrowser.ensureCursorVisible
    language = 'en'
    audio_file = gTTS(text="Sending mails complete", lang=language, slow=False)
    audio_file_name =  "temp.mp3"
    audio_file.save(audio_file_name)
    playsound(audio_file_name)
    os.remove(audio_file_name)

        
def send_emails_with_attachments(self):
    no = 1
    attachment_name_ = self.attachment_name.toPlainText()
    self.senders_address_here_label.setText(_translate("main", sender))
    self.attachment_status_label.setText(_translate("main", "Yes"))
    self.status_label.setText(_translate("main", "Sending Emails"))
    self.textBrowser.append("# sending emails with attachments")
    self.textBrowser.append("# please wait")
    self.textBrowser.ensureCursorVisible
    i = 0 
    for email_id in mailid_list_ :
         mail_content = '''Hello ''' + names_list_[i].upper() + '''
''' + body_
         #The mail addresses and password
         sender_address = sender
         sender_pass = auth_code
         receiver_address = email_id 
         #Setup the MIME
         message = MIMEMultipart()
         message['From'] = sender_address
         message['To'] = receiver_address
         message['Subject'] = 'ENTER THE SUBJECT HERE .'
         #The subject line
         #The body and the attachments for the mail
         message.attach(MIMEText(mail_content, 'plain'))
         attach_file_name = attachment 
         attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
         payload = MIMEBase('application', 'octate-stream', name = attachment_name_)
         payload.set_payload((attach_file).read())
         encoders.encode_base64(payload) #encode the attachment
         #add payload header with filename
         payload.add_header('Content-Decomposition', 'attachment', filename = attachment_name_)
         message.attach(payload)
         #Create SMTP session for sending the mail
         session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
         session.starttls() #enable security
         session.login(sender_address, sender_pass) #login with mail_id and password
         text = message.as_string()
         session.sendmail(sender_address, receiver_address, text)
         session.quit()
         i += 1
         attach_file.close()
         self.textBrowser.append('# email has been send to ' + email_id)
         self.textBrowser.ensureCursorVisible()
         self.total_mails_no_label.setText(_translate("main", str(no)))
         no += 1
    self.textBrowser.append("# ")
    self.status_label.setText(_translate("main", "Sending Complete"))
    self.textBrowser.append("# Email sending complete ")
    self.textBrowser.ensureCursorVisible
    self.textBrowser.append("# Total number of emails send : " + str(no))
    self.textBrowser.ensureCursorVisible
    language = 'en'
    audio_file = gTTS(text="Sending mails complete", lang=language, slow=False)
    audio_file_name =  "temp.mp3"
    audio_file.save(audio_file_name)
    playsound(audio_file_name)
    os.remove(audio_file_name)
    
from PyQt5 import QtWebEngineWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QWidget()
    ui = Ui_main()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())

