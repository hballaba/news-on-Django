from django.contrib import admin

from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    #передаем поля, которые будут доступны в админке
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published', 'category')
    #устанавливаем ссылку на соответствующую запись модели. по умолчанию только id
    list_display_links = ('id', 'title')
    #устанавливаем поиск по полям
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter =    ('is_published', 'title')



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

#регистрация модели в админке
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)


