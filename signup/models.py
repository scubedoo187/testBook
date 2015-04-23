from django.db import models
# Create your models here.


class SignUp(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    password = models.CharField(max_length=128, null=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self):
        return self.email
    

class Posting(models.Model):
    publisher = models.ForeignKey(SignUp)
    contents = models.TextField(max_length=1000, null=False)
    imgup = models.ImageField(upload_to=
                              '/home/jungyg/repo/testBook/static/media', 
                              height_field=600, width_field=800, max_length=100)
    comment = models.CharField(max_length=100, null=True, blank=True)
    like = models.IntegerField()
    
    def __unicode__(self):
        return self.publisher