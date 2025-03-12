from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!" \

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


cd D:\DSML\flask_app
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/Krishsharma3/FlaskApp.git
git push -u origin main
