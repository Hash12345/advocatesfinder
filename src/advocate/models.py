import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    logo = models.ImageField(upload_to="company", blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name
    

class TechStack(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False, null=False)
    description = models.CharField(max_length=500, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Advocate(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    full_name = property(lambda self: f"{self.first_name} {self.last_name}")
    profile_pic = models.ImageField(upload_to="profile", blank=True)
    bio_short = models.TextField(max_length=500, blank=True, null=True)
    bio_long = models.TextField(max_length=5000, blank=True, null=True)
    advocate_years_exp = models.PositiveIntegerField(blank=True, null=True)
    priority = models.IntegerField(default=0)
    tech_stack  = models.ManyToManyField(to=TechStack)
    company = models.ForeignKey(to=Company, on_delete=models.SET_NULL, blank=True, null=True)
    is_complete = models.BooleanField(default=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-priority']

    def __str__(self):
        return self.full_name


class Link(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, blank=False, null=False)
    advocate = models.ForeignKey(to=Advocate, related_name='links', on_delete=models.CASCADE, blank=False, null=False)
    followers = models.PositiveIntegerField(default=0)
    url = models.URLField(unique=True, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['advocate', 'name']


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    advocator = models.ForeignKey(to=Advocate, related_name='reviewed', on_delete=models.CASCADE, blank=False, null=False)
    reviewed_by = models.ForeignKey(to=Advocate, related_name='reviewer', on_delete=models.CASCADE, blank=False, null=False)
    message = models.TextField(max_length=500,blank=True, null=True)
    rate = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        unique_together = ['advocator', 'reviewed_by']