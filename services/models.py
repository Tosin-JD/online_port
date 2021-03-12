from django.db import models

# Create your models here.
class Service(models.Model):
    """
    
    """
    name = models.CharField(max_length=100)
    bullet_one = models.CharField(max_length=300)
    bullet_two = models.CharField(max_length=300)
    bullet_three = models.CharField(max_length=300)
    description = models.TextField()
    second_description = models.TextField()
    third_description = models.TextField()
    image = models.ImageField(upload_to='services/')
    second_image = models.ImageField(upload_to='services/')
    third_image = models.ImageField(upload_to='services/')
    
    def __str__(self):
        return self.name
    
    
class AnimatedIntro(models.Model):
    one_word_title = models.CharField(max_length=12)
    rem_title = models.CharField(max_length=38)
    note = models.TextField()
    slide = models.ImageField(upload_to='slides')
    
    def __str__(self):
        return "{} {}".format(self.one_word_title, self.rem_title)
    

class WelcomeNote(models.Model):
    half_title = models.CharField(max_length=30)
    rem_title = models.CharField(max_length=30, verbose_name='Remaining Title')
    first_para = models.TextField(verbose_name='First Paragraph')
    sec_para = models.TextField(verbose_name='Second Paragraph')
    first_bul = models.TextField(verbose_name='First Bullet')
    sec_bul = models.TextField(verbose_name='Second Bullet')
    third_bul = models.TextField(verbose_name='Third Bullet')
    conclusion = models.TextField()
  
    def __str__(self):
        return "{} {}".format(self.half_title, self.rem_title)
    
    
class About(models.Model):
    about_title = models.CharField(max_length=255)
    first_description = models.TextField()
    second_description = models.TextField()
    third_description = models.TextField()
    about_image = models.ImageField(upload_to='about')
    conclusion = models.TextField()
  
    def __str__(self):
        return "{}".format(self.title)
        
    
    