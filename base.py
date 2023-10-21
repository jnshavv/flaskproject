import email
from email.message import EmailMessage
from this import d
from flask import *

from dbm import displayrec, displayrec1, displayrec2, insertrec, insertrec1, selectrec,selectrec1,updaterec,display,insertrec2,displaydon,deleterec










#from project.dbm import selectrec1

app = Flask(__name__,template_folder="templates")


@app.route("/")

def wel():
    return render_template("welcome.html")


@app.route("/register")
def reg():
    return render_template("register.html")  

@app.route("/sendr")     
def sendr():
    return render_template("sendrequestform.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/donation")
def camp():
    return render_template("campreg.html")    





@app.route("/log", methods=["post"])
def log():
    email = request.form["email"]
    password1 = request.form["password"]
    t = (email, password1)
    t1 = selectrec(email)
    if t in t1:
        d=displayrec2(email)
        return render_template("donoredit.html",elist=d)
    

    else:
        return redirect("login.html")    



@app.route("/insert", methods=["post"])
def ins():
    
    donorname = request.form["dname"]
  
    gender=request.form["gender"]
    age=request.form["age"]
    bloodgroup=request.form["blood"]
    email = request.form["email"]
    password = request.form["passw"]
    contact = request.form["con"]
    t = ( donorname,gender,age,bloodgroup, email, password, contact)
    insertrec(t)

    return  render_template("success.html",s="registered successfully") 


    


@app.route("/insert1", methods=["post"])
def inser():

    name = request.form["uname"]
    gender=request.form["gender"]
    age=request.form["age"]
    bloodgroup=request.form["blood"]
    email = request.form["email"]
    contact = request.form["con"]
    address=request.form["address"]
    t = (name,gender,age,bloodgroup, email, contact,address)
    insertrec1(t)
    return  render_template("success.html",s='registered successfully')



@app.route("/insert2", methods=["post"])

def insercamp():

    camp = request.form["camp"]
    dod=request.form["date"]
    units=request.form["nou"]
    location=request.form["loc"]
    email=request.form["email"]
    t = (camp,dod,units,location,email)
    insertrec2(t)
    
    info = displaydon(email)
    return  render_template("showdonation.html",elist=info)    


@app.route("/update", methods=["post"])
def up():
   donorname = request.form["uname"]
  
   gender=request.form["gender"]
   age=request.form["age"]
   bloodgroup=request.form["blood"]
   email = request.form["email"]
   password = request.form["pass"]
   contact = request.form["con"]
   t = ( donorname,gender,age,bloodgroup, email, password, contact,email)
   updaterec(t)
   
   return redirect("/donors")  
   

@app.route("/edit")
def ed():
    edit_email = request.args.get("email")
    info = selectrec1(edit_email)
    return render_template("edit.html", elist=info)


@app.route("/delete")
def dele():
    em = request.args.get("email")
    deleterec(em)
    return render_template('delete.html',s='The Donor has deleted') 


@app.route("/donors")
def details():
    d = displayrec()
    return render_template("donorform.html", elist=d)





@app.route("/afteredit")
def details1():
    d = display()
    return render_template("donoredit.html", elist=d)




@app.route("/viewdonation")
def viedon():
    edit_email =request.form["email"]
    d = displaydon(edit_email)
    return render_template("showdonation.html", elist=d)





  



'''@app.route("/donoredit")
def details1():
    email = request.form["email"]
    password1 = request.form["password"]
    t=(email,password1)
    d = displayrec2(t)
    return render_template("donoredit.html", elist=d)   ''' 




@app.route("/viewr")
def sendrequest():
     d=displayrec1()
     return render_template("viewrequest.html",elist=d)


if __name__ == "__main__":
    app.run(debug=True)
