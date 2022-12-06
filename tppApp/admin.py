from django.contrib import admin
from .models import PredResults, Feedback

admin.site.register([PredResults, Feedback])
