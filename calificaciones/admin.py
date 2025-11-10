from django.contrib import admin
from .models import CalificacionTributaria, Corredor

# --- CONFIGURACIÓN PARA EL MODELO CORREDOR ---
@admin.register(Corredor)
class CorredorAdmin(admin.ModelAdmin):
    # Se añade 'usuario' para ver quién está vinculado
    list_display = ('nombre', 'codigo_corredor', 'activo', 'usuario')
    search_fields = ('nombre', 'codigo_corredor', 'usuario__username')
    
    # Hacer que 'usuario' sea un campo de autocompletar
    autocomplete_fields = ['usuario']
    
    # Organización de la vista
    fieldsets = (
        ('Datos del Corredor', {'fields': ('nombre', 'codigo_corredor', 'activo')}),
        ('Vínculo de Seguridad', {'fields': ('usuario',)}),
    )

# --- CONFIGURACIÓN PARA EL MODELO CALIFICACIÓN TRIBUTARIA ---
@admin.register(CalificacionTributaria)
class CalificacionTributariaAdmin(admin.ModelAdmin):
    list_display = (
        'instrumento', 
        'fecha', 
        'corredor', # Se muestra a qué corredor está relacionada
        'tipo_mercado', 
        'fuente_ingreso',
        'fecha_modificacion',
        'origen',
    )
    
    list_filter = (
        'corredor', # Posibilidad de filtrar por corredor
        'tipo_mercado', 
        'fuente_ingreso',
        'origen',
        'fecha_modificacion',
    )
    
    search_fields = ('instrumento', 'secuencia', 'corredor__nombre', 'descripcion_dividendo')
    
    # campo 'corredor' de solo lectura
    readonly_fields = ('fecha_modificacion',)

    
    fieldsets = (
        ('Datos de Identificación', {
            'fields': (
                'corredor', 
                'instrumento', 
                'instrumento_no_inscrito', 
                'fecha',
                'tipo_mercado',
                'descripcion_dividendo',
                'acogido_isfut',
                'origen',
                'factor_actualizacion',
                'fuente_ingreso',
                'secuencia', 
                'numero_dividendo', 
                'tipo_sociedad', 
                'valor_historico'
            )
        }),
        ('Fechas de Auditoría', {
            'classes': ('collapse',),
            'fields': ('fecha_modificacion',)
        }),
        ('Factores Tributarios', {
            'classes': ('collapse',),
            'fields': (
                ('factor_8', 'factor_9', 'factor_10'),
                ('factor_11', 'factor_12', 'factor_13'),
                ('factor_14', 'factor_15', 'factor_16'),
                ('factor_17', 'factor_18', 'factor_19'),
                ('factor_20', 'factor_21', 'factor_22'),
                ('factor_23', 'factor_24', 'factor_25'),
                ('factor_26', 'factor_27', 'factor_28'),
                ('factor_29', 'factor_30', 'factor_31'),
                ('factor_32', 'factor_33', 'factor_34'),
                ('factor_35', 'factor_36', 'factor_37'),
            )
        }),
    )
