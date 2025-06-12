from django.db import models


class Administrador(models.Model):
    correoelectronico = models.CharField(unique=True, max_length=100)
    contrasena = models.CharField(max_length=100)

    class Meta:
        db_table = 'administrador'


class Alcohol(models.Model):
    stockactual = models.IntegerField()
    cantidadunidad = models.CharField(max_length=50)
    ano = models.IntegerField(blank=True, null=True)
    categoria = models.CharField(max_length=50, blank=True, null=True)
    ia = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    marca = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'alcohol'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Barra(models.Model):
    nombrebarra = models.CharField(max_length=100)
    idadministrador = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='idadministrador')
    idlista = models.ForeignKey('Listadealcohol', models.DO_NOTHING, db_column='idlista')

    class Meta:
        db_table = 'barra'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Listaaalcohol(models.Model):
    pk = models.CompositePrimaryKey('idlista', 'idalcohol')
    idlista = models.ForeignKey('Listadealcohol', models.DO_NOTHING, db_column='idlista')
    idalcohol = models.ForeignKey(Alcohol, models.DO_NOTHING, db_column='idalcohol')

    class Meta:
        db_table = 'listaaalcohol'


class ListaDeAlcohol(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = 'listadealcohol'


class Reporte(models.Model):
    fecha = models.DateField()
    bartender = models.CharField(max_length=100)
    idbarra = models.ForeignKey(Barra, models.DO_NOTHING, db_column='idbarra')

    class Meta:
        db_table = 'reporte'
        unique_together = (('idbarra', 'fecha'),)