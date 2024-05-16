from django.contrib import admin

from web_basics_exam_retake.recipe_app.models import Profile, Recipe

# Register your models here.
admin.site.register(Profile)
admin.site.register(Recipe)