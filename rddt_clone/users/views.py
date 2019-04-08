from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from django.views.generic import ListView
from .models import User
from .filters import UsersFilter


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            messages.success(request, f'Your account has been created {username}!')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {'u_form': u_form}

    return render(request, 'users/profile.html', context)



def profiles_list(request):

    return render(request, 'users/profile_list.html', context = {'users': User.objects.all()})


class ProfileListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'users/profile_list.html'
    ordering = ['username']

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['filter'] = UsersFilter(self.request.GET, queryset=self.get_queryset())
        return context
