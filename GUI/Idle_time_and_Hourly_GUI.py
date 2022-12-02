import os,sys,time,json,datetime,threading,psutil
import matplotlib.pyplot as plt
from PyQt5.QtCore import QTimer
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.QtGui import  QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
exec(open("main.py").read())