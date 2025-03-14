# Send-Payload-to-PS

You must create a server on your iPhone with default port 5000 so that the page can send the payload to PS.
# 
![Screenshot 2025-03-12 193947](https://github.com/user-attachments/assets/48f65be2-7b47-4a32-99f8-c421bbcd2954)

## Verify Python and pip installation
Open the iSH application and enter the following commands:

[Download Apple Store IOS](https://apps.apple.com/us/app/ish-shell/id1436902243)

To verify Python installation, type:

```
python3 --version
```
If Python is installed, the version will appear as follows:

```
Python 3.x.x
```
## If the version doesn't appear, Python isn't installed. You can reinstall it using:

```
apk add python3
```
## To verify pip installation, type:


pip3 --version
## If pip is installed, the version will appear as follows:


pip x.x.x from /usr/lib/python3.x/site-packages/pip (python 3.x)
## If it isn't installed, install it using:

```
apk add py3-pip
```
## Verify Flask is installed
Type:

```
python3 -m flask --version
```
## If Flask is installed, the version will be displayed as:


Python 3.x.x
Flask x.x.x
Werkzeug x.x.x

## If it isn't installed, you can install it with:
```
pip3 install flask

pip3 install flask-cors
```
##socat
```socat
apk add socat
```

 Verify that all prerequisites are installed at once

## You can verify that all packages are installed with the command:
```
python3 -c "import flask; print('Flask is installed!')"
```
## If Flask is installed, the message will be displayed:


Flask is installed!

## Files will be uploaded soon

https://github.com/user-attachments/assets/35acc892-6981-42dc-82db-c82fe8dbf814

