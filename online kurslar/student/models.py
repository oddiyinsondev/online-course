from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import FileExtensionValidator




class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status = 'published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=255)
    all_courses = models.TextField()
    virtual_class = models.TextField()
    real_meeting = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()  
    published = PublishedManager() 

    class Meta:
        ordering = ('-publish',)
 
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])


    def __str__(self):
        return self.title
    
    
    
    
class Courses(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    name = models.CharField(max_length=255)
    teacher_image =  models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)
    body = models.TextField()
    lesson_time_image = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)
    free_or_pay = models.CharField(max_length=5)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()  
    published = PublishedManager() 

    class Meta:
        ordering = ('-publish',)
 
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])


    def __str__(self):
        return self.name
    

class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.full_name



class about_user(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    best_education_name =  models.CharField(max_length=55)
    best_education_body = models.TextField()
    best_education_images1 = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)
    top_managment_name = models.CharField(max_length=55)
    top_managment_body = models.TextField()
    top_managment_images2 = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)
    quality_meeting_name = models.CharField(max_length=55)
    quality_meeting_body = models.TextField()
    quality_meeting_images3 = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()  
    published = PublishedManager() 

    class Meta:
        ordering = ('-publish',)
 
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])


    def __str__(self):
        return self.best_education_name


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = "Cotegories"
        
    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('category_post', args=[self.slug])


class videos_post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    video = models.FileField(upload_to='videos_uploaded',null=True,
    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()  # defoult manager
    published = PublishedManager() # published manajer yangiliklarni qayataradi

    class Meta:
        ordering = ('-publish',)
 
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])


    def __str__(self):
        return self.title


class CommentPost(models.Model):
    post = models.ForeignKey(videos_post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateField(auto_now_add=True)


    def __str__(self) -> str:
        return f"{self.author} -> {self.body}"

    class Meta:
        ordering = ('-created',)




