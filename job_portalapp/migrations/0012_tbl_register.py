# Generated by Django 4.1.5 on 2024-02-04 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portalapp', '0011_alter_tbl_jobpost_hiringtimeline'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]