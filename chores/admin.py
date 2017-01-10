from django.contrib import admin
from .models import ChoreList, Chore

# Register your models here.
class ChoreInline(admin.TabularInline):
    model = Chore
    extra = 2

class ChoreListAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Date Info', {'fields': ['due_date'], 'classes': ['collapse']})
        ]
    inlines = [ChoreInline]

admin.site.register(ChoreList, ChoreListAdmin)