# Generated by Django 3.1.4 on 2021-01-10 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0013_eduuniversitaria_strcomentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='eduposgrado',
            name='strComentario',
            field=models.TextField(blank=True, null=True),
        ),
    ]