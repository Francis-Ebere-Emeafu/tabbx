from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from .utils.states import STATE_CHOICES
from .utils.gender import GENDER_CHOICES



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=True, null=True)

    birth_date = models.DateField(verbose_name="Date of birth", null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    picture = models.ImageField(upload_to="profile", null=True, blank=True)

    state = models.CharField(max_length=3, choices=STATE_CHOICES, blank=True, null=True)
    school = models.CharField(max_length=20, blank=True, null=True)

    confirm_email = models.BooleanField(default=False)
    date_registered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        if self.middle_name:
            return "{} {} {}".format(self.first_name, self.middle_name, self.surname)
        else:
            return "{} {}".format(self.first_name, self.surname)




class Judge(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

