from django.contrib import admin
from .models import Portfolio, Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_readed')

admin.site.register(Portfolio)
admin.site.register(Feedback, FeedbackAdmin)
