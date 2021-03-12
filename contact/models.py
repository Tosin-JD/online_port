from django.db import models

# Create your models here.



STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    
    def __str__(self):
        return "from " + self.name
    
    
    
class Booking(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date = models.CharField(max_length=12)
    time = models.CharField(max_length=12)
    number_of_people = models.IntegerField()
    message = models.TextField()
    
    def __str__(self):
        return '{} coming on {} at {}.'.format(self.name, self.date, self.time)
   
    
class Testimonial(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    testifier_image = models.ImageField(upload_to='testimony')
    occupation = models.CharField(max_length=30)
    position = models.CharField(max_length=30, blank=True, null=True)
    title = models.CharField(max_length=255)
    testimony = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    
    
    def __str__(self):
        return "from " + self.first_name + ' testimony'
        
    class Meta:
        verbose_name = 'Testimony'
        verbose_name_plural = 'Testimonies'
