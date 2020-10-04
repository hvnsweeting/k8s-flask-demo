import os
from flask import Flask

app = Flask("hi")


@app.route("/")
def hello():
    return "Hello Pymi.vn"


@app.route("/env")
def read_env():
    config = os.environ.get("K8S_CONFIGMAP")
    secret = os.environ.get("K8S_SECRET")
    return "Hello Pymi.vn, config: {} secret: {}".format(config, secret)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
