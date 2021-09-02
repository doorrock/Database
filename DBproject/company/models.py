from django.db import models
from user.models import User
from superuser.models import Affilate
# Create your models here.

class MyCompany(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    aff_name = models.ForeignKey(Affilate, on_delete=models.CASCADE)
    c_name = models.CharField(blank=True, max_length=50)
    type = models.CharField(blank=True, max_length=50)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)

    class Meta:
        db_table = 'my_company'
        unique_together = ['user_id', 'aff_name']

class Review(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    aff_name = models.ForeignKey(Affilate, on_delete=models.CASCADE)
    review = models.TextField()

    class Meta:
        db_table = 'review'
        unique_together = ['user_id', 'aff_name']