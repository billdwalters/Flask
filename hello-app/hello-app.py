from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    loop = ''
    names = "brad", "Diana", "Kevin", "Amy", "Tina"
    for friends in names:
        print (friends)
        loop += " : " + friends 
    return loop


if __name__ == '__main__':
    app.debug=True
    app.run()
