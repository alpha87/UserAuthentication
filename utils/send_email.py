'''
Desc:
    发送电子邮件
'''
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

EMAIL_HOST = os.environ["EMAIL_HOST"]

EMAIL_PORT = os.environ["EMAIL_PORT"]

EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]

EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]


def send_email(receiver, link, config="confirm"):

    mail_msg = """<p>仅需最后一步来激活您的帐号。点击下面的链接来验证您的邮箱地址：</p><a href="{link}">{link}</a>""".format(
        link=link)
    mail_title = '验证您的[ 用户认证系统 ]帐号注册邮箱'

    if config == "forgot":
        mail_msg = """<p>点击下面的链接来重设您的密码：</p><a href="{link}">{link}</a>""".format(
        link=link)
        mail_title = '验证您的[ 用户认证系统 ]帐号重设密码邮箱'

    message = MIMEText(mail_msg, "html", 'utf-8')
    message['Subject'] = mail_title
    message['From'] = 'jianxun<{}>'.format(EMAIL_HOST_USER)
    message['To'] = receiver
    receivers = [receiver]

    smtp = smtplib.SMTP()
    smtp.connect(host=EMAIL_HOST, port=EMAIL_PORT)
    smtp.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    smtp.sendmail(EMAIL_HOST_USER, receivers, message.as_string())
    smtp.quit()