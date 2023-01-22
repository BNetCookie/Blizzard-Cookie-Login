import py_cui
import os
from winproxy import ProxySetting
from mitmproxy import http
from mitmproxy.tools.main import mitmdump
import time
import threading
from py_cui import py_cui, PyCUI

os.system('mode con: cols=85 lines=25')

class BlizzardCookie:

    
    def __init__(self, master: PyCUI):
        
        self.master = master
        
        self.master.set_refresh_timeout(0.1)
        
        self.master.toggle_unicode_borders()

        self.master.set_title('Blizzard Cookie Login')

        self.cookie = self.master.add_text_box("COOKIE:", 1, 1, 1, 4)

        self.console = self.master.add_scroll_menu('Console:', 4, 0, 3, 6)

        self.btn = self.master.add_button("LOGIN WITH COOKIE", 3, 1, 1, 4, command=self.startThread)

        self.master.set_status_bar_text('Blizzard Cookie Login | By Fr0st3h#7019')
        
    def setWindowsProxy(self):
        p = ProxySetting()
        p.server = dict(http='127.0.0.1:8080', https='127.0.0.1:8080')
        p.enable = True
        p.display()
        p.registry_write()
        

    def startCookieLogin(self):
        self.console.add_item("Setting Proxy..")
        setWindowsProxy()
        console.add_item("Click START PROXY SERVER and then open the battle.net client")
        console.add_item("The application will freeze after clicking and close after opening Battle.net")
        btn.set_title('START PROXY SERVER')
        
    started = False
        
    def startThread(self):
        global started
        if(started == False):
            thread = threading.Thread(target=self.startCookieLogin)
            thread.start()
            started = True
        else:
            mitmdump(args=["-s", "proxy.py", "-q", '--set', f'cookie={self.cookie._text}'])

if __name__ == "__main__":
    os.system("mode con cols=104 lines=29")
    root = py_cui.PyCUI(6, 6)