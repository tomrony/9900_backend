import json

from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from .forms import UserForm




def main_page(request):
    return render(request, 'main_page.html')

@csrf_exempt
def login(request):
    if request.method == 'GET':
        # if request.session.get('username'):
        #     return HttpResponseRedirect('/')
        # usr_cookie = request.COOKIES.get('username')
        # if usr_cookie:
        #     request.session['username'] = usr_cookie
        #     return HttpResponseRedirect('/')
        # return render(request, 'login.html')
        csrf_token = get_token(request)
        return JsonResponse({'csrfToken': csrf_token})

    elif request.method == 'POST':
        # username = request.POST['username']
        # password = request.POST['password']
        # user = authenticate(username=username, password=password)
        # if user is not None:
        #     auth_login(request, user)
        #     request.session['username'] = username
        #     return HttpResponseRedirect('/')
        # else:
        #     messages.error(request, 'We could not verify the login details you entered.')
        #     return render(request, 'login.html')
        inputs = json.loads(request.body)
        username = inputs['username']
        password = inputs['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            request.session['username'] = username
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid username or password'})



@csrf_exempt
def signup(request):
    if request.method == 'GET':
        # return render(request, 'signup.html')
        csrf_token = get_token(request)
        return JsonResponse({'csrfToken': csrf_token})

    elif request.method == 'POST':
        # username = request.POST['username']
        # password_1 = request.POST['password_1']
        # password_2 = request.POST['password_2']
        # if username == '' or password_1 == '' or password_2 == '':
        #     messages.error(request, 'Fields cannot be empty')
        #     return render(request, 'signup.html')
        # if password_2 != password_1:
        #     messages.error(request, 'Passwords do not match')
        #     return render(request, 'signup.html')
        # if User.objects.filter(username=username).exists():
        #     messages.error(request, 'User already exists')
        #     return render(request, 'signup.html')
        # User.objects.create(username=username, password=password_1)
        # messages.success(request, 'Registration successful, please login')
        # return HttpResponseRedirect('/login')
        inputs = json.loads(request.body)
        form = UserForm(inputs)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Registration successful, please login'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)




