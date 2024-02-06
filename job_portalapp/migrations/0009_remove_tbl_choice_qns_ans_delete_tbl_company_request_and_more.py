# Generated by Django 4.1.5 on 2024-02-04 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portalapp', '0008_tbl_questionanswer_choice1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_choice',
            name='qns_ans',
        ),
        migrations.DeleteModel(
            name='tbl_company_request',
        ),
        migrations.AddField(
            model_name='tbl_company',
            name='status',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='tbl_choice',
        ),
    ]