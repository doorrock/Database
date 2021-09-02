from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(primary_key=True, blank=True, max_length=50)
    owner = models.CharField(blank=True, max_length=50)
    date = models.DateField(blank=True)
    marketC = models.CharField(blank=True, max_length=50)
    intro = models.TextField()

    class Meta:
        db_table = 'company_info'


class Affilate(models.Model):
    affilate = models.CharField(primary_key=True, blank=True, max_length=50)
    c_name = models.ForeignKey(Company, db_column='c_name', on_delete=models.CASCADE)
    type = models.CharField(blank=True, max_length=50)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)

    class Meta:
        db_table = 'hire_info'
        unique_together = ['affilate', 'c_name']