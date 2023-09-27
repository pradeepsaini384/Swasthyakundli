from flask import Flask,render_template ,Response,redirect,request,flash,url_for,Request,session
from sql import authentication,registration,partnership_form,patient_record_saving,get_records,admin_authentication
from ai import call_ai
import os
from werkzeug.utils import secure_filename
import requests

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
user_data = None
admin_data = None
UPLOAD_FOLDER = 'static/images/Reports/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#---------------- website Directories ------------------
@app.route('/')
def website_home():
    return render_template('/website/index.html')

@app.route('/Website_Contact')
def Website_Contact():
    return render_template('/website/contact.html')


@app.route('/user_login_page')
def user_login_page():
    return render_template('/website/user-login.html')
@app.route('/doctor_login_page')
def doctor_login_page():
    return render_template('/website/doctor-login.html')
@app.route('/admin_login_page')
def admin_login_page():
    return render_template('/website/admin-login.html')

@app.route('/appointment')
def patnership():

    return render_template('website/appointment.html')
#-----------------------user login ------------
@app.route('/user_login',methods = ['GET','POST'])
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
@app.route('/doctor_login',methods = ['GET','POST'])
def doctor_login():
    name = request.form.get("email")
    password = request.form.get("password")
    
    user_data =  authentication(name,password)
    print(user_data)
    
    if(len(user_data)>0):
            session['user_data'] = user_data[0]
            user_data = session.get('user_data')
            return render_template('/doctor/index.html',user_data=user_data)

    return redirect(url_for('login'))
@app.route('/admin_login',methods = ['GET','POST'])
def admin_login():
    name = request.form.get("email")
    password = request.form.get("password")
    
    user_data =  admin_authentication(name,password)
    print(user_data)
    
    if(len(user_data)>0):
            session['admin_data'] = user_data[0]
            admin_data = session.get('admin_data')
            return render_template('/admin/index.html',user_data=admin_data)

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
    if Name=="health_history":
         resp = get_records(user_data[0])
         print(resp)
         return render_template(f"/user/{Name}.html",user_data = user_data,user_records=resp)
    if Name=="care_center1":
        url = "https://api.data.gov.in/resource/de59e770-2333-4eaf-9088-a3643de040c8?api-key=579b464db66ec23bdd000001632b336f56834f2054f46036789c78e4&format=json&limit=20&filters%5B_cityname_%5D=jaipur"
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response if the API returns JSON data
            data = response.json()
            
            # Now you can work with the 'data' variable, which contains the API response
            return render_template(f"/user/{Name}.html",user_data = user_data,hospital_list=data['records'])
            

        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code}")
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
    admin_data = session.get('admin_data')
    return render_template(f'/admin/{Name}.html',user_data=admin_data)

@app.route("/call_ai_doctor",methods = ['GET','POST'])
def doctor_ai():
    query = request.form.get("text")
    print(query)
    reponse = call_ai(query)
    return render_template("/doctor/health_tips.html",user_data=user_data,ai_result=reponse)
@app.route('/save_record',methods=['GET','POST'])
def save_record():
    report_data = request.form.get("report_data")
    date = request.form.get("date")
    Report_info = request.form.get("Report_info")
    Doctors_info = request.form.get("Doctors_info")
    report_status = request.form.get("customColorRadio")
    
    patient_reports = request.files['patient_reports']
    
    user_data = session.get('user_data')
    if patient_reports:
        # resized_image = Image.open(file)
        # resized_image = resized_image.resize((300,230))
        
        username= user_data[1]
        user_id = user_data[0]
        
        path = app.config['UPLOAD_FOLDER']+f'{username}'
        
        if not os.path.exists(path):
            os.makedirs(path)
        filename = secure_filename(patient_reports.filename)
        patient_reports.save(os.path.join(path, filename))
        filedic = path+filename
        # print(filedic)
        patient_report_list = [user_id,report_data,date,filedic,Report_info,Doctors_info,report_status]
        resp = patient_record_saving(patient_report_list)
        if resp == 202:
            message = "Details Entered Successfully!"
            color = "green"
            return render_template('/user/recordData.html',message = message,color = color,user_data=user_data)
        else:
            message = "Duplicate entry or Something error!"
            color = "red"
            return render_template('/user/recordData.html',message = message,color = color,user_data=user_data)
        
    else:
            message = "Duplicate entry or Something error!"
            color = "red"
            return render_template('/user/recordData.html',message = message,color = color,user_data=user_data)
if __name__ == "__main__":
    app.run(debug=True)
