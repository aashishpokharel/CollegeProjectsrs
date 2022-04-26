
import re
from django.views import View
from django.contrib.auth.hashers import check_password
from Recommendation.models import m_oldschool

pattern = re.compile(r'')
from django.shortcuts import render, redirect
from Recommendation.models.m_oldschool import oldSchool

from Recommendation.models.register import Register


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        register = Register.get_student_by_email(email)
        # registerCheck = Register.check_student_by_email(email)
        error_message = None
        if register:
            flag = check_password(password, register.password)
            if flag:
                request.session['registers_id'] = register.id
                request.session['name'] = register.name
                request.session['email'] = register.email
                Display_id = request.session.get('register_id')
                Display_name = request.session.get('name')
                context = {
                    'data_id': Display_id,
                    'data_name': Display_name
                }
                # if m_oldschool.email_check:
                #     print("I got it")
                #     return redirect('DashboardHome')
                # else:
                #     print("I didnt got it")
                return render(request, 'DashboardHome.html', context)




            else:
                error_message = "Email or password invalid"
                return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('login')
