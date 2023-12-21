from django.contrib import admin

# Register your models here.
from .models import FeedBack
from .models import Firsts
admin.site.register(FeedBack)
admin.site.register(Firsts)

