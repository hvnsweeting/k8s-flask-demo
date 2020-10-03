from flask import Flask

app = Flask("hi")


@app.route("/")
def hello():
    return "Hello Pymi.vn"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
