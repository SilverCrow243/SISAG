import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from datetime import date, timedelta
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from ministries.models import Ministry
from projects.models import Project
import random

# Essayer de récupérer un utilisateur existant ou en créer un
try:
    user = User.objects.first()  # Récupérer le premier utilisateur
    if not user:
        print("❌ Aucun utilisateur trouvé. Création d'un utilisateur...")
        user = User.objects.create_user(username="admin", password="12345")
        print(f"✅ Utilisateur créé: {user.username}")
    else:
        print(f"✅ Utilisateur trouvé: {user.username}")
except Exception as e:
    print(f"❌ Erreur lors de la récupération de l'utilisateur: {e}")
    exit()

# Définir les projets spécifiques pour chaque ministère
projects_by_ministry = {
    "Ministère de la Santé Publique": [
        {"title": "Campagne nationale de vaccination", "description": "Assurer la vaccination de la population contre les maladies prioritaires.", "status": "in_progress"},
        {"title": "Modernisation des hôpitaux régionaux", "description": "Équiper les hôpitaux avec du matériel médical moderne.", "status": "planning"}
    ],
    "Ministère de l'Éducation Nationale": [
        {"title": "Numérisation des classes", "description": "Intégrer les outils numériques dans les écoles primaires et secondaires.", "status": "in_progress"},
        {"title": "Programme de formation des enseignants", "description": "Organiser des ateliers et formations pour le personnel éducatif.", "status": "completed"}
    ],
    "Ministère des Finances": [
        {"title": "Réforme fiscale digitale", "description": "Mettre en place un système digital pour améliorer la collecte des impôts.", "status": "planning"}
    ],
    "Ministère de l'Intérieur": [
        {"title": "Renforcement des services de sécurité", "description": "Moderniser les forces de sécurité et améliorer la gestion des collectivités.", "status": "in_progress"}
    ],
    "Ministère des Travaux Publics": [
        {"title": "Réhabilitation du réseau routier national", "description": "Réparer et construire des routes dans tout le pays.", "status": "on_hold"}
    ],
    "Ministère de l'Énergie et Ressources Hydrauliques": [
        {"title": "Programme d'électrification rurale", "description": "Étendre l'accès à l'électricité dans les zones rurales.", "status": "planning"}
    ],
    "Ministère de l'Agriculture et Développement Rural": [
        {"title": "Développement de coopératives agricoles", "description": "Créer et soutenir des coopératives pour améliorer la production agricole.", "status": "in_progress"}
    ]
}

# Ajouter les projets dans la base
projects_created = 0
for ministry_name, projects in projects_by_ministry.items():
    try:
        ministry = Ministry.objects.get(name=ministry_name)
    except Ministry.DoesNotExist:
        print(f"❌ Ministère non trouvé : {ministry_name}")
        continue
    
    for proj in projects:
        # Vérifier si le projet existe déjà
        if Project.objects.filter(title=proj["title"], ministry=ministry).exists():
            print(f"⏭️  Projet déjà existant : {proj['title']} ({ministry.name})")
            continue
            
        start_date = date.today() - timedelta(days=random.randint(0, 365))
        end_date = start_date + timedelta(days=random.randint(30, 365))
        budget = round(random.uniform(50000, 5000000), 2)
        progress_percentage = random.randint(0, 100)
        
        try:
            project = Project.objects.create(
                title=proj["title"],
                description=proj["description"],
                ministry=ministry,
                status=proj["status"],
                start_date=start_date,
                end_date=end_date,
                budget=budget,
                progress_percentage=progress_percentage,
                created_by=user
            )
            
            print(f"✅ Projet ajouté : {project.title} ({ministry.name})")
            projects_created += 1
        except Exception as e:
            print(f"❌ Erreur lors de la création du projet {proj['title']}: {e}")

print(f"\n📊 Total de projets créés : {projects_created}")
