# from pynput.mouse import Button, Controller
# import time
# from pymouse import PyMouse
# from pykeyboard import PyKeyboard
# m = PyMouse()
# k = PyKeyboard()
# import win32gui,win32con,win32api,win32print

import src.ScreenScale as ScreenScale
windows_common = ScreenScale.WindowsCommon()
ScreenScale = windows_common.getScreenScaleRate()

import pyautogui
print(pyautogui.position())