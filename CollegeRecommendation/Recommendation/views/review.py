import re

from django.contrib.admin.templatetags.admin_list import results
from django.views import View
from django.contrib.auth.hashers import check_password, make_password
from Recommendation.models.collegereview import Review
from django.views import View
pattern = re.compile(r'')
from django.shortcuts import render, redirect
from Recommendation.models.collegereview import Review
from Recommendation.models.faculty import Faculty





class postReview(View):
    def get(self, request):
        results = Faculty.objects.all()
        return render(request, 'review.html', {'showFaculty': results})

    def post(self, request):
        postData = request.POST
        schoolname = postData.get('oldschool')
        registered_email = request.session.get('email')
        address = postData.get('address')
        collegeName = postData.get('collegeName')
        collegeLocation = postData.get('collegeLocation')
        faculty = postData.get('faculty')
        review = postData.get('review')
        rating = postData.get('rating')
        print("The review rating",rating)
        # facultyInstance = Faculty.objects.get(pk=faculty)
        # validation
        addReview = Review(schoolname=schoolname,
                            address=address,
                            registered_email = registered_email,
                            collegeName=collegeName,
                            collegeLocation=collegeLocation,
                            facultyName_id=faculty,
                            collegeReview=review,
                            rating = rating)
        Review_error = self.validateReview(collegeName, schoolname, address, collegeLocation, addReview)
        value = {
            'oldschool': schoolname,
            'address': address,
            'collegeName': collegeName,
            'collegeLocation': collegeLocation,
            }

        if not Review_error:
            addReview.AddReview()
            return redirect('DashboardHome')
        else:
            reviewdata = {
                'error': Review_error,
                'values': value,
                'showFaculty': results
            }
        return render(request, 'review.html', reviewdata)
    def validateReview(self,collegeName, schoolname, address, collegeLocation,collegereview):
        Review_error = None
        if not collegeName:
            Review_error = "College name should be added"
        elif re.search(r'[A-Z]', collegeName):
            Review_error = "College name donot contain capital letter"
        elif re.search(r'[A-Z]', schoolname):
            Review_error = "School name doesnot contain capital letter"
        elif re.search(r'[A-Z]', address):
            Review_error = "School address doesnot contain capital letter"
        elif re.search(r'[A-Z]', collegeLocation):
            Review_error = "college Location doesnot contain capital letter"
        elif collegereview.isExist:
            Review_error = "This Email already gave Review"

        # elif addReview.isExist():
    #       Review_error = 'Email Address Already Registered'
        return Review_error

    # def get_review_from_data(int):
    #     try:
    #         return Review.objects.get(rating = )