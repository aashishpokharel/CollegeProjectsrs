from importlib import import_module
from django.conf import settings

# SessionStore = import_module(settings.SESSION_ENGINE).sessionStore

from django.db import models
from .faculty import Faculty

class Review(models.Model):
    # name = models.CharField(max_length=200)
    schoolname = models.CharField(max_length=200)
    registered_email = models.EmailField(default=True)
    # register_id = models.OneToOneField(Register, on_delete=models.CASCADE, default=True)
    address = models.CharField(max_length=500)
    collegeName = models.CharField(max_length=200)
    collegeLocation = models.CharField(max_length=200)
    facultyName = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    collegeReview = models.CharField(max_length=200)
    rating = models.IntegerField(default=True)
    # created_at = models.DateTimeField(auto_now_add=True)

    def AddReview(self):
        self.save()

    # @staticmethod
    # def get_school_name(self):
    #     try:
    #         return Review.objects.filter(schoolname = self.schoolname)
    #     except:
    #         return False



    # @staticmethod
    # def get_review_from_data(int):
    #     try:
    #         return Review.objects.get(rating = int)
    #     except:
    #         return False


    @property
    def isExist(self):
        if Review.objects.filter(collegeName = self.collegeName) & Review.objects.filter(registered_email = self.registered_email):
            return True
        return False

    @staticmethod
    def get_review_value():
        return Review.objects.all()