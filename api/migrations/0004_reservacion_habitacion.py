# Generated by Django 4.2.6 on 2023-10-14 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_habitacion_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservacion',
            name='habitacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.habitacion'),
        ),
    ]
