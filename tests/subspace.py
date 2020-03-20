from telegram.ext import *
import logging
import os
import pyautogui
import subprocess
import time
import win32gui, win32com.client
from telegram.error import *


exes = []

def get_all_exes(root):
	global exes;
	try:
		for fol in os.listdir(root):
			if "." not in fol:
				get_all_exes(root+fol+"/")
			else:
				if "exe" in fol[len(fol)-3::]:
					print(fol)
					exes.append(fol)
	except:
		return


get_all_exes("C://Program Files/")


