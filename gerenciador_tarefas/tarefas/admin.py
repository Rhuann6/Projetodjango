from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'criado_em', 'atualizado_em')
    list_filter = ('status',)
    search_fields = ('titulo', 'descricao')