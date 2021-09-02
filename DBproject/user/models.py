from django.db import models

# Create your models here.
class User(models.Model):


    user_id = models.CharField(primary_key=True, verbose_name='id', blank=True, max_length=50)
    password = models.CharField(verbose_name='pw', blank=True, max_length=50)
    name = models.CharField(verbose_name='name', blank=True, max_length=50)
    nick_name = models.CharField(verbose_name='nick', blank=True, max_length=50)
    age = models.IntegerField(verbose_name='age', blank=True)
    score = models.FloatField(verbose_name='score', blank=True)
    gender = models.CharField(blank=True, max_length=50)

    class Meta:
        db_table = 'user_info'