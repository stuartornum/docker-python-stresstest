import time
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    st = time.mktime(time.gmtime())
    c = 0
    while c != 10000000:
        c += 1
    ft = time.mktime(time.gmtime()) - st
    return "Hello World! time: {0}".format(ft)

if __name__ == "__main__":
    app.run()
