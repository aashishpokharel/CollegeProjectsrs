from django.contrib import admin
from .models.collegereview import Review
from .models.faculty import Faculty
from .models.register import Register
from .models.AddCollege import AddColleges
from .models.m_oldschool import oldSchool


class AdminReview(admin.ModelAdmin):
    list_display = ['id','schoolname','address', 'collegeName', 'collegeLocation', 'facultyName', 'collegeReview','rating' ,'registered_email']


class AdminFaculty(admin.ModelAdmin):
    list_display = ['name']

class AdminRegister(admin.ModelAdmin):
    list_display = ['id','name','email','password','address','phone','date_created']

class AdminAddCollege(admin.ModelAdmin):
    list_display = ['name','address','phone','description','website','image']

class AdminOldSchool(admin.ModelAdmin):
    list_display = ['pastSchool','address','student_email']


# Register your models here.
admin.site.register(Review, AdminReview)
admin.site.register(Faculty, AdminFaculty)
admin.site.register(Register, AdminRegister)
admin.site.register(AddColleges, AdminAddCollege)
admin.site.register(oldSchool, AdminOldSchool)
