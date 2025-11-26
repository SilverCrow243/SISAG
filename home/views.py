from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from ministries.models import Ministry
from projects.models import Project, Indicator



def dashboard(request):
    """Vue du tableau de bord principal"""
    ministries = Ministry.objects.all()
    projects = Project.objects.all()[:6]
    total_projects = Project.objects.count()
    completed_projects = Project.objects.filter(status='completed').count()
    in_progress_projects = Project.objects.filter(status='in_progress').count()
    
    context = {
        'ministries': ministries,
        'projects': projects,
        'total_projects': total_projects,
        'completed_projects': completed_projects,
        'in_progress_projects': in_progress_projects,
        'page_title': 'Tableau de Bord',
    }
    return render(request, 'home/dashboard.html', context)


@login_required
def dashboard_stats(request):
    """API pour les statistiques du tableau de bord (JSON)"""
    data = {
        'total_ministries': Ministry.objects.count(),
        'total_projects': Project.objects.count(),
        'completed': Project.objects.filter(status='completed').count(),
        'in_progress': Project.objects.filter(status='in_progress').count(),
        'on_hold': Project.objects.filter(status='on_hold').count(),
    }
    return JsonResponse(data)
