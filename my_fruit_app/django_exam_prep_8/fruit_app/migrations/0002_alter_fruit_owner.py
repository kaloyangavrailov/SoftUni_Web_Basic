# Generated by Django 4.2.11 on 2024-04-16 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fruit_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruit',
            name='owner',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='fruit_app.profile'),
        ),
    ]
