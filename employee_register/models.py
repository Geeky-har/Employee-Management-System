from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=20)

    # this will show the value of positions in the dropdown
    def __str__(self):
        return self.title

class Employee(models.Model):
    name = models.CharField(max_length=100)
    empid = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=100)

    # any deletion in Positions table will also be reflected in this table
    position = models.ForeignKey(Position, on_delete=models.CASCADE)