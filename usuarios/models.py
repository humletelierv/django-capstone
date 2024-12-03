from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    rut = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=30)

    # Sobrescribe para eliminar la relación implícita
    groups = None
    user_permissions = None  # También puedes eliminar permisos si no los usas

    def __str__(self):
        return f"{self.username} ({self.rut})"

class UsuarioGroup(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Eliminación en cascada
    group = models.CharField(max_length=100)
    
class InfoHorno(models.Model):
    batch = models.CharField(max_length=22, primary_key=True)  # Definir BATCH como clave primaria
    fecha = models.DateField()
    variedad = models.CharField(max_length=40)
    
    temp_sobre_grano = models.FloatField()
    temp_bajo_tela = models.FloatField()
    temp_ambiente = models.FloatField()
    hr_sobre_tela = models.FloatField()
    
    p_apertura_damper = models.FloatField()
    presion_diferencial = models.FloatField()

    gas_total = models.DecimalField(max_digits=10, decimal_places=2)
    gas_et_1 = models.DecimalField(max_digits=10, decimal_places=2)
    gas_et_2 = models.DecimalField(max_digits=10, decimal_places=2)
    gas_et_3 = models.DecimalField(max_digits=10, decimal_places=2)
    gas_et_4 = models.DecimalField(max_digits=10, decimal_places=2)
    gas_et_5 = models.DecimalField(max_digits=10, decimal_places=2)
    gas_et_6 = models.DecimalField(max_digits=10, decimal_places=2)

    tiempo_total = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_barra_e1 = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_barra_e2 = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_barra_e3 = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_barra_e4 = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_barra_e5 = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_barra_e6 = models.DecimalField(max_digits=10, decimal_places=2)

    sp_temp_1 = models.DecimalField(max_digits=10, decimal_places=2)
    sp_temp_2 = models.DecimalField(max_digits=10, decimal_places=2)
    sp_temp_3 = models.DecimalField(max_digits=10, decimal_places=2)
    sp_temp_4 = models.DecimalField(max_digits=10, decimal_places=2)
    sp_temp_5 = models.DecimalField(max_digits=10, decimal_places=2)
    sp_temp_6 = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Batch: {self.batch} - Fecha: {self.fecha}"
    
    class Meta:
        db_table = 'INFO_HORNO'
        managed = False  # No permitir que Django administre esta tabla


from django.db import models

class InfoProduccion(models.Model):
    batch = models.PositiveIntegerField (primary_key=True)
    fecha_horneo = models.DateField()
    id_tipo_horno = models.PositiveIntegerField()
    tipo_variedad = models.CharField(max_length=60)
    id_tipo_malta = models.PositiveIntegerField()
    cebada_sucia = models.FloatField()
    impureza = models.PositiveIntegerField()
    polvo = models.PositiveIntegerField()
    cebada_limpia = models.FloatField()
    malta_sucia = models.PositiveIntegerField()
    brote = models.PositiveIntegerField()
    malta_limpia = models.PositiveIntegerField()
    malta_verde = models.PositiveIntegerField()
    materiaseca = models.PositiveIntegerField()
    malta_equivalente = models.PositiveIntegerField()
    fecha_volteo = models.DateField()
    fecha_pulido = models.DateField()
    electricidad = models.PositiveIntegerField()
    gas = models.PositiveIntegerField()
    agua = models.PositiveIntegerField()
    cs_cl = models.FloatField()
    cl_ml = models.FloatField()
    brote_ml = models.PositiveIntegerField()
    ms_ml = models.FloatField()
    cs_ml = models.FloatField()
    cl_ms = models.FloatField()
    factor_perdida_humedad = models.FloatField()
    factor_perdida_conversion = models.FloatField()
    kg_perdida_humedad = models.PositiveIntegerField()
    kg_perdida_conversion = models.PositiveIntegerField()
    kg_destino_2 = models.PositiveIntegerField()
    silo_destino_2 = models.PositiveIntegerField()
    kg_destino_1 = models.PositiveIntegerField()
    silo_destino_1 = models.PositiveIntegerField()
    kg_silo_origen_1 = models.PositiveIntegerField()
    silo_origen_1 = models.PositiveIntegerField()
    kg_silo_origen_2 = models.PositiveIntegerField()
    silo_origen_2 = models.PositiveIntegerField()

    class Meta:
        db_table = 'INFO_PRODUCCION'
        verbose_name = 'Información de Producción'
        verbose_name_plural = 'Información de Producción'
        managed = False  # No permitir que Django administre esta tabla


    def __str__(self):
        return f'Batch {self.batch} - Fecha: {self.fecha_horneo}'
    

class InfoAnalisis(models.Model):
    batch = models.IntegerField(primary_key=True)
    id_estado = models.IntegerField()
    id_tipo_malta = models.IntegerField()
    fecha_produccion = models.DateField()
    fecha_analisis = models.DateField()
    id_cliente = models.IntegerField()
    id_tipo_horno = models.IntegerField()
    proceso_tag = models.CharField(max_length=2)
    id_variedad = models.IntegerField()
    silo_origen = models.CharField(max_length=80)
    silo_destino_1 = models.CharField(max_length=40)
    malta_limpia = models.IntegerField()
    humedad = models.FloatField()
    tipo_sacarificacion = models.FloatField()
    ext_fino_ss = models.FloatField()
    ext_gru_ss = models.FloatField()
    fan = models.FloatField()
    id_analista = models.IntegerField()

    def __str__(self):
        return f"Batch: {self.batch}"
    
    class Meta:
        db_table = 'INFO_ANALISIS'
        managed = False  # No permitir que Django administre esta tabla


class InfoGerm(models.Model):
    cod_germ = models.IntegerField(primary_key=True)
    batch = models.IntegerField()
    dia = models.IntegerField()
    hora = models.IntegerField()
    rociador = models.IntegerField()
    tretorno = models.IntegerField()
    texterior = models.IntegerField()
    tinferior = models.IntegerField()
    tsuperior = models.IntegerField()
    cajongerminacion = models.IntegerField()
    horareloj = models.CharField(max_length=20)
    fecha = models.DateField()

    def __str__(self):
        return f"Batch: {self.batch}"
    
    class Meta:
        db_table = 'INFO_GERM'
        managed = False  # No permitir que Django administre esta tabla


class InfoTina(models.Model):
    cod_tina = models.IntegerField(primary_key=True)
    batch = models.IntegerField()
    fecha = models.DateField()
    hora = models.CharField(max_length=20)
    temptina1 = models.IntegerField()
    temptina2 = models.IntegerField()
    id_estado_tina = models.IntegerField()

    def __str__(self):
        return f"Batch: {self.batch}"
    
    class Meta:
        db_table = 'INFO_TINA'
        managed = False  # No permitir que Django administre esta tabla