
from django.contrib import admin
from django.urls import path
from Recommendation import views
from .views.login import Login, logout
from .views.signup import Signup
from .views.home import homePages
from .views.review import postReview
from .views.dashboard import Dashboard
from .views.rating_collect import Rate_collect
from .views.college import College
from .views.sname_collect import Sname_Collect
from .views.v_oldschool import PastSchool
from .views.dashboardhome import DashboardHome

urlpatterns = [
    path('', homePages, name='homepage'),
    path('Dashboard/', Dashboard, name = 'dashboard'),
    path('signupages',Signup.as_view(), name = 'signuppages'),
    path('dashboardhome',DashboardHome, name = 'DashboardHome'),
    path('college', College, name = 'college'),
    path('rate', Rate_collect, name = 'rate'),
    path('sname', Sname_Collect, name = 'sname'),
    path('oldschool', PastSchool.as_view(), name = 'oldschool'),
    path('login', Login.as_view(), name = 'login'),
    path('logout', logout, name = 'logout'),
    path('review', postReview.as_view(), name='review'),
    # path('ratings/', include('star_ratings.urls', namespace='ratings')),
]


