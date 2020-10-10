from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import user_auth, Music_field
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'music/home.html')


def home_music(request):
    musics = Music_field.objects.all()
    print(len(musics), musics[1].name)
    if request.method == 'POST':
        query = request.POST.get('search')
        
        try:
            musics = Music_field.objects.get(music_file=query)
            return render(request, 'music/home_music.html', {'musics':musics})
        except KeyError:
            return HttpResponse('Music does not found')

    return render(request, 'music/home_music.html', {'musics':musics})


def signout(request):
    del request.session['authenticated']
    #print(User.is_authenticated())
    return redirect('home_page')



def signin(request):
    if request.method == 'POST':
        Email = request.POST.get('email')
        Password = request.POST.get('password')
        
        if Email and Password:
            try:
                original_user = user_auth.objects.get(email=Email)
                
                if check_password(Password, original_user.password):
                    request.user = original_user
                    request.user.save()
                    request.session['authenticated'] = True
                    return redirect('home_page')
                else:
                    return HttpResponse("password does not match")
            except Exception:
                return HttpResponse("Email does not exist")
    #print(False, False)
    print(request.GET.get('next'))
    return render(request, 'auth/signin.html')



def signup(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        hashed_password = make_password(request.POST.get('password'))
        if Name and Email and hashed_password:
            new = user_auth.objects.create(name=Name, email=Email, password=hashed_password)
            request.user = new
            request.session['authenticated'] = True
            return redirect('home_page')

    return render(request, 'auth/signup.html')