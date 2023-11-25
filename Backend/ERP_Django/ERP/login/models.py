from django.db import models

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


#creating an base user
class UserManager(BaseUserManager):
    def create_user(self,id,password=None,**extra_fields):
        if not id:
            raise ValueError('the id filed must be set')
        if not password:
            raise ValueError('set password')
        user=self.model(id=id,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
#creating an super user

    def create_superuser(self,id,password=None,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("speruser must have is_staff=true.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("superuser must have is_superuser=True")
        
        return self.create_user(id,password,**extra_fields)
    

#creating a login database   
class LoginUser(AbstractBaseUser):
    user_id=models.IntegerField(unique=True)
    password=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    otp=models.IntegerField(null=True,blank=True)

    objects=UserManager
    USERNAME_FIELD='id'
    REQUIRED_FIELDS=[id]

    def __str__(self):
        return self.id



class Student(models.Model):
    user_id=models.IntegerField(unique=True,primary_key=True)
    password=models.CharField(max_length=100,default='1234')
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    admission_date=models.DateField(auto_now_add=True,blank=True,null=True)
    email=models.EmailField(unique=True)
    aadhar=models.CharField(max_length=12,blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    phone_number=models.IntegerField(unique=True)
    profile_photo_url=models.URLField()
    role=models.CharField(max_length=100,default='student')
    Branch=models.CharField(max_length=100)
    Year=models.IntegerField()
    semester=models.IntegerField()
    section=models.CharField(max_length=100)
    religion=models.CharField(max_length=100,blank=True,null=True)
    dob=models.DateField(blank=True,null=True)
    objects=UserManager
    USERNAME_FIELD='user_id'
    REQUIRED_FIELDS=[user_id]

    def __str__(self):
        return self.user_id
    
class Faculty(models.Model):
    user_id=models.IntegerField(unique=True,primary_key=True)
    password=models.CharField(max_length=100,default='1234')
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone_number=models.IntegerField(unique=True)
    profile_photo_url=models.URLField()
    role=models.CharField(max_length=100,default='faculty')
    Post=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    gender=models.CharField(max_length=6,blank=True,null=True)
    aadhar=models.CharField(max_length=12,blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    objects=UserManager
    USERNAME_FIELD='user_id'
    REQUIRED_FIELDS=[user_id]

    def __int__(self):
        return self.user_id  
    

class Subjects(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=20,unique=True,primary_key=True)
    semester=models.IntegerField()
   # staff=models.ForeignKey(Faculty,on_delete=models.CASCADE)    

class Attendance(models.Model):
    subject=models.ForeignKey(Subjects,on_delete=models.CASCADE,related_name='attendance')
    #student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='attendance')
    student_id=models.IntegerField(default=None)
    date=models.DateField(auto_now_add=True)
    is_present=models.BooleanField(null=True,blank=True)    

class classassigned(models.Model):
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE,related_name='classassigned')
    class_assigned=models.CharField(max_length=100,blank=True,null=True)
    semester=models.IntegerField(blank=True,null=True)
    subject_code=models.CharField(max_length=20,blank=True,null=True)
    objects=UserManager
    USERNAME_FIELD='faculty'
    REQUIRED_FIELDS=[faculty]
    def __str__(self):
        return self.faculty  
    

""" 
class AuthModel(models.Model):
    user_id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=100,uniqueblank=
    password=models.CharField(max_length=100)
    email=models.EmailField(default="mohammadanas0544@gmail.com",unique=True)
    choices=(('admin','admin'),('faculty','faculty'),('warden','warden'),('student','student'))
    role=models.CharField(max_length=100,choices=choices)

class StaffProfile(models.Model):
    user=models.ForeignKey(AuthModel,on_delete=models.CASCADE)
    title=models.CharField(max_length=5,blank=True,null=True)
    gender=models.CharField(max_length=6,blank=True,null=True)
    fname=models.CharField(max_length=100,blank=True,null=True)
    lname=models.CharField(max_length=100,blank=True,null=True)
    phone=models.CharField(max_length=10,blank=True,null=True)
    aadhar=models.CharField(max_length=12,blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    profile_url=models.URLField(blank=True,null=True)    """ 