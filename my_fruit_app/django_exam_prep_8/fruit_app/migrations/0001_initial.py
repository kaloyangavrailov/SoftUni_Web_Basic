# Generated by Django 4.2.11 on 2024-04-16 07:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_exam_prep_8.fruit_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(2), django_exam_prep_8.fruit_app.models.check_starts_with_letter])),
                ('last_name', models.CharField(max_length=35, validators=[django.core.validators.MinLengthValidator(1), django_exam_prep_8.fruit_app.models.check_starts_with_letter])),
                ('email', models.EmailField(max_length=40, unique=True)),
                ('password', models.CharField(help_text='*Password length requirements: 8 to 20 characters', max_length=20, validators=[django.core.validators.MinLengthValidator(8)])),
                ('image_url', models.URLField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, default=18, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(2), django_exam_prep_8.fruit_app.models.check_only_letters])),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('nutrition', models.TextField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fruit_app.profile')),
            ],
        ),
        migrations.AddConstraint(
            model_name='fruit',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_constraint_name', violation_error_message='"This fruit name is already in use! Try a new one."'),
        ),
    ]
