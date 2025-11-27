from django.contrib import admin
from.models import Produto, Categoria, Contato, Pagina
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'estoque')
    search_fields = ('nome',)
    list_filter = ('categoria', )

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'mensagem')
    search_fields = ('nome',)


class PaginaAdmin(admin.ModelAdmin):
    list_display = ('nome_Site',)
    search_fields = ('nome_Site',)


admin.site.register(Contato, ContatoAdmin)
admin.site.register(Produto)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Pagina, PaginaAdmin)

