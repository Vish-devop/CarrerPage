from flask import Flask

app=Flask(__name__)
@app.route('/')
def Greeting():
    return ("Hey, It's my first program in Flask -> Good to see you")

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)

