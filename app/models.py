from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Company(models.Model):
    image = models.ImageField(upload_to='company_images/')
    name = models.CharField(max_length=255)
    about = models.TextField()
    contacts = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural ='Companies'

class Statistics(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    cars = models.FloatField()
    customers = models.IntegerField()
    network = models.IntegerField()
    reviews = models.IntegerField()

    def __str__(self):
        return f'Statistics for {self.company.name}'

class OfficeHours(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    day = models.CharField(max_length=255)
    hours = models.CharField(max_length=255)

    def __str__(self):
        return f'Office Hours for {self.company.name} on {self.day}'

class SocialNetworks(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return f'Social Network {self.name} for {self.company.name}'

class Partners(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='partner_images/')

    def __str__(self):
        return f'Partner for {self.company.name}'



class Steps(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Steps'
        verbose_name = 'Steps'

class StepDetails(models.Model):
    steps = models.ForeignKey(Steps, on_delete=models.CASCADE, related_name='details')
    about = models.TextField()

    def __str__(self):
        return f'Details for {self.steps.name}'

class Blogs(models.Model):
    image = models.ImageField(upload_to='blog_images/')
    date = models.DateTimeField()
    header = models.CharField(max_length=255)
    summary = RichTextUploadingField()

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural ='Blogs'

class FAQ(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class FAQInfo(models.Model):
    faq = models.ForeignKey(FAQ, on_delete=models.CASCADE, related_name='info')
    about = models.TextField()

    def __str__(self):
        return f'Info for {self.faq.name}'