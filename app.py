from flask import Flask,render_template ,Response,redirect,request,flash,url_for,Request



app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)