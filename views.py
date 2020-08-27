import csv
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'index.html')

def addstudent(request):
    return render(request,'addstudent.html')

def showstudent(request):
    return render(request,'showstudent.html')

def appendata(studentid, studentname, gender, date, city, state, email_id, qualification, stream):
    fieldnames = ['studentid', 'studentname', 'gender', 'date', 'city', 'state', 'email_id', 'qualification', 'stream']
    with open('students.csv', 'a+', newline='\n') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writerow({
            'studentid' : studentid,
            'studentname' : studentname,
            'gender' : gender,
            'date' : date,
            'city' : city,
            'state' : state,
            'email_id' : email_id,
            'qualification' : qualification,
            'stream' : stream,

        })

def retrieve(request):
    studentid = request.POST['studentid']
    studentname = request.POST['studentname']
    gender = request.POST['gender']
    date = request.POST['date']
    city = request.POST['city']
    state = request.POST['state']
    email_id = request.POST['email_id']
    qualification = request.POST['qualification']
    stream = request.POST['stream']
    appendata(studentid, studentname, gender, date, city, state, email_id, qualification, stream)
    return render(request,'showresult.html',{'name':studentname})


def showstudentdetails(request):
    id = int(request.POST["id"])
    with open("students.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        rows = [r for r in reader]
    val = rows[id]
    return render(request,'showdata.html', {'val':val})

def allstudent(request):
    return render(request,'allstudent.html')

def allstudentdetail(request):
    with open("students.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        rows = [r for r in reader]
    row = rows[0:]
    return render(request,'showalldetail.html',{'row':rows})
