from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token

# Create your views here.
def index(request):
    context={}
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            
            return render(request,'pagina/Index.html' ,{"fname":fname})
        else:
            messages.error(request, "nombre de usuario o contraseña erronea")
            
    return render(request, 'pagina/Index.html', context)

def registro(request):
    context={}
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('registro')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('registro')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('registro')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('registro')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('/')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
       
        # Welcome Email
        subject = "Bienvenido a UcO"
        message = "Hola " + myuser.first_name + "!! \n" + "Bienvenido a ÜcÖ \nGracias por Registrarte\n. Te hemos enviado un correo para confirmar tu correo, porfavor revisa tu carpeta de Spam, para que no te pierdas nada \n\nGracias\nEquipo de ÜcÖ"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ GFG - Django Login!!"
        message2 = render_to_string('email_confirmation.html',{
            
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [myuser.email],
        )
        email.fail_silently = True
        email.send()
        
        return redirect('registro')

    return render(request, 'pagina/registro.html', context)

def nosotros(request):
    context={}
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            
            return render(request,'pagina/Nosotros.html' ,{"fname":fname})
        else:
            messages.error(request, "nombre de usuario o contraseña erronea")
    return render(request, 'pagina/Nosotros.html', context)
def pantalones(request):
    context={}
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            
            return render(request,'pagina/pantalones.html' ,{"fname":fname})
        else:
            messages.error(request, "nombre de usuario o contraseña erronea")
    return render(request, 'pagina/pantalones.html', context)
def poleras(request):
    context={}
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            
            return render(request,'poleras/Index.html' ,{"fname":fname})
        else:
            messages.error(request, "nombre de usuario o contraseña erronea")
    return render(request, 'pagina/poleras.html', context)
def polerones(request):
    context={}
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            
            return render(request,'polerones/Index.html' ,{"fname":fname})
        else:
            messages.error(request, "nombre de usuario o contraseña erronea")
    return render(request, 'pagina/polerones.html', context)

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('/')

def activate(request,uidb64,token):
    try:
        uid = (urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('/')
    else:
        return render(request,'activation_failed.html')