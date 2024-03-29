# Generated by Django 4.1.5 on 2024-02-04 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_portalapp', '0005_tbl_company_request'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_Mock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=20, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='job_portalapp.tbl_category')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_QuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(null=True)),
                ('answer', models.TextField(null=True)),
                ('mock', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='job_portalapp.tbl_mock')),
            ],
        ),
    ]
