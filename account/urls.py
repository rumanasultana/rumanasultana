from django.contrib import admin
from django.urls import path
from account import views
admin.site.site_header = "CDC ADMIN"
admin.site.site_title = "CDC ADMIN"
admin.site.index_title = "CDC ADMIN"

urlpatterns = [
    path('', views.index,name='home'),
    path('home/', views.index,name='home'),
    path('computer/', views.computer,name='computer'),
    path('electronics/', views.electronics,name='electronics'),
    path('electrical/', views.electrical,name='electrical'),
    path('mechanical/', views.mechanical,name='mechanical'),
    path('civil/', views.civil,name='civil'),
    path('basic_science/', views.basic_science,name='basic_science'),
    path('CareerDevelopmentCell/', views.CareerDevelopmentCell,name='CareerDevelopmentCell'),
    path('admission/', views.admission,name='admission'),
    path('placement', views.placement,name='placement'),
    path('single/', views.single,name='single'),
    path('single1/', views.single1,name='single1'),
    path('single2/', views.single2,name='single2'),
    path('single3/', views.single3,name='single3'),
    
    path('contact/', views.contact,name='contact'),
    path('login/', views.login,name='login'),
    path('signup/', views.signup,name='signup'),


    path('', views.signin, name='signin'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),



   
    path('addnews/', views.addnews, name='addnews'),
    path('allnews/', views.allnews, name='allnews'),
    path('newsdetails/<int:pk>/', views.newsdetails, name='newsdetails'),
    path('editnews/<int:pk>/', views.editnews, name='editnews'),
    path('deletenews/<int:pk>/', views.deletenews, name='deletenews'),
    path('detailsnews/<int:pk>/', views.detailsnews, name='detailsnews'),
    
]

    
