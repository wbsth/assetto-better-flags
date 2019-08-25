__author__ = "Michal Ungeheuer"

import ac, acsys
import platform, os, sys
import configparser

if platform.architecture()[0] == "64bit":
    sysdir = os.path.dirname(__file__)+'/lib/stdlib64'
else:
    sysdir = os.path.dirname(__file__)+'/lib/stdlib'

sys.path.insert(0, sysdir)
os.environ['PATH'] = os.environ['PATH'] + ";."

from lib.sim_info import info

import ctypes
from ctypes import wintypes

# Initialize custom font
ac.initFont(0, "Roboto", 1, 1)

# loading config
update_config = False
config_path = 'config.ini'
config = configparser.ConfigParser()
config.read(config_path)

if not config.has_section('Better_Flags'):
    config.add_section('Better_Flags')
    update_config = True

# helper function
def get_val_or_set_def(config, key, default):
    global update_config
    try:
        return config["Better_Flags"][key]
    except:
        config["Better_Flags"][key] = default
        update_config = True

# get config values or set defaults
font_size = int(get_val_or_set_def(config, 'font_size', '50'))

# config update if is it necessary
if update_config:
    with open(config_path, 'w') as config_file:
        config.write(config_file)

ui_flag = 0
flagtype = 0
timer = 0
timer1 = 0
timer2 = 0
appWindow = 0

def acMain(ac_version):
    global ui_flag, flag, appWindow, font_size

    width = 8 * font_size
    height = 2 * font_size

    appName = "Better Flags"
    appWindow = ac.newApp(appName)
    ac.setTitle(appWindow, "")
    ac.setSize(appWindow, int(width), int(height))
    ac.drawBorder(appWindow, 0)
    ac.setBackgroundOpacity(appWindow, 0)
    ac.setIconPosition(appWindow, 0, -10000)

    ui_flag = ac.addLabel(appWindow, "")
    ac.setCustomFont(ui_flag, "Roboto", 0, 1)
    ac.setFontAlignment(ui_flag, "center")
    ac.setPosition(ui_flag, int(width/2), (int(height/2) - int(font_size/2))) 
    ac.setFontSize(ui_flag, int(font_size))
    ac.setText(ui_flag, "")

    return appName


def acUpdate(deltaT):
    global timer, timer1, timer2, flagtype, appWindow

    timer += deltaT
    timer1 += deltaT
    if timer2 < 5:
        timer2 += deltaT

    # for keeping the app visible at beginning
    if timer2 <= 5:
        start_info()

    # normal app functionality
    else:
        # Limit frequency to 60hz
        if timer > 0.0166:
            timer = 0
            flagtype = info.graphics.flag
            check_flag_type()
            ac.console(str(flagtype))

        # Limit frequency to 0.5 hz to keep app background visible for 2 seconds
        if timer1 > 2:
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


def set_yellow_flag():
    global flagtype, ui_flag
    ac.setText(ui_flag, "YELLOW FLAG")
    ac.setFontColor(ui_flag, 1, 1, 0, 1)


def clear_flags():
    global flagtype, ui_flag
    ac.setFontColor(ui_flag, 1, 1, 1, 0)

def start_info():
    global ui_flag
    ac.setText(ui_flag, "Better-Flags")
    ac.setFontColor(ui_flag, 1, 1, 1, 1)
    ac.setBackgroundOpacity(appWindow, 0.6) 

