![alt text](icon.ico "Remoth")
# What is Remoth?
Remoth is a home automation tool to send key events to the host PC over WIFI using either a mobile device or another PC. The idea is to have a minimalistic and lightweight API to talk with.

# Build from source:
Create a virtualenv
```
python -m venv venv
```
Active the virtual enviorment
```
.\venv\Scripts\activate
```
Install required dependecies
```
pip install -r requirements.txt
```
Build the exe file
```
pyinstaller -w -F --add-data "static;static" app.py --icon "icon.ico" --name "Remoth" --clean
```

# Usage:
Make sure that all your devices you wish to control are in one private network.

1. Open Remoth application.

2. Navigate to http://localhost:5000/ to see your device name and local IP address.

3. Find your desired key from this map and then call your host:

    https://github.com/boppreh/keyboard/blob/master/keyboard/_winkeyboard.py#L170-L330

# Examples:
Trigger volume down event 

* Call from the host machine:

    http://localhost:5000/press/volume_down

* Call host from another machine:
  
    http://192.168.0.17:5000/press/volume_down


# Licencing:
MIT License
