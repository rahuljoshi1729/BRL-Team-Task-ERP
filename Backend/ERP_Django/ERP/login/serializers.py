
from rest_framework import serializers
from  .models import *

class LoginSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    password = serializers.CharField(write_only=True)


class UserSerialiazer(serializers.ModelSerializer):
    class Meta:
        model=LoginUser
        fields=['user_id','password','is_verified']

class dataeditorserializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['user_id','first_name','last_name','admission_date','email','aadhar','phone_number','role','Branch','Year','semester','section','password','religion','dob']        

    
class VerifyOTPSerializer(serializers.Serializer):
    otp = serializers.IntegerField()
    email = serializers.EmailField()

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()    


class PasswordtakingSerializer(serializers.Serializer):
    password=serializers.CharField(write_only=True)
    confirm_password=serializers.CharField(write_only=True)

class subjecteditorserializer(serializers.ModelSerializer):
    class Meta:
        model=Subjects
        fields=['name','code','semester']


class attendenceeditorserializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields=['date','student_id','subject','is_present']

class facultyeditorserializer(serializers.ModelSerializer):
    class Meta:
        model=Faculty
        fields=['user_id','first_name','last_name','email','phone_number','role','Post','Department','password','aadhar','address','gender']   

class classassignserializer(serializers.ModelSerializer):
    class Meta:
        model=classassigned
        fields=['subject_code','faculty','semester','class_assigned']        

