from django.db import models


# Create your models here.

class tbl_category(models.Model):
    categoryname = models.CharField(max_length=100, null=True)
    categorystatus = models.CharField(max_length=100, null=True)


class tbl_company(models.Model):
    identificationno = models.IntegerField(null=True)
    company_name=models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    postalcode = models.CharField(max_length=100, null=True)
    owner = models.CharField(max_length=100, null=True)
    nominal_capital = models.CharField(max_length=100, null=True)
    industry = models.CharField(max_length=100, null=True)
    mobileno = models.IntegerField(null=True)
    email = models.EmailField(max_length=100, null=True)
    companyimage = models.ImageField(null=True, upload_to='media')
    website = models.CharField(max_length=100, null=True)
    username= models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100, null=True)
    status=models.CharField(max_length=10,null=True)


class tbl_jobpost(models.Model):
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE,null=True)
    company = models.ForeignKey(tbl_company, on_delete=models.CASCADE, null=True)
    jobtitle = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    jobtype = models.CharField(max_length=100, null=True)
    schedule = models.CharField(max_length=100, null=True)
    experiencelevel = models.CharField(max_length=100, null=True)
    numberofopening = models.CharField(max_length=100, null=True)
    hiringtimeline = models.DateField(max_length=100, null=True)
    minimum = models.CharField(max_length=100, null=True)
    maximum = models.CharField(max_length=100, null=True)
    rate = models.CharField(max_length=100, null=True)
    jobdescription = models.CharField(max_length=100, null=True)

class tbl_skills(models.Model):
    jobid=models.ForeignKey(tbl_jobpost,on_delete=models.CASCADE,null=True)
    skills = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, null=True)

class tbl_Mock(models.Model):
    level = models.CharField(max_length=20, null=True)
    category = models.ForeignKey(tbl_category,on_delete=models.CASCADE, null=True)



class tbl_QuestionAnswer(models.Model):
    mock = models.ForeignKey(tbl_Mock, on_delete=models.CASCADE,null=True)
    question = models.TextField(null=True)
    answer = models.TextField(null=True)
    choice1=models.CharField(max_length=20, null=True)
    choice2=models.CharField(max_length=20, null=True)
    choice3=models.CharField(max_length=20, null=True)
    choice4=models.CharField(max_length=20, null=True)
    mark=models.CharField(max_length=10,null=True)

class tbl_Register(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class tbl_JobApplication(models.Model):
    company = models.ForeignKey(tbl_company, on_delete=models.CASCADE, null=True)
    userid= models.ForeignKey(tbl_Register,on_delete=models.CASCADE,null=True)
    jobid=models.ForeignKey(tbl_jobpost,on_delete=models.CASCADE,null=True)
    full_name = models.CharField(max_length=255,null=True)
    email = models.EmailField(null=True)
    resume = models.FileField(upload_to='resumes/',null=True)
    cover_letter = models.TextField(null=True)
    status=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.full_name


class tbl_Mock_User(models.Model):
    userid= models.ForeignKey(tbl_Register,on_delete=models.CASCADE,null=True)
    level = models.CharField(max_length=20, null=True)
    category = models.CharField(max_length=20, null=True)
    total_mark=models.IntegerField(null=True)
    Result=models.CharField(max_length=20,null=True)
    dt = models.DateField(auto_now_add=True)

class tbl_Mock_Answers(models.Model):
    mock_user = models.ForeignKey(tbl_Mock_User, on_delete=models.CASCADE, null=True)
    question = models.TextField(null=True)
    selected_answer = models.TextField(null=True)
    Correct_answer=models.CharField(null=True,max_length=20)
    dt=models.DateField(auto_now_add=True)
    user = models.ForeignKey(tbl_Register, on_delete=models.CASCADE, null=True)


class tbl_Championship(models.Model):
    name=models.CharField(max_length=100,null=True)
    image=models.ImageField(upload_to="champ",null=True)
    question1=models.TextField(null=True)
    question2 = models.TextField(null=True)
    question3 = models.TextField(null=True)
    dt=models.DateField(auto_now_add=True)

class tbl_Result_Championship(models.Model):
    champ = models.ForeignKey(tbl_Championship,on_delete=models.CASCADE,null=True)
    userid = models.ForeignKey(tbl_Register,on_delete=models.CASCADE,null=True)
    answer1 = models.TextField(null=True)
    answer2 = models.TextField(null=True)
    answer3 = models.TextField(null=True)
    result1 = models.CharField(max_length=30,null=True)
    result2 = models.CharField(max_length=30, null=True)
    result3 = models.CharField(max_length=30, null=True)
    dt = models.DateField(auto_now_add=True)





