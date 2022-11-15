from django.contrib import admin

from .models import Article, Tags, Scope

class ScopeInline(admin.TabularInline):
    model = Scope


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    list_display = ['title', 'text', 'published_at', 'image']
    list_filter = ['title']

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']
