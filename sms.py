import hashlib
import random
import requests
import time
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# 短信发送 API 接口地址
SMS_API_URL = "https://106.ihuyi.com/webservice/sms.php?method=Submit"
# 互亿短信平台的 API_ID 和 API_KEY
SMS_API_ID = "C96183775"
SMS_API_KEY = "f3fc21ba0a7d7d5de2959f0eda948128"
def sendemail():
    # 发件人邮箱账号
    from_addr = 'freeconpon123@outlook.com'
    # 发件人邮箱密码或授权码
    password = 'cg56fft66tg66r'
    # 收件人邮箱账号
    to_addr = 'bvyybvfhnj@outlook.com'
    # 邮件主题
    subject = 'Test Email'
    # 邮件正文
    body = 'This is a test email.'
    # 创建一个带附件的邮件对象
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    # 添加邮件正文
    msg.attach(MIMEText(body, 'plain'))
    '''
    # 添加附件
    with open('test_file.txt', 'rb') as f:
        attachment = MIMEApplication(f.read(), _subtype='txt')
        attachment.add_header('Content-Disposition', 'attachment', filename='test_file.txt')
        msg.attach(attachment)
    '''
    # 发送邮件
    smtp_server = 'smtp.office365.com'
    smtp_port = 587
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(from_addr, password)




if __name__ == "__main__":
    sendemail()
    
    url = 'https://smstome.com/country/france'

    # 获取初始页面内容
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    element = soup.find_all('small')[1]
    qtext = element.text

    while True:
        # 等待10秒钟
        time.sleep(20)

        # 获取页面内容
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        element1 = soup.find_all('small')[1]
        new_text = element1.text

        # 如果文本发生变化，打印新文本
        if new_text != qtext:
            qtext = new_text
            print('The text has changed to:', qtext)
            sendemail()
