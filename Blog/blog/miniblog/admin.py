from django.contrib import admin
from .models import Postblog,Comment
# Register your models here.
@admin.register(Postblog)

class PostBlogAdmin(admin.ModelAdmin):
    list_display=['id','title','desc']


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display=['id','name','email','comments']    