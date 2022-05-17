from flask import Flask, ren

app = Flask(__name__)

@app.route('/')
def index():
    # return '<h1>Hello World</h1>'
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(port = 5050, debug = True)