from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=400)
    address = models.CharField(max_length=80)
    phone = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


    @staticmethod
    def get_student_by_email(email):
        try:
            return Register.objects.get(email=email)
        except:
            return False

    # @staticmethod
    # def getName(name):
    #     try:
    #         return Register.objects.get(name=name)
    #     except:
    #         return False

    @property
    def isExist(self):
        if Register.objects.filter(email = self.email):
            return True
        else:
            return False

    def registerData(self):
        self.save()
