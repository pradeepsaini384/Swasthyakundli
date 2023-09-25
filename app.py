from flask import Flask,render_template ,Response,redirect,request,flash,url_for,Request



app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#---------------- website Directories ------------------
@app.route('/')
def website_home():
    return render_template('/website/index.html')

@app.route('/Website_Contact')
def Website_Contact():
    return render_template('/website/contact.html')


@app.route('/login')
def login():
    return render_template('/website/login.html')

@app.route('/user/signup')
def user_signup():
    return render_template('/website/signup.html')
@app.route('/appointment')
def appointment():
    return render_template('/website/appointment.html')




@app.route('/User')
def home():
    return render_template('/user/index.html',name="Pradeep Saini")

@app.route('/User/<Name>')
def user_page(Name):
    return render_template(f"/user/{Name}.html",name="Pradeep Saini")


if __name__ == "__main__":
    app.run(debug=True)
