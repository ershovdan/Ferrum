import tkinter
from tkinter import *
import requests
from datetime import datetime, date , time
import json
from window import MainWindow as window
from operation import MainOperation as Operation
from operation import JsonSumClear
import sched, time

JsonSumClear('Sum')
Operation()

window()
MainFile = open('data.json', 'r', encoding='utf-8')
MainFile2 = MainFile.read()
a = json.loads(MainFile2)
MainFile.close()
g = 0
d = a['AllMoney']



# for i in a['AllMoney']['Sum']:
#     print(i)

