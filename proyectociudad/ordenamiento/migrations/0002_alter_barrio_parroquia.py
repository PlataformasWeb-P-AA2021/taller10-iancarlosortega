# Generated by Django 3.2.4 on 2021-06-19 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ordenamiento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barrio',
            name='parroquia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barrios', to='ordenamiento.parroquia'),
        ),
    ]