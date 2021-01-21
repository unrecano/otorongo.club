# Generated by Django 3.1.4 on 2021-01-21 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0018_experiencialaboral'),
    ]

    operations = [
        migrations.CreateModel(
            name='CargoPartidario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idHVCargoPartidario', models.IntegerField(blank=True, null=True)),
                ('intItemCargoPartidario', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('idOrgPolCargoPartidario', models.IntegerField(blank=True, null=True)),
                ('strOrgPolCargoPartidario', models.TextField(blank=True, null=True)),
                ('strCargoPartidario', models.TextField(blank=True, null=True)),
                ('strAnioCargoPartiDesde', models.CharField(blank=True, max_length=5, null=True)),
                ('strAnioCargoPartiHasta', models.CharField(blank=True, max_length=5, null=True)),
                ('idEstado', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('strUsuario', models.CharField(blank=True, max_length=255, null=True)),
                ('strOrder', models.TextField(blank=True, null=True)),
                ('strComentario', models.TextField(blank=True, null=True)),
                ('election', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='votes.elections')),
                ('idHojaVida', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='votes.hojavida')),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='votes.person')),
            ],
        ),
    ]
