from flask import Flask, render_template, request, redirect
from routerinfo import list
#feedback
#Add checkbox ->replace cross
# abillity to assign to someone


print(list)
app = Flask(__name__)

db = [] #could potentially save it to a file to prevent server crash
maintasks = open("dashboardsite/tasks.txt","r+")
for line in maintasks:
    db.append(line)
maintasks.close()

def sendemail(NewTask):
    print(NewTask)

@app.route('/',methods=["GET","POST"])
def dashboard():
    maintasks = open("dashboardsite/tasks.txt","a")
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
 

@app.route('/manas',methods=["GET","POST"])
def manas():
    return "Manas Home page"

@app.route('/vaibhav',methods=["GET","POST"])
def vaibhav():
    return "Vaibhav Home page"

@app.route('/vineet',methods=["GET","POST"])
def vineet():
    return "Vineet Home page"

@app.route('/arpita',methods=["GET","POST"])
def arpita():
    return "Arpita Home page"

@app.route('/network',methods=["GET","POST"])
def network():
    routername = list[0]['DeviceName']
    devices=[]
    for items in list[1]:
        devices.append(items[0])

    return render_template("routerinfo.html",name = routername,devices = devices)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 8090)
