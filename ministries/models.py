from django.db import models
from django.contrib.auth.models import User


class Ministry(models.Model):
    """Modèle pour représenter un ministère"""
    name = models.CharField(max_length=200, unique=True)
    acronym = models.CharField(max_length=10, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ministère"
        verbose_name_plural = "Ministères"
        ordering = ['name']

    def __str__(self):
        return self.name


class Objective(models.Model):
    """Modèle pour les objectifs d'un ministère"""
    ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE, related_name='objectives')
    title = models.CharField(max_length=300)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ministry.name} - {self.title}"
