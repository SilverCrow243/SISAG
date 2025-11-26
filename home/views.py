from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Avg, Count, Q
from ministries.models import Ministry
from projects.models import Project, Indicator



def dashboard(request):
    """Vue du tableau de bord principal"""
    ministries = Ministry.objects.all()
    projects = Project.objects.all()
    
    # Statistiques générales
    total_ministries = ministries.count()
    total_projects = projects.count()
    completed_projects = projects.filter(status='completed').count()
    in_progress_projects = projects.filter(status='in_progress').count()
    planning_projects = projects.filter(status='planning').count()
    on_hold_projects = projects.filter(status='on_hold').count()
    total_indicators = Indicator.objects.count()
    
    # Projets récents (derniers 6)
    recent_projects = projects.order_by('-created_at')[:6]
    
    # Budget total et exécution
    total_budget = projects.aggregate(total=Sum('budget'))['total'] or 0
    
    # Moyenne de progression
    avg_progress = projects.aggregate(avg=Avg('progress_percentage'))['avg'] or 0
    
    # Projets en retard (supposé: si end_date < today et status != completed)
    from django.utils import timezone
    today = timezone.now().date()
    late_projects = projects.filter(
        Q(end_date__lt=today) & ~Q(status='completed')
    ).count()
    
    context = {
        'ministries': ministries,
        'projects': recent_projects,
        'total_ministries': total_ministries,
        'total_projects': total_projects,
        'completed_projects': completed_projects,
        'in_progress_projects': in_progress_projects,
        'planning_projects': planning_projects,
        'on_hold_projects': on_hold_projects,
        'total_indicators': total_indicators,
        'total_budget': total_budget,
        'avg_progress': round(avg_progress, 1),
        'late_projects': late_projects,
        'page_title': 'Tableau de Bord',
    }
    return render(request, 'home/dashboard.html', context)


@login_required
def dashboard_stats(request):
    """API pour les statistiques du tableau de bord (JSON)"""
    projects = Project.objects.all()
    data = {
        'total_ministries': Ministry.objects.count(),
        'total_projects': projects.count(),
        'completed': projects.filter(status='completed').count(),
        'in_progress': projects.filter(status='in_progress').count(),
        'on_hold': projects.filter(status='on_hold').count(),
        'planning': projects.filter(status='planning').count(),
    }
    return JsonResponse(data)
