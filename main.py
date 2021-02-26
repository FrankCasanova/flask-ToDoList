from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world Flask'


# if __name__ == "__main__":
#      app.run(port = 8080, debug = True)