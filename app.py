from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello! Flask is running this is main page!'

@app.route('/vineetha')
def about():
    return 'this vineetha second url page'

@app.route('/kajalpage')
def kajal():
    return 'this is kajal personal page'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)