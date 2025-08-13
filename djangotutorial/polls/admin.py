from django.contrib import admin
from . models import Quest, Choice
class QuestAdmin(admin.ModelAdmin):
    fieldsets = [(None, {"fields": ["question_text"]}),
                ("Date information",{"fields": ["pub_date"]}),
            ]
admin.site.register(Quest, QuestAdmin)
























