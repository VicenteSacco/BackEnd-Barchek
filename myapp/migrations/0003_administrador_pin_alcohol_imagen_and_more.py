# Generated by Django 5.2.2 on 2025-06-14 22:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_administrador_options_alter_alcohol_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrador',
            name='pin',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='alcohol',
            name='imagen',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='barra',
            name='idadministrador',
            field=models.ForeignKey(blank=True, db_column='idadministrador', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.administrador'),
        ),
        migrations.AddField(
            model_name='barra',
            name='idlista',
            field=models.ForeignKey(blank=True, db_column='idlista', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.listadealcohol'),
        ),
        migrations.AddField(
            model_name='listaaalcohol',
            name='idalcohol',
            field=models.ForeignKey(blank=True, db_column='idalcohol', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.alcohol'),
        ),
        migrations.AddField(
            model_name='listaaalcohol',
            name='idlista',
            field=models.ForeignKey(blank=True, db_column='idlista', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.listadealcohol'),
        ),
        migrations.AddField(
            model_name='reporte',
            name='idbarra',
            field=models.ForeignKey(blank=True, db_column='idbarra', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.barra'),
        ),
        migrations.AlterUniqueTogether(
            name='listaaalcohol',
            unique_together={('idlista', 'idalcohol')},
        ),
        migrations.AlterUniqueTogether(
            name='reporte',
            unique_together={('idbarra', 'fecha')},
        ),
    ]
