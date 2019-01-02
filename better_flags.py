##################################
# Better flags v0.1
# author : Wobo#1287
##################################

import ac, acsys
import platform, os, sys

if platform.architecture()[0] == "64bit":
    sysdir = os.path.dirname(__file__)+'/lib/stdlib'
else:
    sysdir = os.path.dirname(__file__)+'/lib/stdlib64'

sys.path.insert(0, sysdir)
os.environ['PATH'] = os.environ['PATH'] + ";."

from lib.sim_info import info

import ctypes
from ctypes import wintypes

scale = 1
ui_flag = 0
flagtype = 0
timer = 0
timer1 = 0
appWindow = 0

def acMain(ac_version):
    global ui_flag, scale, flag, appWindow

    width = 400
    height = 70
    font_size = 50
    scaled_width = width * scale
    scaled_height = height * scale
    scaled_font = font_size * scale

    appName = "Better Flags"
    appWindow = ac.newApp(appName)
    ac.setTitle(appWindow, "")
    ac.setSize(appWindow, int(scaled_width), int(scaled_height))
    ac.drawBorder(appWindow, 0)
    ac.setBackgroundOpacity(appWindow, 0)
    ac.setIconPosition(appWindow, 0, -10000)

    ui_flag = ac.addLabel(appWindow, "")
    ac.setFontAlignment(ui_flag, "center")
    ac.setPosition(ui_flag, int(scaled_width/2), 0) #
    ac.setFontSize(ui_flag, int(scaled_font))
    ac.setText(ui_flag, "")


    ac.log("WCZYTANO FLAGI")
    return appName


def acUpdate(deltaT):
    global timer, timer1, flagtype, appWindow

    timer += deltaT
    timer1 += deltaT

    # Limit frequency to 60hz
    if timer > 0.0166:
        timer = 0
        flagtype = info.graphics.flag
        check_flag_type()
        ac.console(str(flagtype))

    # Limit frequency to 1hz
    if timer1 > 1:
        timer1 = 0
        ac.setBackgroundOpacity(appWindow, 0)


def check_flag_type():
    global flagtype
    if flagtype == 1:
        # Blue flag
        set_blue_flag()
    elif flagtype == 2:
        # Yellow flag
        set_yellow_flag()
    else:
        # Clears flags
        clear_flags()


def set_blue_flag():
    global flagtype, ui_flag
    ac.setText(ui_flag, "BLUE FLAG")
    ac.setFontColor(ui_flag, 0, 0, 1, 1)
    ac.console("BLUE FLAG")


def set_yellow_flag():
    global flagtype, ui_flag
    ac.setText(ui_flag, "YELLOW FLAG")
    ac.setFontColor(ui_flag, 1, 1, 0, 1)
    ac.console("YELLOW FLAG")


def clear_flags():
    global flagtype, ui_flag
    ac.setFontColor(ui_flag, 1, 1, 1, 0)
    ac.console("CLEAR FLAG")

