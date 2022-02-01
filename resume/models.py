from django.db import models
from .import choice_state
# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(choices=choice_state.CHOICE_GENDER, max_length=100)
    locality = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    district = models.CharField(choices=choice_state.STATE_CHOICE, max_length=150)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_image', blank=True)
    my_file = models.FileField(upload_to='document', blank=True)

    def __str__(self):
        return self.name
    