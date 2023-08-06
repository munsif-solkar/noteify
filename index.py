from flask import Flask,render_template,request,redirect,session,send_from_directory
from flask_sqlalchemy import SQLAlchemy
import socket
from datetime import date
import time
import random


web = Flask(__name__,static_folder='static')
web.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
web.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
web.secret_key = "zxccxz"
web_db = SQLAlchemy(web)
# upload_folder = web.config['UPLOAD_FOLDER'] = web.root_path.rsplit('/',1)[0]
class register(web_db.Model):
    id = web_db.Column(web_db.Integer,primary_key=True)
    mainUsername = web_db.Column(web_db.String(20),unique=True,nullable=False)
    username = web_db.Column(web_db.String(20),unique=True,nullable=False)
    password = web_db.Column(web_db.String(20),unique=False,nullable=False)
    accountBirthDate = web_db.Column(web_db.String(20),unique=False,nullable=False)

class data(web_db.Model):
    id = web_db.Column(web_db.Integer,primary_key=True)
    uniqueKey = web_db.Column(web_db.String(20),unique=False,nullable=False)
    uniquePublicKey = web_db.Column(web_db.String(20),unique=False,nullable=False)
    date = web_db.Column(web_db.String(20),unique=False,nullable=False)
    user = web_db.Column(web_db.String(20),unique=False,nullable=False)
    mainUser = web_db.Column(web_db.String(20),unique=False,nullable=False)
    note_title = web_db.Column(web_db.String(100),unique=False,nullable=False)
    note_muscle = web_db.Column(web_db.String(200),unique=False,nullable=False)
    isPrivate = web_db.Column(web_db.String(20),unique=False,nullable=False)


class recently(web_db.Model):
    id = web_db.Column(web_db.Integer,primary_key=True)
    uniqueKey = web_db.Column(web_db.String(20),unique=False,nullable=False)
    uniquePublicKey = web_db.Column(web_db.String(20),unique=False,nullable=False)
    date = web_db.Column(web_db.String(20),unique=False,nullable=False)
    user = web_db.Column(web_db.String(20),unique=False,nullable=False)
    mainUser = web_db.Column(web_db.String(20),unique=False,nullable=False)
    note_title = web_db.Column(web_db.String(100),unique=False,nullable=False)
    note_muscle = web_db.Column(web_db.String(200),unique=False,nullable=False)
    isPrivate = web_db.Column(web_db.String(20),unique=False,nullable=False)

print(web.root_path)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
host = s.getsockname()

def currentDate():
    dmy = time.strftime('%d/%m/%y')
    return dmy

@web.route('/',methods=['GET','POST'])
def index():
    session["isLogged"] = False
    if "check_username" in session:
        session["isLogged"] = True
        return redirect('/panel')
    return render_template('home.html')


def usernameExistence(uname):
    if len(list(register.query.filter_by(mainUsername=uname))) < 1 and len(uname) > 3:
        return True
    else:
        return False
@web.route('/register',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        Username = request.form['username'].lower()
        MainUsername = request.form['mainUsername'].lower()
        Password = request.form['password']
        if len(list(register.query.filter_by(username=Username))) > 0:
            return render_template('register.html',usernameAlert=1)
        elif not usernameExistence(MainUsername):
            return render_template('register.html',usernameAlert=2)
        else:
            web_db.session.add(register(
                username=Username,
                password=Password,
                mainUsername=MainUsername,
                accountBirthDate=currentDate()))
            web_db.session.commit()
            session["holdEmail"] = Username
            session["holdUsername"] = MainUsername
            return redirect('/login')
    usernameAlert = 0
    return render_template('register.html',usernameAlert=0)
    
@web.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        check_username = request.form['username'].lower()
        check_password = request.form['password']
        for items in register.query.all():
            if check_username == items.username:
                check_password_indb = register.query.filter_by(username=check_username).first()
                if check_password == check_password_indb.password:
                    email = register.query.filter_by(password=check_password).first()
                    session.permanent = True
                    session["check_username"] = check_username
                    session["main_username"] = register.query.filter_by(username=check_username).first().mainUsername
                    try:
                        session['holdEmail'] = ''
                        session['holdUsername'] = ''
                    except:
                        pass
                    session["isLogged"] = True
                    return redirect('/panel')
                    break
                else:
                    alert = 1
                    return render_template('login.html',alert=alert)
                    break
        alert = 1
        return render_template('login.html',alert=alert)
    alert = 0
    if "check_username" in session:
        return redirect('/panel')
    return render_template('login.html',alert=alert)

@web.route('/panel/')
def panel():
    renderDate = date.today()
    if "check_username" in session:
        username = session["check_username"]
        main_username = session['main_username']
        usdata = data.query.all()
        data_filter = []
        for gold in usdata:
            if gold.user == username:
                data_filter_dict = {'date':gold.date,'title':gold.note_title,'muscle':gold.note_muscle,'key':gold.uniqueKey,'isPrivate':gold.isPrivate}
                data_filter.append(data_filter_dict)
        data_filter.reverse()
        return render_template('panel.html',username=username,main_username=main_username,data_filter=data_filter,renderDate=currentDate())
    else:
        return redirect('/login')


@web.route('/panel/logout')
def logout():
    session.pop('check_username',None)
    return redirect('/login')

@web.route('/panel/add',methods=['POST','GET'])
def addNew():
    renderDate = date.today()
    if "check_username" in session:
        username = session["check_username"]
        main_username =  session['main_username']
        if request.method == 'POST':
            noteTitle = request.form['note_title']
            noteMuscle = request.form['note_muscle']
            date_today=time.strftime('%d/%m/%y')
            uniqueKey = "".join(random.sample('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890',10))
            uniquePublicKey = "".join(random.sample('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890',19))
            web_db.session.add(data(uniqueKey=uniqueKey,uniquePublicKey=uniquePublicKey,date=date_today,user=username,mainUser=main_username,note_title=noteTitle,note_muscle=noteMuscle,isPrivate='yes'))
            web_db.session.commit()
            return redirect('/panel/read='+uniqueKey)
        # return render_template('addNew.html',username=username,renderDate=f'{renderDate.day}/{renderDate.month}/{renderDate.year}')
        return redirect('/')
    else:
        return redirect('/login')

@web.route('/panel/<delt>',methods=['GET','POST'])
def delete(delt):
    perform = delt.rsplit('=',1)
    # perform[0] = perform[0].replace('?','')
    # print(perform[0])
    try:
        #move to trash
        if perform[0] == 'delete':
            try:
                sip = data.query.filter_by(uniqueKey=perform[1]).first()
                if sip.user == session['check_username']:
                    web_db.session.add(recently(uniqueKey=sip.uniqueKey,uniquePublicKey=sip.uniquePublicKey,date=sip.date,user=sip.user,mainUser=sip.mainUser,note_title=sip.note_title,note_muscle=sip.note_muscle,isPrivate='yes'))
                    web_db.session.commit()
                    web_db.session.delete(sip)
                    web_db.session.commit()
                    return redirect('/panel')
                else:
                    return redirect('/panel')
            except:
                return redirect('/panel')

        #permanent delete
        elif perform[0] == 'permanent':
            try:
                sip = recently.query.filter_by(uniqueKey=perform[1]).first()
                if sip.user == session['check_username']:
                    web_db.session.delete(sip)
                    web_db.session.commit()
                    return redirect('/panel/trash')
                else:
                    return redirect('/panel/trash')
            except:
                return redirect('/panel/trash')

        #edit
        elif perform[0] == 'edit':
            try:
                sip = data.query.filter_by(uniqueKey=perform[1]).first()
                if sip.user == session['check_username']:
                    if request.method == 'POST':
                        edited_note_title = request.form['edited_note_title']
                        edited_note_muscle = request.form['edited_note_muscle']
                        sip.note_title = edited_note_title
                        sip.note_muscle = edited_note_muscle
                        web_db.session.commit()
                        return redirect('/panel/read='+perform[1])
                    # return render_template('edit.html',date=sip.date,title=sip.note_title,note=sip.note_muscle)
                    return redirect('/')
                else:
                    return redirect('/panel')
            except:
                return redirect('/panel')

        #read        
        elif perform[0] == 'read':
            try:
                sip = data.query.filter_by(uniqueKey=perform[1]).first()
                if sip.user == session['check_username']:
                    date = sip.date
                    title = sip.note_title
                    note = sip.note_muscle
                    key = sip.uniqueKey
                    return render_template('read.html',date=date,title=title,note=note,key=key,uniquePublicKey=sip.uniquePublicKey,isPrivate=sip.isPrivate,host=[host[0],5000])
                    
                else:
                    return redirect('/panel')
            except:
                return redirect('/panel')

        #public handler
        elif perform[0] == 'publicView':
            try:
                sip = data.query.filter_by(uniqueKey=perform[1]).first()
                if sip.user == session['check_username']:
                    if sip.isPrivate == 'yes':
                        resetPublicKey = "".join(random.sample('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890',19))
                        sip.uniquePublicKey = resetPublicKey
                        sip.isPrivate = 'no'
                        web_db.session.commit()
                        return redirect('/panel/read='+perform[1])
                    else:
                        sip.isPrivate = 'yes'
                        web_db.session.commit()
                        return redirect('/panel/read='+perform[1])
                    
                else:
                    return redirect('/panel')
            except:
                return redirect('/panel')


        #restore
        elif perform[0] == 'restore':
            try:
                sip = recently.query.filter_by(uniqueKey=perform[1]).first()
                if sip.user == session['check_username']:
                    date = sip.date
                    title = sip.note_title
                    note = sip.note_muscle
                    key = sip.uniqueKey    
                    uniquePublicKey = sip.uniquePublicKey
                    web_db.session.add(data(uniqueKey=key,uniquePublicKey=uniquePublicKey,date=date,user=sip.user,note_title=title,note_muscle=note,isPrivate=sip.isPrivate))
                    web_db.session.commit()
                    web_db.session.delete(sip)
                    web_db.session.commit()
                    return redirect('/panel')
                else:
                    return redirect('/panel')
            except:
                return redirect('/panel')

    except:
        return redirect('/panel')

    return redirect('/panel')

@web.route('/panel/trash')
def bin():
    if "check_username" in session:
        username = session["check_username"]
        usdata = recently.query.all()
        data_filter = []
        for gold in usdata:
            if gold.user == username:
                data_filter_dict = {'date':gold.date,'title':gold.note_title,'muscle':gold.note_muscle,'key':gold.uniqueKey}
                data_filter.append(data_filter_dict)
        data_filter.reverse()
        return render_template('trash.html',username=username,data_filter=data_filter)
    else:
        return redirect('/login')

#Public handler
@web.route('/v/<this>')
def publicView(this):
    session['isLogged'] = False
    date_today = time.strftime('%d/%m/%y')
    if "check_username" in session:
        session['isLogged'] = True
    try:
        sip = data.query.filter_by(uniquePublicKey=this).first()
        if sip.isPrivate == 'no':
            if "check_username" in session:
                if sip.user == session['check_username']:
                    return redirect(f'/panel/read={sip.uniqueKey}')
            sharedBy = sip.mainUser
            return render_template('publicread.html',title=sip.note_title,date=sip.date,note=sip.note_muscle,user=sharedBy,isLogged=session['isLogged'],date_today=date_today)
        else:
            return redirect('/login')
    except:
        return redirect('/panel')


if __name__ == "__main__":
    # s.getsockname()[0]
    web.run(debug=True,host=host[0],port=5000)
