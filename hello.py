import time
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    st = time.mktime(time.gmtime())
    return "Hello World! time: {0}".format(st)

