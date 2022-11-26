from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить

            is_main = form.cleaned_data
            print(is_main)
            if is_main.get('is_main') == True:
                count += 1
        if count > 1:
            raise ValidationError('Основным может быть только один тег, снимите лишние галочки')
            return super().clean()  # вызываем базовый код переопределяемого метода
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    list_display = ['title', 'text', 'published_at', 'image']
    list_filter = ['title']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
