from django.db import models

class Subject(models.Model):

    name = models.CharField(max_length=255)

    slug = models.SlugField(unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Unit(models.Model):
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,related_name="units")
    title=models.CharField(max_length=255)
    slug=models.SlugField(unique=True)
    order=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

class Topic(models.Model):
    unit=models.ForeignKey(Unit,on_delete=models.CASCADE,related_name="topics")
    title=models.CharField(max_length=255)
    slug=models.SlugField(unique=True)
    markdown_content=models.TextField()
    order=models.PositiveIntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
