from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def town(request):
    return render(request, 'town.html')


def mshomo(request):
    return render(request, 'mshomo.html')


def index(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'profile.html')


def upload_post(request):
    return render(request, 'upload_post.html')


def signup(request):
    if request.method == "POST":

        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('home')

    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'signup.html', context)


def neighbourhoods(request):
    all_hoods = Neighbourhood.objects.all()
    all_hoods = all_hoods[::-1]
    params = {
        'all_hoods': all_hoods,
    }
    return render(request, 'neighbourhoods.html', params)


def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm()
    return render(request, 'create_profile.html', {'form': form})
