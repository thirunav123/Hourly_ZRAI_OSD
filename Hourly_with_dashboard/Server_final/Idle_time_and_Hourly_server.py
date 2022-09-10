import os,sys,socket,queue,datetime,time,threading,requests,json,schedule,copy,psutil
from openpyxl import Workbook,load_workbook
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
exec(open("trans.py").read())