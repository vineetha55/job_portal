# Generated by Django 4.1 on 2024-01-19 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portalapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_company',
            old_name='nameco',
            new_name='company_name',
        ),
        migrations.AddField(
            model_name='tbl_company',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tbl_company',
            name='industry',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tbl_company',
            name='nominal_capital',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tbl_company',
            name='owner',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tbl_company',
            name='website',
            field=models.CharField(max_length=100, null=True),
        ),
    ]