from django.db import models


class Boss(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=200)
    quote = models.TextField()
    image = models.ImageField(default='default-boss.jpg')


class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=200)
    image = models.ImageField(default='default-employee.jpg')


class City(models.Model):
    name = models.CharField(max_length=100)