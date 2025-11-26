from django.db import models


class DashboardStatistic(models.Model):
    """Modèle pour les statistiques affichées au tableau de bord"""
    title = models.CharField(max_length=200)
    value = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True)  # Nom de l'icône
    description = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Statistique"
        verbose_name_plural = "Statistiques"

    def __str__(self):
        return self.title
