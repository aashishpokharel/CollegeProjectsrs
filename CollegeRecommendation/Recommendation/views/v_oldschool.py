from django.http import request
from django.shortcuts import render, redirect
from django.views import View
from Recommendation.models.m_oldschool import oldSchool
import re
pattern = re.compile(r'')

class PastSchool(View):
    def get(self, request):
        return render(request, 'oldschool.html')

    def post(self, request):
        postData = request.POST
        schoolname = postData.get('sname')
        student_email = request.session.get('email')
        schoollocation = postData.get('slocation')

        oldschool = oldSchool(pastSchool=schoolname,
                              address=schoollocation,
                              student_email = student_email)

        error_message = None
        # validation

        value = {
            schoolname:'schoolname',
            schoollocation:'schoollocation'
        }

        error_message = self.validationOldSchool(schoolname,schoollocation)

        #saving
        if not error_message:
            oldschool.SaveOldSchool()
            return redirect('DashboardHome')
        else:
            data = {
                'error':error_message,
                'values':value
            }
            return render(request, 'oldschool.html', data)

    def validationOldSchool(self, schoolname,schoollocation):
        error_message = None
        if (not schoolname):
            error_message = "School name is required"
        elif (not schoollocation):
            error_message = "Schoollocation is required"
        elif re.search(r'[!@#$%&]', schoolname):
            error_message = "School name doesnot contain special character"
        elif re.search(r'[A-Z]', schoolname):
            error_message = "School name should be small letter"
        elif re.search(r'[!@#$%&]', schoollocation):
            error_message = "School location doesnot contain special character"
        elif re.search(r'[A-Z]', schoollocation):
            error_message= "School location should be in small letter"
        return error_message

