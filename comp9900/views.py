import json
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from .forms import UserForm, LoginForm




def main_page(request):
    return render(request, 'main_page.html')

# @csrf_exempt
def login(request):
    if request.method == 'GET':
        csrf_token = get_token(request)
        return JsonResponse({'csrfToken': csrf_token})

    elif request.method == 'POST':
        inputs = json.loads(request.body)
        form = LoginForm(data=inputs)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username,password)
            if user is not None:
                auth_login(request, user)
                request.session['username'] = username
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'message': 'Invalid username or password'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})



# @csrf_exempt
def signup(request):
    if request.method == 'GET':
        csrf_token = get_token(request)
        return JsonResponse({'csrfToken': csrf_token})

    elif request.method == 'POST':
        inputs = json.loads(request.body)
        form = UserForm(inputs)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({'success': True, 'message': 'Registration successful, please login'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})




