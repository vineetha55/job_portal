# Generated by Django 4.1 on 2024-01-19 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=100, null=True)),
                ('categorystatus', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificationno', models.IntegerField(null=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('postalcode', models.CharField(max_length=100, null=True)),
                ('nameco', models.CharField(max_length=100, null=True)),
                ('mobileno', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('companyimage', models.ImageField(null=True, upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_jobpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtitle', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('jobtype', models.CharField(max_length=100, null=True)),
                ('schedule', models.CharField(max_length=100, null=True)),
                ('experiencelevel', models.CharField(max_length=100, null=True)),
                ('numberofopening', models.CharField(max_length=100, null=True)),
                ('hiringtimeline', models.CharField(max_length=100, null=True)),
                ('companyemail', models.EmailField(max_length=254, null=True)),
                ('companyaddress_city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('pincode', models.IntegerField(null=True)),
                ('websitelink', models.CharField(max_length=100, null=True)),
                ('minimum', models.CharField(max_length=100, null=True)),
                ('maximum', models.CharField(max_length=100, null=True)),
                ('rate', models.CharField(max_length=100, null=True)),
                ('jobdescription', models.CharField(max_length=100, null=True)),
                ('skills', models.CharField(max_length=100, null=True)),
                ('advanced', models.CharField(max_length=100, null=True)),
                ('beginner', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]