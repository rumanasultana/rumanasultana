from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from .decorator import *
from django.core.exceptions import PermissionDenied
from datetime import datetime
from datetime import date
 
# Create your views here.
from math import ceil

global approvednews
global filterdnews

def approvednews(limit=500):# index page
    print(limit)
    allnews = News.objects.all().order_by('-postedtime')[:limit]
    print(allnews)
    allValue = []
    if allnews is not None:
        for ND in allnews:
            if ND.status:
                allValue.append({
                    "id": ND.id,
                    "headlines": ND.headlines,
                    "details": ND.details,
                    'dept': ND.dept,
                    'owner': ND.owner,
                    'img': ND.img,
                    "postedtime": ND.postedtime
                })

            else:
                allValue
    else:
        allValue

    return allValue


def filterdnews(queryfilter):
    allnews = News.objects.filter(dept=queryfilter).order_by('-postedtime') 
    allValue = []
    if allnews is not None:
        for ND in allnews:
            if ND.status:
                allValue.append({
                    "id": ND.id,
                    "headlines": ND.headlines,
                    "details": ND.details,
                    'dept': ND.dept,
                    'owner': ND.owner,
                    'img': ND.img,
                    "postedtime": ND.postedtime
                })

            else:
                allValue
    else:
        allValue

    return allValue

def index(request):
     # allnews=News.objects.all().order_by('-postedtime') [:12] # this is for Slide
    allnews = approvednews(16)
    print(allnews)
    n = len(allnews)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    params = {'no_of_slides': nSlides, 'range': range(
        0, nSlides), 'allnews': allnews}

    #FourNews = News.objects.all().order_by('-postedtime')[:4]
    FourNews=approvednews(4)

    TwoNews = approvednews(2)
    
    OneNews = approvednews(1)

    SevenNews = approvednews(7)

    context = {"allnews": allnews, "TwoNews": TwoNews,
               "SevenNews": SevenNews, 'FourNews': FourNews, 'params': params , " OneNews" : OneNews}
    return render(request, 'site/index.html', context)

 

  
def computer(request):
    #cse=News.objects.filter(dept='ComputerScience').order_by('postedtime')
    try:
        newsdetails = News.objects.filter(dept='ComputerScience').order_by('postedtime')
    except News.DoesNotExist:
        newsdetails = None
    computer = [] 
    if newsdetails is not None:
        for ND in newsdetails:
            if ND.status:
                 computer.append({
                "id": ND.id,
                "headlines": ND.headlines,
                "details": ND.details,
                'dept': ND.dept,
                'owner': ND.owner,
                'img':ND.img,
                "postedtime": ND.postedtime,

            })
            else:
                computer
    else:
        computer
    context={'computer':computer}  
    return render(request,'site/computer.html',context)



def electronics(request):
     #cse=News.objects.filter(dept='ComputerScience').order_by('postedtime')
    try:
        newsdetails = News.objects.filter(dept='Electronics&Communication').order_by('postedtime')
    except News.DoesNotExist:
        newsdetails = None
    electronics = [] 
    if newsdetails is not None:
        for ND in newsdetails:
            if ND.status:
                 electronics .append({
                "id": ND.id,
                "headlines": ND.headlines,
                "details": ND.details,
                'dept': ND.dept,
                'owner': ND.owner,
                'img':ND.img,
                "postedtime": ND.postedtime,

            })
            else:
                electronics 
    else:
        electronics 
    context={'electronics ':electronics }  
    return render(request,'site/electronics.html',context)



def electrical(request):
    #cse=News.objects.filter(dept='ComputerScience').order_by('postedtime')
    try:
        newsdetails = News.objects.filter(dept='Electrical').order_by('postedtime')
    except News.DoesNotExist:
        newsdetails = None
    electrical = [] 
    if newsdetails is not None:
        for ND in newsdetails:
            if ND.status:
                 electrical .append({
                "id": ND.id,
                "headlines": ND.headlines,
                "details": ND.details,
                'dept': ND.dept,
                'owner': ND.owner,
                'img':ND.img,
                "postedtime": ND.postedtime,

            })
            else:
                electrical
    else:
        electrical
    context={'electrical':electrical }
    return render(request,'site/electrical.html',context)



def  mechanical(request):
    
    mechanical=filterdnews('Mechanical')
    context = { "Mechanical" : mechanical}
    return render(request, 'site/mechanical.html', context)


def civil(request):
     #cse=News.objects.filter(dept='ComputerScience').order_by('postedtime')
    try:
        newsdetails = News.objects.filter(dept='Civil').order_by('postedtime')
    except News.DoesNotExist:
        newsdetails = None
    civil = [] 
    if newsdetails is not None:
        for ND in newsdetails:
            if ND.status:
                 civil .append({
                "id": ND.id,
                "headlines": ND.headlines,
                "details": ND.details,
                'dept': ND.dept,
                'owner': ND.owner,
                'img':ND.img,
                "postedtime": ND.postedtime,

            })
            else:
               civil
    else:
        civil
    context={'civil ':civil }
    return render(request,'site/civil.html',context)



def basic_science(request):
    return render(request,'site/basic_science.html')


 
def CareerDevelopmentCell(request):
    FourNews = approvednews(4)
    CareerDevelopmentCell=filterdnews('CareerDevelopmentCell')
    context = { "FourNews": FourNews, 'CareerDevelopmentCell': CareerDevelopmentCell}
    return render(request, 'site/CareerDevelopmentCell.html', context)


    


def  admission(request):
    FourNews = approvednews(4)
    admission=filterdnews('admission')
    context = {"FourNews": FourNews,"admission" : admission}
    return render(request, 'site/admission.html', context)

def placement(request):
    FourNews = approvednews(4)
    placement=filterdnews('placement')
    context = {"FourNews": FourNews,'placement': placement}
    return render(request, 'site/placement.html', context)
   
 
def video(request):
    FourNews = approvednews(4)
    context = {"FourNews": FourNews }
    return render(request,'site/video.html', context)
 
def event(request):
    FourNews = approvednews(4)
    context = {"FourNews": FourNews }
    return render(request,'site/event.html', context)

def single(request):
    FourNews = approvednews(4)
    context = {"FourNews": FourNews }
    return render(request,'site/single.html' , context)
def single1(request):
    FourNews = approvednews(4)
    context = {"FourNews": FourNews }
    return render(request,'site/single1.html', context)

def single2(request):
    FourNews = approvednews(4)
    context = {"FourNews": FourNews }
    return render(request,'site/single2.html', context)
def single3(request):
    FourNews = approvednews(4)
    context = {"FourNews": FourNews }
    return render(request,'site/single3.html', context)


def contact(request):
    return render(request, 'site/contact.html')

def detailsnews(request,pk):
    detailsnews=News.objects.get(pk=pk)
    user = User.objects.get(pk=detailsnews.owner)
    author = user.first_name + ' ' + user.last_name
    authorimg = user.profilepic.url

    url=''
    if detailsnews.dept=='Civil':
        url='civil'
    elif detailsnews.dept=='Electrical':
         url='electrical'
    elif detailsnews.dept=='Mechanical':
         url='mechanical'
    elif detailsnews.dept=='Electronics':
         url='electronics'
    elif detailsnews.dept=='ComputerScience':
         url='computer'
    
    elif detailsnews.dept=='CDC':
         url='CareerDevelopmentCell'
    elif detailsnews.dept=='Placement':
         url='placement' 
    elif detailsnews.dept=='Event':
         url='event'     
    else: 
        url="home"
           
    context = {'detailsnews':detailsnews,'page':url,'author':author,'authorimg':authorimg}
    return render(request, 'site/detailsnews.html', context)




@OnlyAuth
def signin(request):
    LM = LoginForm(request.POST or None)
    if request.method == 'POST':
        if LM.is_valid():
            UserName = request.POST.get('username')
            PassWord = request.POST.get('password')
            user = authenticate(request, username=UserName, password=PassWord)

            if user is not None and user.is_cdc:
                login(request, user)
                return redirect('cdc')
            elif user is not None and user.is_teacher:
                login(request, user)
                return redirect('teacher')
            elif user is not None and user.is_student:
                login(request, user)
                return redirect('student')
            else:
                messages.error(request, 'Username or Password is incorrect')
        else:
            messages.error(request, LM.errors)
    else:
        LM = LoginForm()
    context = {'form': LM}
    return render(request, 'common/signin.html', context)


@OnlyAuth
def signup(request):
    if request.method == 'POST':
        SF = SignupForm(request.POST)
        if SF.is_valid():
            isStudent = SF.cleaned_data.get('is_student')
            isTeacher = SF.cleaned_data.get('is_teacher')
            if isStudent:
                SignUpUser = SF.save(commit=False)
                SignUpUser.is_student = True
                SignUpUser.status = True
                SignUpUser.save()
            elif isTeacher:
                SignUpUser = SF.save(commit=False)
                SignUpUser.is_teacher = True
                SignUpUser.status = False
                SignUpUser.save()
            else:
                messages.warning(request, 'Please Select Your user Type')
                return redirect('signin')
            user = SF.cleaned_data.get('username')
            messages.success(request, 'Account Created for ' + user)
            return redirect('signin')
        else:
            messages.error(request, SF.errors)
    else:
        SF = SignupForm()
    context = {'form': SF}
    return render(request, 'common/signup.html', context)


@login_required(login_url='signin')
def signout(request):
    logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def cdc(request):
    if not request.user.is_cdc:
        raise PermissionDenied
    return render(request, 'admin/CdcProfile.html')

@login_required(login_url='signin')
def student(request):
   
    if not request.user.status:
        return render(request, 'common/notActive.html')

    userdata = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        UserProfileForm = SignupForm(
            request.POST, request.FILES, instance=userdata)

        if UserProfileForm.is_valid():
            student = UserProfileForm.save(commit=False)
            student.is_student = True
            student.status = True
            UserProfileForm.save()
            messages.success(
                request, 'Profile is Updated. please login again to craete a new Session')
            return redirect('signout')
        else:
            messages.warning(request, UserProfileForm.errors)
    else:
        UserProfileForm = SignupForm(instance=userdata)
    context = {'StudentData': userdata, 'UserProfileForm': UserProfileForm}
    return render(request, 'student/StudentProfile.html', context)


@login_required(login_url='signin')
def addnews(request):
    if not request.user.status:
        return render(request, 'common/notActive.html')

    userdata = User.objects.get(pk=request.user.id)

    try:
        newsdetails = News.objects.all()
    except News.DoesNotExist:
        newsdetails = None

    AllNews = []
    if newsdetails is not None:
        for ND in newsdetails:
            user = User.objects.get(pk=ND.owner)
            if user is not None:
                author = user.first_name + ' ' + user.last_name
                img = user.profilepic.url
            else:
                author = ""

            AllNews.append({
                "id": ND.id,
                "headlines": ND.headlines,
                "details": ND.details,
                'dept': ND.dept,
                 
                'owner': ND.owner,
                'ownername': author,
                'ownerimg': img,
                "postedtime": ND.postedtime,
            })

    if request.method == 'POST':
        NewsForm = NewsManagement(request.POST, request.FILES)
        if NewsForm.is_valid():
            news = NewsForm.save(commit=False)
            news.status = False
            news.owner = request.user.id
            news.postedtime = date.today()
            news.save()
            messages.success(
                request, 'Your News Details is submited and wait for CDC process')
            return redirect('allnews')
        else:
            messages.warning(request, NewsForm.errors)

    else:
        NewsForm = NewsManagement()

    context = {'StudentData': userdata, 'NewsData': newsdetails,
               'NewsForm': NewsForm}
    return render(request, 'news/addnews.html', context)


@login_required(login_url='signin')
def allnews(request):
    if not request.user.status:
        return render(request, 'common/notActive.html')

    userdata = User.objects.get(pk=request.user.id)
    try:
        newsdetails = News.objects.all()
    except News.DoesNotExist:
        newsdetails = None

    AllNews = []
    if newsdetails is not None:
        for ND in newsdetails:
            user = User.objects.get(pk=ND.owner)
            if user is not None:
                author = user.first_name + ' ' + user.last_name
                img = user.profilepic.url
            else:
                author = ""
              
            print(author)
              
            AllNews.append({
                "id": ND.id,
                "headlines": ND.headlines,
                "details": ND.details,
                'dept': ND.dept,
                'owner': ND.owner,
                'ownername': author,
                'ownerimg': img,
                "postedtime": ND.postedtime
            })
    context = {'StudentData': userdata, 'NewsData': AllNews}
    return render(request, 'news/Allnews.html', context)


@login_required(login_url='signin')
def editnews(request, pk):
    if not request.user.status:
        return render(request, 'common/notActive.html')

    userdata = User.objects.get(pk=request.user.id)
    newsdetails = News.objects.get(pk=pk)

    if request.method == 'POST':
        NewsForm = NewsManagement(
            request.POST, request.FILES, instance=newsdetails)
        if NewsForm.is_valid():
            news = NewsForm.save(commit=False)
            news.status = False
            news.owner = request.user.id
            news.postedtime = date.today()
            news.save()
            messages.success(
                request, 'Your News Details is submited')
            return redirect('allnews')
        else:
            messages.warning(request, NewsForm.errors)
    else:
        NewsForm = NewsManagement(instance=newsdetails)

    context = {'StudentData': userdata, 'NewsForm': NewsForm}
    return render(request, 'news/editnews.html', context)


@login_required(login_url='signin')
def deletenews(request, pk):
    if not request.user.status:
        return render(request, 'common/notActive.html')
    if request.method == 'POST':
        target_data = News.objects.get(pk=pk)
        target_data.delete()
        messages.success(request, 'This News deleted')
        return redirect('allnews')
        
def newsdetails(request,pk):
    if not request.user.status:
        return render(request, 'common/notActive.html')

    userdata = User.objects.get(pk=request.user.id)
    try:
        newsdetails = News.objects.get(pk=pk)
    except News.DoesNotExist:
        newsdetails = None
     
    newsowner= User.objects.get(pk=newsdetails.owner)  
        

    
    context = {'StudentData': userdata, 'NewsData': newsdetails,'newsowner':newsowner}
    return render(request, 'news/newsdetails.html', context)



@login_required(login_url='signin')
def teacher(request):
    if not request.user.is_teacher:
        raise PermissionDenied
    if not request.user.status:
        return render(request, 'common/notActive.html')
    userdata = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        UserProfileForm = SignupForm(
            request.POST, request.FILES, instance=userdata)

        if UserProfileForm.is_valid():
            student = UserProfileForm.save(commit=False)
            student.is_teacher = True
            student.status = True
            UserProfileForm.save()
            messages.success(
                request, 'Profile is Updated. please login again to craete a new Session')
            return redirect('signout')
        else:
            messages.warning(request, UserProfileForm.errors)
    else:
        UserProfileForm = SignupForm(instance=userdata)
    context = {'StudentData': userdata, 'UserProfileForm': UserProfileForm}
    return render(request, 'teacher/TeacherProfile.html', context)


def allstudent(request):
    if not request.user.is_teacher:
        raise PermissionDenied
    if not request.user.status:
        return render(request, 'common/notActive.html')

    userdata = User.objects.get(pk=request.user.id)
    studentdata = User.objects.all()
    allstudent = []

    for i in studentdata:
        if i.is_student == True:
            allstudent.append({
                "id": i.id,
                "first_name": i.first_name,
                "last_name": i.last_name,
                'dept': i.dept,
                'year': i.year,
                'semester': i.semester,
                'enrollment': i.enrollment,
                'profilepic': i.profilepic,
            })

    context = {'StudentData': userdata, 'allstudent': allstudent}
    return render(request, 'teacher/allstudent.html', context)

# for teacher only










