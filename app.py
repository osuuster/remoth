import sys
from os import path
from socket import gethostname, gethostbyname_ex, getfqdn
from threading import Thread

from flask import Flask
from keyboard import press
from PIL import Image
from pystray import Icon, Menu, MenuItem

base_dir = path.join(sys._MEIPASS) if hasattr(sys, '_MEIPASS') else "."
staticDir = path.join(base_dir, 'static')
image = Image.open(staticDir + "\icon.ico")

icon = Icon('Remoth', icon=image,
            menu=Menu(MenuItem('Close', lambda x: x.stop())))

app = Flask(__name__)
server = Thread(target=app.run, kwargs={"host": "0.0.0.0", "debug": False})
server.setDaemon(True) # Kills the server when icon is stopped


@app.route("/press/<key>")
def press_key(key):
    press(key)
    return f"{key} pressed"


@app.route("/")
def index():
    return {
        "ip": gethostbyname_ex(getfqdn())[2][1],
        "host_name" : gethostname()
    }


if __name__ == "__main__":
    server.start()
    icon.run()
