from django.contrib import admin
from .models import Post
from .models import Count
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','pub_date')

admin.site.register(Post, PostAdmin)

class CountAdmin(admin.ModelAdmin):
    list_display=('year','name','price','count','last')

admin.site.register(Count, CountAdmin)