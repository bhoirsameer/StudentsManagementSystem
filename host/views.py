from django.shortcuts import render
from django.http import HttpResponse
from host.models import Courses,Trainers,Host,Enquiry,Trainerslogin,Attendence,ToDO
from host.forms import CoursesForm,TrainersForm,AttendenceForm,ToDoForms
import datetime,csv

# Create your views here.



def index(request):
    return render(request,'index.html')



def hostlogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        data = Host.objects.all().values_list()
        for info in data:
            if username == info[1] and password == info[2]:
                # no_of_students = 0
                # students = Enquiry.objects.all().values_list(enrl_status="Enrolled")
                # for student in students:
                #     nno_of_students +=1
                return render(request,'host.html')
            else:
                return render(request,'hostlogin.html')
    else:
        return render(request,'hostlogin.html')
def host(request):
    return render(request,'host.html')

    
def IT(request):
    if request.method == "POST":
        form = CoursesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                ITcourses = Courses.objects.filter(department="IT").values()
                data = {
                'courses':ITcourses
                }
                return render(request,'IT.html',data)
            except Exception as e:
                pass
        else:
            return render(request,'IT.html',{'msg':'error occur while saving data'})
    else:
        courses = Courses.objects.filter(department='IT').values()
        data = {
            'courses':courses
        }
        return render(request,'IT.html',data)
    
def civil(request):
    if request.method == "POST":
        form = CoursesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                ITcourses = Courses.objects.filter(department="Civil").values()
                data = {
                'courses':ITcourses
                }
                return render(request,'civil.html',data)
            except Exception as e:
                pass
        else:
            return render(request,'civil.html',{'msg':'error occur while saving data'})
    else:
        courses = Courses.objects.filter(department='Civil').values()
        data = {
            'courses':courses
        }
        return render(request,'civil.html',data)
    


def mech(request):
    if request.method == "POST":
        form = CoursesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                courses = Courses.objects.filter(department="Mechanical").values()
                data = {
                'courses':courses
                }
                return render(request,'mech.html',data)
            except Exception as e:
                pass
        else:
            return render(request,'mech.html',{'msg':'error occur while saving data'})
    else:
        courses = Courses.objects.filter(department='Mechanical').values()
        data = {
            'courses':courses
        }
        return render(request,'mech.html',data)




def edit(request,id,dept):
    if request.method == "POST":
        department = request.POST['department']
        coursename = request.POST['coursename']
        fees = request.POST['fees']
        description = request.POST['description']
        Courses.objects.filter(id=id).update(
            coursename=coursename,
            department=department,
            fees = fees,
            description = description,
        )
        courses = Courses.objects.filter(department=dept).values()
        data = {
        'courses':courses
        }
        return render(request,'IT.html',data)        

    else:
        courses = Courses.objects.filter(id=id).values()
        data = {
        'courses':courses
        }
        return render(request,'edit.html',data)
    


def delete(request,id,dept):
    course = Courses.objects.filter(id=id,department=dept)
    course.delete()
    courses = Courses.objects.filter(department=dept).values()
    data = {
        'courses':courses
        }
    return render(request,'IT.html',data)



def add_trainer(request):   
    if request.method == "POST":
        form = TrainersForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                trainers = Trainers.objects.all()
                data = {
                    'trainers':trainers
                }
                return render(request,'trainers.html',data)
            except:
                pass
    else:
        trainers = Trainers.objects.all()
        data = {
            'trainers':trainers
        }
        return render(request,'trainers.html',data)
    

def edit_trainer(request,id):
    if request.method == "POST":
        name=request.POST['name']
        department=request.POST['department']
        Trainers.objects.filter(id=id).update(name=name,department=department)
        Trainerslogin.objects
        trainers = Trainers.objects.all().values()
        data = {
            'trainers':trainers
        }
        return render(request,'trainers.html',data)
    else:
        trainers = Trainers.objects.filter(id=id).values()
        data = {
            'trainers':trainers
        }
        return render(request,'edit_trainer.html',data)


def trainer_lgn(request):
    if request.method == "POST":
        data = Trainerslogin.objects.all().values_list()
        username = request.POST['username']
        password = request.POST['password']
        for i in data:
            if i[1] == username and i[2] == password:
                department = i[3]
                enquries = Enquiry.objects.all().filter(Department=department)
                data = {
                    "enquries" : enquries,
                    "department":department,

                }
                return render(request,'trainershomepage.html',data)
        else:
            return render(request,'trainerlogin.html',{"msg":"Invalid Credentials"})
    else:
        return render(request,'trainerlogin.html')


def delete_trainer(request,id):
    trainer = Trainers.objects.filter(id=id)
    trainer.delete()
    trainers = Trainers.objects.all().values()
    data = {
        'trainers':trainers
    }
    return render(request,'trainers.html',data)

def enquiry(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        data = Enquiry.objects.all().filter(email=email)
        if data:
            return render(request,'enquiry.html',{"msg":"Email Id Is already Used Start With Login"})
        address = request.POST['address']
        contact = request.POST['contact']
        education = request.POST['education']
        department = request.POST['department']
        adhaarno = request.POST['adhaarno']
        clgname = request.POST['clgname']
        reference = request.POST['reference']
        date=datetime.datetime.now()
        date=date.strftime("%x")

        form = Enquiry(name=name,
                       email=email,
                       password=password,
                       address=address,
                       contact=contact,
                       education=education,
                       date=date,
                       adhaarno=adhaarno,
                       clgname=clgname,
                       reference=reference,
                       )
        form.save()
        user = Enquiry.objects.all().filter(name=name,
                                            email=email,
                                            adhaarno=adhaarno).values_list()
        for i in user:
            for j in i:
                userid = i[0]
        courses = Courses.objects.filter(department=department).values()
        data = {
            "courses":courses,
            "userid":userid,
        }
        return render(request,'enquiryhome.html',data)
    else:
        return render(request,'enquiry.html')
    
def enroll(request,id):
    if request.method == "POST":
        user = Enquiry.objects.all().values_list().last() # (43, 'Sameer Waman Bhoir', 'Sameer@gmail.com') OUTPUT will be singgle tuple
        course = Courses.objects.all().filter(id=id).values_list() # <QuerySet [(17, 'Django', 'IT', '185000', 'Framework For Python')]>
        for i in course:
            depart = i[2]
            course = i[1]
        userid = user[0]
        Enquiry.objects.all().filter(id=userid).update(Department=depart,course=course,enrl_status="Enrolled")
        return render(request,'studentlogin.html',{"msg":"Enrollment Successful"})
        
    else:
        course = Courses.objects.filter(id=id).values()
        return render(request,'enroll.html',{"course":course,})

def admsn_mang(request):
    x= datetime.datetime.now()
    x = x.strftime("%x")
    enqries = Enquiry.objects.all().filter(date=x)
    allenqries = Enquiry.objects.all()
    return render(request,'enquries.html',{"enqries":enqries,"allenqries":allenqries})


# Student Login

def std_lgn(request):
    if request.method =="POST":
        email = request.POST['username']
        password = request.POST['password']
        user = Enquiry.objects.all().filter(email=email).values_list()
        for i in user:
            if email in i and password in i:
                user = Enquiry.objects.all().filter(email=email).values()
                data = {
                    "user":user,
                    "email":email,
                }
                return render(request,'studenthomepage.html',data)
        return render(request,'studentlogin.html',{"msg":"Invalid Credentials"})
    else:
        return render(request,'studentlogin.html')


from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

def dwn_atten(request,email):
    # creating Bytestream buffer
    buf = io.BytesIO()
    c = canvas.Canvas(buf,pagesize=letter,bottomup=0)
    # creatriung text oibject what to put in canvas
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica",12)

    lines = []
    print(email)
    att = Attendence.objects.filter(email=email)
    if att:
        for a in att:
            lines.append(f'{a.date}\n{a.status}\n\n')

    else:
        return HttpResponse("ERROR")
    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf,as_attachment=True,filename='attendence.pdf')

def upgrade(request):
    courses = Courses.objects.all().values()
    data ={
        "courses":courses
    }
    return render(request,'upgrade.html',data)


def upgrade_course(request,department,email):
    courses = Courses.objects.all().filter(department = department).values()
    data ={
        "courses":courses,
        "email":email,
    }
    return render(request,"upgrade.html",data)
# def add_course(request,id,email): 
def add_course(request, id, email): 
    append_course = Enquiry.objects.filter(email=email)
    crs = Courses.objects.filter(id=id).values('coursename').first()
    for enquiry in append_course:
        enquiry.course += str(" ")+crs['coursename']
        enquiry.save()    
    course = Enquiry.objects.filter(email=email)
    user = Enquiry.objects.all().filter(email=email).values()
    data = {
    "user":user,
    "email":email,
    }
    return render(request,'studenthomepage.html',data)

def attendence(request,department):
    students = Enquiry.objects.all().filter(Department=department)
    data = {
        "students" : students,
    }
    return render(request,'attendence.html',data)

def add_attend(request,id):
    if request.method == "POST":
        form = AttendenceForm(request.POST)
        try :
            if form.is_valid():
                form.save()
                student = Enquiry.objects.all().filter(id=id).values_list('Department')
                for std in student:
                    department = std[0]
                students = Enquiry.objects.all().filter(Department=department)
                data = {
                    "students":students,
                }
                return render(request,'attendence.html',data)
            else:  
                pass
        except Exception as e:
            pass
    else:
        date = datetime.datetime.now()
        date = date.strftime("%x")
        student = Enquiry.objects.all().filter(id=id)
        data = {
            'student':student,
            'date':date,
        }
        return render(request,'addattendence.html',data)
    

def down_all_enq(request):
    enquries = Enquiry.objects.all().values_list()
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename="allenquries.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name','Email','Contact','Address','Education','Date Of Joining','Department','Collage Name','Reference','Enrollment Status','Course'])
    for enq in enquries:
        writer.writerow([enq[1],enq[2],enq[5],enq[4],enq[6],enq[7],enq[8],enq[10],enq[11],enq[12],enq[13]])
    return response

def down_tod_enq(request):
    x= datetime.datetime.now()
    x = x.strftime("%x")
    enquries = Enquiry.objects.all().filter(date=x).values_list()
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename="allenquries.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name','Email','Contact','Address','Education','Date Of Joining','Department','Collage Name','Reference','Enrollment Status','Course'])
    for enq in enquries:
        writer.writerow([enq[1],enq[2],enq[5],enq[4],enq[6],enq[7],enq[8],enq[10],enq[11],enq[12],enq[13]])
    return response



# ToDo
def fetchingdata():
    listdata = ToDO.objects.all().values()
    context = {
                "listdata":listdata,
            }
    return context

def fetchingdata_filter(id):
    listdata = ToDO.objects.all().filter(id=id)
    context = {
                "listdata":listdata,
            }
    return context

def delete_data(id):
    task = ToDO.objects.all().filter(id=id)
    task.delete()

def todo(request):
    if request.method == "POST":
        form = ToDoForms(request.POST)
        if form.is_valid():
            form.save()            
            return render(request,'todo.html',fetchingdata())
    else:
        return render(request,'todo.html',fetchingdata())
    
def edit_todo(request,id):
    if request.method == "POST":
        user = ToDO.objects.all().get(id=id)
        form = ToDoForms(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return render(request,'todo.html',fetchingdata())
    else:
        return render(request,'edit_todo.html',fetchingdata_filter(id))
    
def delete_todo(request,id):
    delete_data(id)
    return render(request,'todo.html',fetchingdata())