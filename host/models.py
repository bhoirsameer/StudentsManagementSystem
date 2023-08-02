from django.db import models

# Create your models here.
class Host(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    class Meta:
        db_table = 'hosttable'
    def __str__(self):
        return f"{self.username}"

class Courses(models.Model):
    coursename = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    fees = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        db_table = 'courses'
    def __str__(self):
        return f"{self.coursename} {self.department}"
    
class Trainers(models.Model):
    name = models.CharField(max_length=55)
    department = models.CharField(max_length=100)
    class Meta:
        db_table = 'trainers'
    def __str__(self):
        return f"{self.name}"

class Trainerslogin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    department = models.CharField(max_length=50,null=True)
    class Meta:
        db_table = 'Trainers_login_table'
    def __str__(self):
        return f"{self.username}"

class Enquiry(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField(max_length=55)
    password = models.CharField(max_length=55,null=True)
    address = models.CharField(max_length=55)
    contact = models.CharField(max_length=55)
    education = models.CharField(max_length=55)
    date = models.CharField(max_length=55)
    Department = models.CharField(max_length=55,null=True)
    adhaarno = models.CharField(max_length=55,null=True)
    clgname = models.CharField(max_length=55,null=True)
    reference = models.CharField(max_length=55,null=True)
    enrl_status = models.CharField(max_length=55,default="NO")
    course = models.CharField(max_length=55,default="Not Enroll Yet")
    class Meta:
        db_table = 'enquiry'
    def __str__(self):
        return f"{self.name}"
    
class Attendence(models.Model):
    roll_no = models.CharField(max_length=55,null=True)
    email = models.CharField(max_length=55,null=True)
    name = models.CharField(max_length=55,null=True)
    date = models.CharField(max_length=55,null=True)
    status = models.CharField(max_length=55,null=True)
    class Meta:
        db_table = "attendence"
    def __str__(self):
        return f"{self.name}"
    

class ToDO(models.Model):
    type = models.CharField(max_length=55)
    date = models.DateField()
    description = models.CharField(max_length=55)
    class Meta:
        db_table = "todo"