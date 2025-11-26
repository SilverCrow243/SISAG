from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ministry, Objective



def ministries_list(request):
    """Liste de tous les ministères"""
    ministries = Ministry.objects.all()
    context = {'ministries': ministries, 'page_title': 'Ministères'}
    return render(request, 'ministries/ministries_list.html', context)



def ministries_detail(request, pk):
    """Détail d'un ministère avec ses objectifs et projets"""
    ministry = get_object_or_404(Ministry, pk=pk)
    objectives = ministry.objectives.all()
    projects = ministry.projects.all()
    
    context = {
        'ministry': ministry,
        'objectives': objectives,
        'projects': projects,
        'page_title': f'Ministère - {ministry.name}',
    }
    return render(request, 'ministries/ministries_detail.html', context)
