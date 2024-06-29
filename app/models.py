from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
class GeneralInfo(models.Model):
    company_name=models.CharField(max_length=100,default='Company')
    location =models.CharField(max_length=250)
    email=models.EmailField()
    desc=models.TextField(default="hello")
    phone =models.CharField(max_length=250)
    open_hours=models.CharField(max_length=100, blank=True,null=True)
    video_url = models.URLField(blank=True,null=True)
    twitter_url = models.URLField(blank=True,null=True)
    facebook_url = models.URLField(blank=True,null=True)
    insta_url = models.URLField(blank=True,null=True)
    linkedin_url = models.URLField(blank=True,null=True)
    def __str__(self):
        return self.company_name
    
class ServiceInfo(models.Model):
    icon=models.CharField(max_length=50 ,null=True,blank=True)
    title=models.CharField(max_length=250, unique=True)
    description=models.TextField()
    def __str__(self):
        return self.title
class Testimonials(models.Model):
    user_image=models.CharField(max_length=225,null=True,blank=True)
    rating_count=models.IntegerField()
    username=models.CharField(max_length=50)
    user_job_title=models.CharField(max_length=50)
    review =models.TextField()
    def __str__(self):
        return self.username
    
class Faq(models.Model):
    question=models.TextField()
    answer=models.TextField()
    def __str__(self):
        return self.question
    
class ContactFormLogs(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    action_time = models.DateTimeField(null=True,blank=True)
    is_success = models.BooleanField(default=False)
    is_error = models.BooleanField(default=False)
    error_message = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.email
    
class Author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name =models.CharField(max_length=50, null=True ,blank=True)
    country = models.CharField(max_length=50)
    joined_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.first_name
    
class Blog(models.Model):
    blog_image=models.CharField(max_length=500, blank=True, null=True)
    category = models.CharField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=500)
    author = models.ForeignKey(Author,on_delete=models.PROTECT,null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    content = RichTextField()#models.TextField()
    def __str__(self):
        return self.title




