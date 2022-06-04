from importlib.metadata import requires
import os,socket,queue,datetime,time,threading,requests,json,schedule
from openpyxl import Workbook,load_workbook
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
exec(open("server.txt").read())
