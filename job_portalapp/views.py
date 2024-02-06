from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import *
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request,'index.html')
def admin_login(request):
    return render(request,'admin_login.html')
def admin_login_check(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(username,password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/adminhome/")
        else:
            return redirect("/admin_login/")

def adminhome(request):
    return render(request,'adminhome.html')
def addvacancy(request):
    data=tbl_category.objects.all()
    return render(request,'addvacancy.html',{"data":data})

def save_vacancy_first(request):
    if request.method=="POST":
        data=tbl_jobpost()
        data.company_id=request.session["cmpid"]
        data.category_id=request.POST.get("job_category")
        data.jobtitle=request.POST.get("jobtitle")
        data.address=request.POST.get("address")
        data.jobtype=request.POST.get("jobtype")
        data.save()
        return redirect("job_vacancy_second",id=data.id)
def job_vacancy_second(request,id):
    data=tbl_jobpost.objects.get(id=id)
    return render(request,"job_vacancy_second.html",{"data":data})
def save_vacancy_second(request,id):
    if request.method=="POST":
        data=tbl_jobpost.objects.get(id=id)
        data.schedule=request.POST.get("schedule")
        data.experiencelevel=request.POST.get("experiencelevel")
        data.numberofopening = request.POST.get("numberofopening")
        data.hiringtimeline = request.POST.get("hiringtimeline")
        data.save()
        return redirect("job_vacancy_fourth", id=data.id)



def job_vacancy_fourth(request,id):
    data = tbl_jobpost.objects.get(id=id)
    return render(request,"job_vacancy_fourth.html",{"data":data})



def save_vacancy_fourth(request,id):
    data = tbl_jobpost.objects.get(id=id)
    data.minimum = request.POST.get("minimum")
    data.maximum = request.POST.get("maximum")
    data.rate = request.POST.get("rate")
    data.save()
    return redirect("job_vacancy_fifth", id=data.id)


def job_vacancy_fifth(request,id):
    data = tbl_jobpost.objects.get(id=id)
    return render(request, "job_vacancy_fifth.html", {"data": data})

def save_vacancy_fifth(request,id):
    data = tbl_jobpost.objects.get(id=id)
    data.jobdescription = request.POST.get("job_description")
    data.save()
    return redirect("job_vacancy_sixth", id=data.id)
def job_vacancy_sixth(request,id):
    data = tbl_jobpost.objects.get(id=id)
    return render(request, "job_vacancy_sixth.html", {"data": data})


def save_vacancy_sixth(request,id):
    data = tbl_jobpost.objects.get(id=id)
    sk=request.POST.getlist("skill[]")
    type=request.POST.getlist("type[]")
    f=zip(sk,type)
    for i,j in f:
        t=tbl_skills()
        t.jobid=data.id
        t.skills=i
        t.type=j
        t.save()
    return redirect("/viewvacancy/")

def job_vacancy_seventh(request,id):
    data = tbl_jobpost.objects.get(id=id)
    return render(request, "job_vacancy_seventh.html", {"data": data})

def  addcategory(request):
    return render(request,"addcategory.html")


def save_category(request):
    d=tbl_category()
    d.categoryname=request.POST.get("category")
    d.categorystatus=request.POST.get("status")
    d.save()
    return redirect("/addcategory/")

def viewcategory(request):
    d=tbl_category.objects.all()
    return render(request,"viewcategory.html",{"d":d})


def addcompany(request):
    return render(request,"addcompany.html")

def save_company(request):
    g=tbl_company()
    g.identificationno=request.POST.get("identificationno")
    g.company_name=request.POST.get("company_name")
    g.description=request.POST.get("description")
    g.address =request.POST.get("address")
    g.city=request.POST.get("city")
    g.state=request.POST.get("state")
    g.country=request.POST.get("country")
    g.postalcode=request.POST.get("postalcode")
    g.owner=request.POST.get("owner")
    g.nominal_capital=request.POST.get("nominal_capital")
    g.industry=request.POST.get("industry")
    g.mobileno=request.POST.get("mobileno")
    g.email=request.POST.get("email")
    g.website=request.POST.get("website")
    g.username=request.POST.get("username")
    g.password =request.POST.get("password")
    companyimage = request.FILES["image"]
    fs=FileSystemStorage()
    filename=fs.save(companyimage.name,companyimage)
    fu=fs.url(filename)
    g.companyimage=fu
    g.save()
    return redirect("/addcompany/")
def viewcompany(request):
    d=tbl_company.objects.all()
    return render(request,"viewcompany.html",{"d":d})


def cmp_more_info(request,id):
    d=tbl_company.objects.get(id=id)
    return render(request,"cmp_more_info.html",{"d":d})

def company_login(request):
    return render(request,"company_login.html")

def company_request(request):
    return render(request,"company_request.html")

def save_cmp_request(request):
    d=tbl_company()
    d.company_name=request.POST.get("company_name")
    d.email=request.POST.get("email")
    d.owner=request.POST.get("owner")
    d.website=request.POST.get("website")
    d.mobileno=request.POST.get("mobile")
    d.status="Requested"
    d.save()
    messages.success(request,"Your confirmation mail and login credentials will send soon..")
    return redirect("/company_login/")

def view_req_cmp(request):
    data=tbl_company.objects.filter(status="Requested")
    return render(request,"view_req_cmp.html",{"data":data})

def request_approval(request,id):
    d=tbl_company.objects.get(id=id)
    return render(request,"request_approval.html",{"d":d})

def save_approval(request,id):
    username = request.POST.get("username")
    password = request.POST.get("password")
    d=tbl_company.objects.get(id=id)
    d.status="Approved"
    d.username=username
    d.password=password
    d.save()

    # message="Username:"+username +"<br>"+"password:"+password
    # send_mail("Confirmation",message,settings.EMAIL_HOST_USER,[d.email])
    return redirect("/view_req_cmp/")

def create_mock(request):
    d=tbl_category.objects.all()
    return render(request,"create_mock.html",{"d":d})

def save_mockqns(request):
    level = request.POST.get("level")
    category= request.POST.get("category")
    if tbl_Mock.objects.filter(level=level,category=category).exists():
        g=tbl_Mock.objects.get(level=level,category=category)
        g.level = request.POST.get("level")
        g.category_id = request.POST.get("category")
        g.save()
    else:
        g=tbl_Mock()
        g.level=request.POST.get("level")
        g.category_id=request.POST.get("category")
        g.save()

    ans=request.POST.getlist("answer[]")
    qns=request.POST.getlist("question[]")
    print(ans,"ans")
    print("nnnnnnnnnnnnnnnn")
    print(qns,"qnss")


    choice1=request.POST.getlist("choice1[]")
    choice2 = request.POST.getlist("choice2[]")
    choice3 = request.POST.getlist("choice3[]")
    choice4 = request.POST.getlist("choice4[]")
    mark= request.POST.getlist("mark[]")
    print(choice4,"choice4")
    print(choice3, "choice3")
    print(choice2, "choice2")
    print(choice1, "choice1")
    zip1 = zip(qns, ans,choice1,choice2,choice3,choice4,mark)

    for i,j,k,l,m,n,o in zip1:
        t = tbl_QuestionAnswer()
        t.mock_id=g.id
        t.question=i
        t.answer=j
        t.choice1=k
        t.choice2=l
        t.choice3=m
        t.choice4=n
        t.mark=o
        t.save()
    return redirect("/view_mock/")

def company_login_check(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    if tbl_company.objects.filter(username=username,password=password,status="Approved").exists():
        d=tbl_company.objects.get(username=username,password=password,status="Approved")
        request.session["cmpid"]=d.id
        return redirect("/company_home/")
    else:
        return redirect("/company_login/")

def company_home(request):
    return render(request,"company_home.html")

def viewvacancy(request):
    d=tbl_jobpost.objects.filter(company=request.session["cmpid"])
    return render(request,"viewvacancy.html",{"d":d})

def vacancy_more_info(request,id):
    d=tbl_jobpost.objects.get(id=id)
    d1=tbl_skills.objects.filter(jobid=id)
    return render(request,"vacancy_more_info.html",{"d":d,"d1":d1})
def user_login(request):
    return render(request,"user_login.html")

def user_register(request):
    return render(request,"user_register.html")

def save_register(request):
    f=tbl_Register()
    f.name=request.POST.get("name")
    f.email = request.POST.get("email")
    f.mobile = request.POST.get("mobile")
    f.username = request.POST.get("username")
    f.password = request.POST.get("password")
    f.save()
    return redirect("/user_login/")


def user_login_check(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    if tbl_Register.objects.filter(username=username,password=password).exists():
        f=tbl_Register.objects.get(username=username,password=password)
        request.session["uid"]=f.id
        return redirect("/user_home/")
    else:
        return redirect("/user_login/")

def user_home(request):
    return render(request,"user_home.html")

def user_view_jobs(request):
    data=tbl_jobpost.objects.all()
    return render(request,"user_view_jobs.html",{"data":data})

def view_more_job_user(request,id):
    data=tbl_jobpost.objects.get(id=id)
    data1=tbl_skills.objects.filter(jobid=id)
    return render(request,"view_more_job_user.html",{"d":data,"d1":data1})

def apply_job(request,id):
    if tbl_JobApplication.objects.filter(jobid=id,userid=request.session['uid']).exists():
        messages.error(request,"You have Already applied to this job")
        return redirect("/user_view_jobs/")
    else:
        d=tbl_jobpost.objects.get(id=id)
        return render(request,"apply_job.html",{"d":d})

def save_job_application(request,id):
    d1= tbl_jobpost.objects.get(id=id)
    d=tbl_JobApplication()
    d.company_id=d1.company.id
    d.jobid_id=id
    d.userid_id=request.session['uid']
    d.full_name=request.POST.get("fullname")
    d.resume=request.FILES['resume']
    d.email=request.POST.get("email")
    d.cover_letter=request.POST.get("cover_letter")
    d.status="Requested"
    d.save()
    return redirect("/my_applications/")

def my_applications(request):
    d=tbl_JobApplication.objects.filter(userid=request.session["uid"])
    return render(request,"my_applications.html",{"d":d})

def user_mock(request):
    f=tbl_category.objects.all()
    return render(request,"user_mock.html",{"f":f})

def search_mock(request):
    level=request.POST.get("level")
    category=request.POST.get("category")
    g=tbl_Mock.objects.get(level=level,category=category)
    b=tbl_QuestionAnswer.objects.filter(mock=g.id)
    f = tbl_category.objects.all()
    return render(request,"user_mock.html",{"b":b,"f":f,"level":level,"category":category})

def save_mock_answers(request):
    cat=request.POST.get("category")
    cat1 = tbl_category.objects.get(id=cat)
    level=request.POST.get("level")
    t=tbl_Mock_User()
    t.userid_id=request.session["uid"]
    t.level=level
    t.category=cat1.categoryname
    t.save()

    questions=[]
    num_questions = (len(request.POST) - 2) // 5
    print(num_questions)
    f=tbl_Mock.objects.get(category=cat1,level=level)
    f1=tbl_QuestionAnswer.objects.filter(mock=f.id).count()


    for i in range(1, f1 + 1):
        question_text = request.POST.get(f"question{i}")
        selected_choice = request.POST.get(f"choice{i}")
        r=tbl_QuestionAnswer.objects.get(question=question_text)

        questions.append({
            'question': question_text,
            'choice': selected_choice,
            'answer':r.answer,
        })
    print(questions)
    for i in questions:
        g=tbl_Mock_Answers()
        g.mock_user_id=t.id
        g.question=i["question"]
        g.selected_answer=i["choice"]
        g.Correct_answer=i["answer"]
        g.user_id=request.session["uid"]
        g.save()
    return redirect("/mock_result/")

def mock_result(request):
    d=tbl_Mock_User.objects.filter(userid=request.session["uid"])
    return render(request,"mock_result.html",{"d":d})


def view_applications(request):
    d=tbl_JobApplication.objects.filter(company=request.session['cmpid'])
    return render(request,"view_applications.html",{"d":d})

def cmp_shortlist(request,id):
    d=tbl_JobApplication.objects.get(id=id)
    d.status="Shortlisted"
    d.save()
    return redirect("/view_applications/")

def cmp_reject(request,id):
    d=tbl_JobApplication.objects.get(id=id)
    d.status="Rejected"
    d.save()
    return redirect("/view_applications/")

