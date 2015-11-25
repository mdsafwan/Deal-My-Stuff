from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from login.models import user_details, user_login
from django.utils import timezone
from __builtin__ import True

def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('auth.html',{'state':state, 'username': username}, context_instance=RequestContext(request))

def display_login(request):
    return render(request, "login.html", {})

def after_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print username
    print password
    return HttpResponse("welcome: %s" % request.path)

def login(request):
    if request.COOKIES.get('User_ID'):
        return HttpResponseRedirect('/logged_in/')
    successful_login = True
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        if user_details.objects.filter(User_Name=username, Password=password).exists():    
            successful_login = True
            x = user_details.objects.filter(User_Name=username)
            status = "Logged_In"
            user_login.objects.create(User_ID = x[0],
                                      Logged_In_Time = timezone.now(),
                                      Status = status)
            #print x[0].User_ID
            return HttpResponseRedirect('/home/')
        else:
            successful_login = False
    return render(request, "login.html", {'successful_login' : successful_login})
#return render_to_response('login.html',{}, context_instance=RequestContext(request))


def register(request):
    username_valid = True
    usn_valid = True
    password_match = True
    
    if request.POST:
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        usn = request.POST.get('usn')
        mobile_number = request.POST.get('mobile_number')
        address = request.POST.get('address')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        gcaptcha = request.POST.get('g-recaptcha-response')
        
        if user_details.objects.filter(USN = usn).exists():
            usn_valid = False
            
        if password != confirm_password:
            password_match = False  
        
        if user_details.objects.filter(User_Name = username).exists():
            username_valid = False
            
        if password_match == False or usn_valid == False or username_valid == False:
            return render(request, "register.html", {'password_match' : password_match,
                                                    'usn_valid' : usn_valid,
                                                    'username_valid' : username_valid})
        print gcaptcha
        
        user_id = user_details.objects.values('User_ID').latest('User_ID')
        user_id = user_id['User_ID']
        x = user_id[4:]
        x = int(x) + 1
        user_id = "DMS_" + str(x)
        #user_id = "DMS_1000"
        user_details.objects.create(User_Name = username,
                                    User_ID = user_id,
                                    Name = name,
                                    Email = email,
                                    USN = usn,
                                    Mobile_Number = mobile_number,
                                    Address = address,
                                    Password = password)
        
        return render(request, "registration_success.html", {})
    
    
    return render(request, "register.html", {'password_match' : password_match,
                                             'usn_valid' : usn_valid,
                                             'username_valid' : username_valid})

def logout(request):
    user_id_of_user_logged_in = user_login.objects.last()
    User_ID = user_id_of_user_logged_in.User_ID
    #user_login.objects.latest('id').update(Status="Logged_Out",
    #                                                  Logged_Out_Time=timezone.now())
    obj = user_login.objects.latest('id')
    obj.Status = "Logged_Out"
    obj.Logged_Out_Time = timezone.now()
    obj.save()
    response = render(request, "logout.html", {'User_ID' : User_ID})
    response.delete_cookie("User_ID")
    return response

def login_error(request):
    return render(request, "please_login.html", {})

def logged_in(request):
    if request.COOKIES.get('User_ID'):
        User_ID = request.COOKIES.get('User_ID')
    return render(request, "logged_in.html", {'User_ID' : User_ID})