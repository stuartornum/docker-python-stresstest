import time
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    st = time.mktime(time.gmtime())
    ft = time.mktime(time.gmtime()) - st
    return "Hello World! time: {0}".format(ft)

if __name__ == "__main__":
    app.run()
