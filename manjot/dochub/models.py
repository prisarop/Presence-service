from django.db import models as m

# Create your models here.
class register(m.Model):
    username=m.SlugField(max_length=80)
    name=m.CharField(max_length=150)
    email=m.EmailField(max_length=150)
    d_o_b=m.CharField(max_length=20)
    gender=m.CharField(max_length=20)
    mobile=m.CharField(max_length=30)
    passwd=m.SlugField(max_length=400)
    date_joined=m.DateTimeField(auto_now_add=True, blank=True)
