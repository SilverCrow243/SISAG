from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Indicator



def projects_list(request):
    """Liste de tous les projets/initiatives"""
    projects = Project.objects.all()
    status_filter = request.GET.get('status', None)
    
    if status_filter:
        projects = projects.filter(status=status_filter)
    
    context = {
        'projects': projects,
        'page_title': 'Initiatives/Projets',
        'status_choices': Project._meta.get_field('status').choices,
        'current_status': status_filter,
    }
    return render(request, 'projects/projects_list.html', context)



def project_detail(request, pk):
    """Détail d'un projet avec ses indicateurs"""
    project = get_object_or_404(Project, pk=pk)
    indicators = project.indicators.all()
    
    context = {
        'project': project,
        'indicators': indicators,
        'page_title': f'Projet - {project.title}',
    }
    return render(request, 'projects/project_detail.html', context)
