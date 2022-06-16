from django.contrib import admin
from livros.models import Livro
from django.contrib.admin.filters import SimpleListFilter

# Register your models here.


class CustomFilter(SimpleListFilter):
    title = 'Filtrar livros'
    parameter_name = 'custom'

    def lookups(self, request, model_admin):
        return (
            ('titulo', 'Titulo'),
            ('autor', 'Autor'),
            ('ano', 'Ano'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'titulo':
            queryset = queryset.order_by('titulo')
        elif self.value() == 'autor':
            queryset = queryset.order_by('autor')
        elif self.value() == 'ano':
            queryset = queryset.order_by('ano')
        return queryset


class LivroAdmin(admin.ModelAdmin):
    list_filter = ['ano', CustomFilter]
    search_fields = ['titulo', 'autor', 'ano']


admin.site.register(Livro, LivroAdmin)
