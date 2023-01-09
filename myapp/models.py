from django.db import models
from datetime import datetime
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

class District(models.Model):
      country = models.ForeignKey(Country, on_delete=models.CASCADE)
      state = models.ForeignKey(State, on_delete=models.CASCADE)
      name = models.CharField(max_length=250)
      created_at =  models.DateTimeField(default=datetime.now)

      def __str__(self):
          return self.name

class prejobloc(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

GENDER_CHOICE = (
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),
)

class employeeDetails(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    mobile = models.CharField(max_length=20)
    gender = models.CharField(choices=GENDER_CHOICE,max_length=210)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    prejoblocation = models.CharField(max_length=250)
    emp_img = models.ImageField(upload_to='emp_pic')
    emp_app = models.FileField(upload_to='emp_attachment')
    is_active = models.CharField(max_length=250,default='Waiting for Approval')
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
    