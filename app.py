from flask import Flask,render_template ,Response,redirect,request,flash,url_for,Request,session
from sql import authentication,registration,partnership_form
from ai import call_ai


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

@app.route('/patnership')
def patnership():

    return render_template('website/patnership.html')
#-----------------------user login ------------
@app.route('/login',methods = ['GET','POST'])
def user_login():
    name = request.form.get("email")
    password = request.form.get("password")
    
    user_data =  authentication(name,password)
    print(user_data)
    
    if(len(user_data)>0):
            session['user_data'] = user_data[0]
            user_data = session.get('user_data')
            return render_template('/user/index.html',user_data=user_data)

    return redirect(url_for('login'))

@app.route('/user/signup')
def user_signup():
    return render_template('/website/signup.html')
@app.route('/patnership',methods = ['GET','POST'])
def appointment():
    name = request.form.get("name")
    type = request.form.get("type")
    email= request.form.get("email")
    mobile_no = request.form.get("number")
    message = request.form.get("message")
    list = [name,email,type,mobile_no,message]
    resp = partnership_form(list)
    if resp== 202:
        disp_message= "Thank You. We Will Reach Out You Soon"
        color = 'green'
        return render_template('/website/appointment.html',disp_message=disp_message,c = color)
    else:
        disp_message= "Something Went Wrong"
        color = 'red'
        return render_template('/website/appointment.html',disp_message=disp_message,c =color)


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

#----------------------user registration---------------
@app.route('/register_data',methods = ['GET','POST'])
def register_data():
    name = request.form.get("name")
    password = request.form.get("password")
    email= request.form.get("email")
    mobile_no = request.form.get("number")
    dob = request.form.get("dob")
    list = [102,name,password,email,mobile_no,dob]
    print(list)
    resp = registration(list)
    if resp == 202 :
        session['user_data'] = list
        user_data = session.get('user_data')
        return render_template('/user/index.html',user_data=user_data)
    else:
        return render_template('/website/signup.html')
#-----------------ai-----------------
@app.route("/call_ai",methods = ['GET','POST'])
def ai():
    query = request.form.get("text")
    print(query)
    reponse = call_ai(query)

    return render_template("/user/health_tips.html",user_data=user_data,ai_result=reponse)


#---------------------------doctor ------------------
@app.route('/doctor')
def Doctor():
    
    return render_template('/doctor/index.html')

@app.route('/doctor/<Name>')
def doctor_page(Name):
    # user_data = session.get('user_data')
    return render_template(f"/doctor/{Name}.html")

@app.route('/admin/<Name>')
def admin_routing(Name):
    return render_template(f'/admin/{Name}.html')

if __name__ == "__main__":
    app.run(debug=True)
