from flask import Flask, render_template, request, redirect
#from routerinfo import list
from weather import weatherinfo
import pprint
import datetime
from pynetgear import Netgear

app = Flask(__name__)

db = [] #could potentially save it to a file to prevent server crash
maintasks = open("dashboardsite/tasks.txt","r+")
for line in maintasks:
    db.append(line)
maintasks.close()

## Main Dashboard 
@app.route('/',methods=["GET","POST"])
def dashboard():
    maintasks = open("dashboardsite/tasks.txt","a")
    print(weatherinfo)
    if request.method == "POST":
        NewTask = request.form["taskentry"]
        AssignTo =request.form["assignto"]
        Tasktoadd = AssignTo + ":  " + NewTask + "\n"
        NewTask = NewTask +"\n"
        if len(NewTask) > 0 and not NewTask in db:
            db.append(Tasktoadd)
            maintasks.writelines(Tasktoadd)

        else:
            print("invalid Entry")
    maintasks.close()
    with open("dashboardsite/tasks.txt", "r+") as file1:
        print(file1.read())
    return render_template("index.html", tasks = db,numelements = len(db))

@app.route('/delelement/<task>')
def delelement(task):

    filename = "dashboardsite/tasks.txt"
    
    db.remove(task)
    print(task)
    f = open(filename, "w")
    f.writelines(db)
    f.close()
    return redirect(f"/")
 

##Profile Pages
#each webpage can be assigned to a different profile 
@app.route('/manas',methods=["GET","POST"])
def manas():
    return render_template("manas.html")

@app.route('/vaibhav',methods=["GET","POST"])
def vaibhav():
    return render_template("vaibhav.html")

@app.route('/vineet',methods=["GET","POST"])
def vineet():
    return render_template("vineet.html")

@app.route('/arpita',methods=["GET","POST"])
def arpita():
    return render_template("arpita.html")

##Other Pages
##router info page
@app.route('/network',methods=["GET","POST"])
def network():
    list = routerinfo()
    routername = list[0]['DeviceName']
    devices=[]
    for items in list[1]:
        devices.append(items[0])
    return render_template("routerinfo.html",name = routername,devices = devices)

## Kitchen page
@app.route('/kitchen',methods=["GET","POST"])
def kitchen():
    return render_template("kitchen.html")




# Functions needed for app to run 

#sends email to person who the task is assigned to
def sendemail(NewTask):
    print(NewTask)

def routerinfo():
    netgear = Netgear(password="********")
    devices = netgear.get_attached_devices()

    routerinfo = netgear.get_info()

    list = []
    list.append(routerinfo)
    list.append(devices)
    return list

if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 8090)
