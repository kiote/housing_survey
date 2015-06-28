"""Initialize django."""
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "housing_survey.settings")
django.setup()
