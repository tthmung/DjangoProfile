from django.db import models
from django.contrib import admin, staticfiles
from django.db.models.deletion import CASCADE
# Create your models here.
# Defines a list of job positions
class experienceList(models.Model):
    # Each list has a company name, the position name, date when job started, date when job ended, and a textfield with short discription of the job
    # And picture associated to it

    # The name of the company, max letter of 200
    company_name = models.CharField(max_length=200)

    # The name of the position taken, max letter of 200
    position_name = models.CharField(max_length=200)

    # Text field containing a short overview of the job
    position_detail = models.TextField()

    # Date Started on the job
    date_started = models.CharField(max_length=200)

    # Date of job termination
    date_ended = models.CharField(max_length=200)

    date = models.DateField(auto_now_add=False)

    @property
    def exp_item_picture(self):
        return self.exp_pics.first().pictures

    def __str__(self):
        return self.company_name

class experienceImage(models.Model):
    pictures = models.ImageField(upload_to="experience/")
    experience = models.ForeignKey(experienceList, default=None, on_delete=CASCADE, related_name="exp_pics")

    def __str__(self):
        return self.experience.company_name
