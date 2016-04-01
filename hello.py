import time
from socket import gethostname
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    c = 0
    while c != 1000000:
        c +=1
    return "Hello World! time: {0} - {1}".format(int(time.mktime(time.gmtime())), gethostname())

