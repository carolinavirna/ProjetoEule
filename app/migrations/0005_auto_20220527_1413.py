# Generated by Django 3.2.13 on 2022-05-27 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_classificacaoadmin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ClassificacaoAdmin',
        ),
        migrations.RemoveField(
            model_name='classificacao',
            name='id_questao',
        ),
    ]
