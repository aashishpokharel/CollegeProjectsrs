
import re
from Recommendation.models.AddCollege import AddColleges
from .review import Review
from Recommendation.models.m_oldschool import oldSchool

from django.views import View

from ..models import m_oldschool, collegereview

pattern = re.compile(r'')
from django.shortcuts import render, redirect

def College(request):

    # int = Review.get_school_name()
    # print("SFsadf", int)
    # int = request.session['email']
    # print(int)
    #
    #
    # # data = m_oldschool.email_check
    #
    # def get_review_from_data(int):
    #     try:
    #         return Review.objects.get(registered_email=int)
    #     except:
    #         return False
    #
    # data = Review.get_review_from_data(int)
    # print(data.rating)

    # subjectData = request.GET.get('oldschool')
    # print("Result",subjectData)
    # dataa = Review.get_review_value()
    #
    # for data in
    global data
    review0 = Review.objects.all()
    for review in review0:
        data = review.pk
        # print(data)

    review2 = Review.objects.all()
    for reviews in review2:
        data1 = reviews.schoolname
        if data1 == 'fasdf':
            print("Fuck")
            # review3 = Review.objects.all()
            # for reviewss in review3:
            #     if reviewss.rating>2:


            # review1 = Review.objects.get(pk=data)
            # print(review1.rating)
            # if review1.rating > 1:
            #     print("The school name is")
                # for data1 in review1.schoolname:
                #     print(data1)
        else:
            print("do not contain value")


    reviewdata = Review.get_review_value()
    listt = []
    for data in reviewdata:
        rating_count = data.rating
        listt.append(rating_count)
    length = len(listt)
    print(length)
    count = 0
    element = 5

    for i in range(0, length):
        if element == listt[i]:
            count += 1
    if count == 0:
        print(element, "Not found in given list")
    else:
        data = count / length


    colleges = AddColleges.get_all_college()
    # request.session['description'] = colleges.description
    # data = AddColleges.get_session_college()
    # request.session['description'] = data

    context = {
    'addcollege': colleges,
    # 'reviewdata': data,
        'reviews':reviewdata
    }
    return render(request, 'college.html', context)
