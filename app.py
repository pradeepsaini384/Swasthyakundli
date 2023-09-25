from flask import Flask,render_template ,Response,redirect,request,flash,url_for,Request



app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/User')
def home():
    return render_template('/user/index.html',name="Pradeep Saini")

@app.route('/User/<Name>')
def user_page(Name):
    return render_template(f"/user/{Name}.html",name="Pradeep Saini")


if __name__ == "__main__":
    app.run()
