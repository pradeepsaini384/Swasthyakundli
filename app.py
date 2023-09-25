from flask import Flask,render_template ,Response,redirect,request,flash,url_for,Request,session
from sql import authentication

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
user_data = None
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
#-----------------------user login ------------
@app.route('/login',methods = ['GET','POST'])
def user_login():
    name = request.form.get("email")
    password = request.form.get("password")
    
    user_data =  authentication(name,password)
    
    
    if(len(user_data)>0):
            session['user_data'] = user_data[0]
            user_data = session.get('user_data')
            return render_template('/user/index.html',user_data=user_data)

    return redirect(url_for('login'))

@app.route('/user/signup')
def user_signup():
    return render_template('/website/signup.html')
@app.route('/appointment')
def appointment():
    return render_template('/website/appointment.html')


#-----------users--------------------

@app.route('/User')
def User():
    user_data = session.get('user_data')
    return render_template('/user/index.html',user_data = user_data)

@app.route('/User/<Name>')
def user_page(Name):
    user_data = session.get('user_data')
    return render_template(f"/user/{Name}.html",user_data = user_data)


@app.route('/user_record1',methods = ['GET','POST'])
def user_record1():
    name = request.form.get("user_name")
    password = request.form.get("password")
    email= request.form.get("email")
    mobile_no = request.form.get("number")
    
    return 'done'

if __name__ == "__main__":
    app.run(debug=True)
