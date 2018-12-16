from django.contrib import admin
from .models import Board, Post, Comment


class BoardAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['x', 'name']})
    ]
    list_display = ('x', 'name')
    search_fields = ['name']


admin.site.register(Board, BoardAdmin)
admin.site.register(Post)
admin.site.register(Comment)
