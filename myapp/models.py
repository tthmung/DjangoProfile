from django.db import models
from django.contrib import admin, staticfiles
from django.db.models.deletion import CASCADE

# Defines a list of porjects
class ProjectList(models.Model):
    # Each list has a project name, and the detail of the project
    # And picture associated to it

    # Name of the projet, max letter of 200
    project_name = models.CharField(max_length=200)

    # Textfield containing overview of the project
    project_detail = models.TextField()

    @property
    def item_picture(self):
        return self.proj_pics.first().images

    def __str__(self):
        return self.project_name


# Define a list of multiple images for Project module
class ProjectImage(models.Model):
    images = models.ImageField(upload_to="project/")
    project = models.ForeignKey(ProjectList, default=None, on_delete=CASCADE, related_name="proj_pics")

    def __str__(self):
        return self.project.project_name
