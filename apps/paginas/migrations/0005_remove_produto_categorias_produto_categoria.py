# Generated by Django 5.1.1 on 2024-09-27 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0004_produto_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='categorias',
        ),
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.CharField(choices=[('CALÇA', 'Calça'), ('BLUSA', 'Blusa'), ('Short', 'Short')], default='', max_length=150),
        ),
    ]
