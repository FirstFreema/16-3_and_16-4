from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomUserChangeForm

def register_user(request):
    """
    Регистрация нового пользователя.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})

def login_user(request):
    """
    Вход в аккаунт пользователя.
    """
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def profile(request):
    """
    Просмотр информации об аккаунте.
    """
    return render(request,
                  'users/profile.html',
                  {'user': request.user}
                  )

@login_required
def edit_profile(request):
    """
    Изменение данных аккаунта.
    """
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST,
                                    request.FILES,
                                    instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request,
                  'users/edit_profile.html',
                  {'form': form})

@login_required
def logout_user(request):
    """
    Выход из аккаунта пользователя.
    """
    logout(request)
    return redirect('login')


