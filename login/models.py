from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    desc = models.CharField(max_length=140,blank=True)
    avatar = models.ImageField(upload_to='avatars/',default='avatars/default.png')

class Administrador(models.Model):
    id_vendedor = models.IntegerField(primary_key=True)
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    usuarios_id_usuario = models.IntegerField()
    foto = models.ImageField(upload_to="administradores",blank=True)

    class Meta:
        managed = False
        db_table = 'administrador'


class Agenda(models.Model):
    id_agenda = models.CharField(primary_key=True, max_length=15)
    fecha_hora = models.DateTimeField()
    motivo = models.CharField(max_length=15)
    estado = models.CharField(max_length=1)
    vendedor_id_vendedor = models.ForeignKey('Vendedor', models.DO_NOTHING, db_column='vendedor_id_vendedor')
    clientes_nro_telefono = models.ForeignKey('Clientes', models.DO_NOTHING, db_column='clientes_nro_telefono')

    class Meta:
        managed = False
        db_table = 'agenda'


class BandejaEntrada(models.Model):
    id_dashboard = models.CharField(primary_key=True, max_length=15)
    tabla_impresiones = models.IntegerField()
    tabla_clics = models.IntegerField()
    tabla_ctr = models.IntegerField()
    tabla_costo = models.IntegerField()
    anual = models.IntegerField()
    mensual = models.IntegerField()
    semanal = models.IntegerField()
    diario = models.IntegerField()
    clientes_nro_telefono = models.ForeignKey('Clientes', models.DO_NOTHING, db_column='clientes_nro_telefono')

    class Meta:
        managed = False
        db_table = 'bandeja_entrada'


class Clientes(models.Model):
    nro_telefono = models.CharField(primary_key=True, max_length=15)
    nombre_whatsapp = models.CharField(max_length=30)
    fecha_hora = models.DateTimeField()
    tipo_documento = models.CharField(max_length=15)
    nro_documento = models.CharField(max_length=15)
    nombre = models.CharField(max_length=30)
    pais = models.CharField(max_length=15)
    ciudad = models.CharField(max_length=30)
    direccion = models.CharField(max_length=20)
    usuarios_id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='usuarios_id_usuario')
    foto = models.ImageField(upload_to="vendedores",blank=True)

    class Meta:
        managed = False
        db_table = 'clientes'


class ConfiguracionDashboard(models.Model):
    id_dashboard = models.CharField(primary_key=True, max_length=15)
    tabla_impresiones = models.IntegerField()
    tabla_clics = models.IntegerField()
    tabla_ctr = models.IntegerField()
    tabla_costo = models.IntegerField()
    anual = models.IntegerField()
    mensual = models.IntegerField()
    semanal = models.IntegerField()
    diario = models.IntegerField()
    clientes_nro_telefono = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='clientes_nro_telefono')

    class Meta:
        managed = False
        db_table = 'configuracion_dashboard'


class DetalleVenta(models.Model):
    id_detalle = models.BigIntegerField(primary_key=True)
    cantidad = models.IntegerField()
    precio_actual = models.DecimalField(max_digits=6, decimal_places=2)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2)
    venta_id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='venta_id_venta')
    productos_id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='productos_id_producto')

    class Meta:
        managed = False
        db_table = 'detalle_venta'


class Mensaje(models.Model):
    id_mensaje = models.CharField(primary_key=True, max_length=15)
    fecha = models.DateField()
    hora = models.TimeField()
    texto_mensaje = models.TextField()
    tipo_mensaje = models.CharField(max_length=1)
    estado = models.IntegerField()
    venta_id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='venta_id_venta')
    clientes_nro_telefono = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='clientes_nro_telefono')
    nota_id_nota = models.ForeignKey('Nota', models.DO_NOTHING, db_column='nota_id_nota')

    class Meta:
        managed = False
        db_table = 'mensaje'


class Nota(models.Model):
    id_nota = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    texto_nota = models.TextField()
    tipo_nota = models.CharField(max_length=1)
    estado = models.IntegerField()
    administrador_id_vendedor = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='administrador_id_vendedor')
    vendedor_id_vendedor = models.ForeignKey('Vendedor', models.DO_NOTHING, db_column='vendedor_id_vendedor')

    class Meta:
        managed = False
        db_table = 'nota'


class Productos(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=15)
    categoria = models.CharField(max_length=20)
    descripcion = models.TextField()
    marca = models.CharField(max_length=20)
    precio_compra = models.DecimalField(max_digits=6, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    foto = models.ImageField(upload_to="productos",blank=True)
    fecha_ingreso = models.DateField()

    class Meta:
        managed = False
        db_table = 'productos'


class Usuarios(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nombre_usuario = models.CharField(max_length=30)
    contrasenia = models.CharField(max_length=30)
    administrador_id_vendedor = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='administrador_id_vendedor')
    vendedor_id_vendedor = models.ForeignKey('Vendedor', models.DO_NOTHING, db_column='vendedor_id_vendedor')
    foto = models.ImageField(upload_to="usuarios",blank=True)

    class Meta:
        managed = False
        db_table = 'usuarios'


class Vendedor(models.Model):
    id_vendedor = models.IntegerField(primary_key=True)
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    foto = models.ImageField(upload_to="vendedores",blank=True)


    class Meta:
        managed = False
        db_table = 'vendedor'


class Venta(models.Model):
    id_venta = models.BigIntegerField(primary_key=True)
    fecha_hora = models.DateTimeField()
    monto = models.DecimalField(max_digits=6, decimal_places=2)
    descuento = models.DecimalField(max_digits=6, decimal_places=2)
    forma_pago = models.CharField(max_length=1)
    tipo_comprobante = models.CharField(max_length=1)
    nro_comprobante = models.CharField(max_length=12)
    vendedor_id_vendedor = models.ForeignKey(Vendedor, models.DO_NOTHING, db_column='vendedor_id_vendedor')

    class Meta:
        managed = False
        db_table = 'venta'