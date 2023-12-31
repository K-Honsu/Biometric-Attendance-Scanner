# Generated by Django 4.2.2 on 2023-06-19 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=450)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('grade', models.CharField(choices=[('grade1', 'Grade1'), ('grade2', 'Grade2'), ('grade3', 'Grade3'), ('grade4', 'Grade4')], max_length=6)),
                ('subject', models.CharField(choices=[('mathematics', 'Mathematics'), ('english', 'English'), ('computer science', 'Computer Science'), ('business studies', 'Business Studies'), ('physics', 'Physics'), ('chemistry', 'Chemistry'), ('biology', 'Biology'), ('arts', 'Arts'), ('commercial', 'Commercial')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=450)),
                ('date_of_birth', models.DateField()),
                ('father_name', models.CharField(max_length=150)),
                ('mother_name', models.CharField(max_length=150)),
                ('parent_phone_number', models.CharField(max_length=15)),
                ('contact_number', models.CharField(max_length=15)),
                ('parent_email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
