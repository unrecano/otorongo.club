# Generated by Django 3.1.4 on 2021-01-15 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0014_eduposgrado_strcomentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='compiledorg',
            name='postula_distrito',
            field=models.TextField(db_index=True, null=True),
        ),
    ]
