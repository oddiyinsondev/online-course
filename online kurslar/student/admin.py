from django.contrib import admin
from .models import Post, Courses, Contact, about_user, videos_post, CommentPost, Category



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'updated')
    
    
@admin.register(Courses)
class Coursess(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(Contact)
admin.site.register(about_user)
admin.site.register(CommentPost)


@admin.register(videos_post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'updated')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('title', 'author')
    
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {'slug':('name',)}
    search_fields = ('name', 'author')
    