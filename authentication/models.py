from django.db import models

from django.contrib.auth.models import AbstractUser


class Items(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)

class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(default=10)

class Parents(models.Model):
    name = models.CharField(max_length=200)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)