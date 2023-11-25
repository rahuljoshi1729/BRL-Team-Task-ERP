from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('register/',register.as_view(),name='register'),
    path('dataeditor/',dataeditor.as_view(),name='dataeditor'),
    path('facultyeditor/',facultyeditor.as_view(),name='faculty_data'),
    path('subjecteditor/',subjecteditor.as_view(),name='dataeditor'),
    path('attendanceeditor/',attendanceeditor.as_view(),name='dataeditor'),
    path('classassign/',classassignview.as_view(),name='classassign'),
    path("verifyotp/",VerifyOTP.as_view(),name="verifyotp"),
    path("passwordreset/",PasswordResetRequest.as_view(),name="passwordresetrequest"),
    path("password/reset/<str:token>/",PasswordReset.as_view(),name="passwordreset"),
    path("attendance/",Attendanceview,name="attendance"),]
    