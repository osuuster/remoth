import sys
from os import path
from threading import Thread

from flask import Flask
from keyboard import send
from PIL import Image
from pystray import Icon, Menu, MenuItem
import mouse

if sys.platform == "linux" or sys.platform == "linux2":
    platform = "linux"
elif sys.platform == "darwin":
    from osascript import osascript
    platform = "OSX"
elif sys.platform == "win32":
    platform = "windows"
else:
    sys.exit()

base_dir = path.join(sys._MEIPASS) if hasattr(sys, '_MEIPASS') else "."
static_dir = path.join(base_dir, 'static')
image_dir = path.join(static_dir, "icon.ico")
image = Image.open(image_dir)

icon = Icon('Remoth', icon=image,
            menu=Menu(MenuItem('Close', lambda x: x.stop())))

app = Flask(__name__)
server = Thread(target=app.run, kwargs={"host": "0.0.0.0", "debug": False})
server.setDaemon(True) # Kills the server when icon is stopped


@app.route("/press/<key>")
def press_key(key):
    if platform == "OSX" and key in ["volume_up", "volume_down"]:
        # Temporary hack as volume controls are not supported for mac by keyboard library
        inc = 2 if key == "volume_up" else -2
        current_volume = int(osascript('get volume settings')[1].split(',')[0].split(':')[1])
        osascript(f"set volume output volume {current_volume + inc}")
        return f"{key} pressed"
    send(key)
    return f"{key} pressed"

@app.route("/move_mouse/<position>")
def move_mouse(position):
    x,y = position.split("|")
    mouse.move(x, y, absolute=False)
    return f"Moved mouse x:{x} y:{y}"

@app.route("/click_mouse")
def click_mouse():
    mouse.click()
    return "Clicked mouse"

@app.route("/scroll_mouse/<position>")
def scroll_mouse(position):
    mouse.wheel(int(position)/20)
    return "Scrolled mouse"

@app.route("/")
def index():
    return "ok"


if __name__ == "__main__":
    server.start()
    icon.run()
