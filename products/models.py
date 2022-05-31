from django.db import models
from django.urls import reverse
from tinymce import models as tiny_models


class Course(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255)
    workload = models.IntegerField()
    content = tiny_models.HTMLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-title']

    def __srt__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("products:course-detail", kwargs={"slug": self.slug})


class Formation(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255)
    workload = models.IntegerField()
    number_of_courses = models.IntegerField()
    content = tiny_models.HTMLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-title']

    def __srt__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("products:formation-detail", kwargs={"slug": self.slug})
