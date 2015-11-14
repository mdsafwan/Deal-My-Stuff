from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from login.models import user_details
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
    successful_login = True
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        if user_details.objects.filter(User_Name=username, Password=password).exists():    
            successful_login = True
            return HttpResponseRedirect('/home/')
        else:
            successful_login = False
    return render(request, "login.html", {'successful_login' : successful_login})
#return render_to_response('login.html',{}, context_instance=RequestContext(request))


def register(request):
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
        if password != confirm_password:
            password_match = False
            return render(request, "register.html", {'password_match' : password_match})
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
                                    Password = password,)
        
        return render(request, "registration_success.html", {})
    
    password_match = True
    return render(request, "register.html", {'password_match' : password_match})