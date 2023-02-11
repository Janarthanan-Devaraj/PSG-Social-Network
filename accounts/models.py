from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    gender = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class AcademicInfo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    graduation_year = models.IntegerField()
    
    def __str__(self):
        return self.user.username + ": " + self.school_name

class CompanyInfo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    salary = models.FloatField()
    
    def __str__(self):
        return self.user.username + ": " + self.company_name

