from django.db import models

# Create your models here.
from django.db import models

# Model for Personal Information
class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    about_me = models.TextField()
    skills = models.TextField()
    phone = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=200,blank=True)
    facebook = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)
    email= models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return self.name


# Model for Projects
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    project_url = models.URLField(blank=True, null=True)  
    image = models.ImageField(upload_to='images/', blank=True, null=True)  

    def __str__(self):
        return self.name
    
# Model for Contact Me
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subject}"

# Model for Experience/Education
class Experience(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # Optional for ongoing roles
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.organization}"


