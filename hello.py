import time
from socket import gethostname
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! time: {0} - {1}".format(int(time.mktime(time.gmtime())), gethostname())

