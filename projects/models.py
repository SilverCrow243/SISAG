from django.db import models
from django.contrib.auth.models import User
from ministries.models import Ministry


class Project(models.Model):
    """Modèle pour représenter une initiative/projet"""
    STATUS_CHOICES = [
        ('planning', 'Planification'),
        ('in_progress', 'En cours'),
        ('completed', 'Complété'),
        ('on_hold', 'En attente'),
    ]

    title = models.CharField(max_length=300)
    description = models.TextField()
    ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE, related_name='projects')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planning')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    budget = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    progress_percentage = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Projet"
        verbose_name_plural = "Projets"

    def __str__(self):
        return self.title


class Indicator(models.Model):
    """Modèle pour les indicateurs/KPIs d'un projet"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='indicators')
    name = models.CharField(max_length=200)
    target_value = models.FloatField()
    current_value = models.FloatField(default=0)
    unit = models.CharField(max_length=50)  # %, nombre, valeur monétaire, etc.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.title} - {self.name}"

    @property
    def progress(self):
        """Calcule le pourcentage de progression"""
        if self.target_value == 0:
            return 0
        return min(100, int((self.current_value / self.target_value) * 100))
