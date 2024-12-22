from django.contrib import admin
from .models import UserProfile
from .models import StudyGroup

admin.site.register(StudyGroup)
admin.site.register(UserProfile)
