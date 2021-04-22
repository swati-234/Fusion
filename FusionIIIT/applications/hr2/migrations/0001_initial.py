# Generated by Django 3.1.5 on 2021-04-22 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('globals', '0003_auto_20191024_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForeignService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, max_length=6, null=True)),
                ('end_date', models.DateField(blank=True, max_length=6, null=True)),
                ('job_title', models.CharField(default='', max_length=50)),
                ('organisation', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=300)),
                ('salary_source', models.CharField(default='', max_length=100)),
                ('designation', models.CharField(default='', max_length=100)),
                ('service_type', models.CharField(choices=[('LIEN', 'LIEN'), ('DEPUTATION', 'DEPUTATION'), ('OTHER', 'OTHER')], max_length=100)),
                ('extra_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(default='', max_length=40)),
                ('mother_name', models.CharField(default='', max_length=40)),
                ('religion', models.CharField(default='', max_length=40)),
                ('category', models.CharField(choices=[('SC', 'SC'), ('ST', 'ST'), ('OBC', 'OBC'), ('GENERAL', 'GENERAL'), ('PWD', 'PWD')], max_length=50)),
                ('cast', models.CharField(default='', max_length=40)),
                ('home_state', models.CharField(default='', max_length=40)),
                ('home_district', models.CharField(default='', max_length=40)),
                ('date_of_joining', models.DateField(blank=True, null=True)),
                ('designation', models.CharField(default='', max_length=40)),
                ('blood_group', models.CharField(choices=[('AB+', 'AB+'), ('O+', 'O+'), ('AB-', 'AB-'), ('B+', 'B+'), ('B-', 'B-'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-')], max_length=50)),
                ('extra_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
        ),
        migrations.CreateModel(
            name='EmpDependents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=50)),
                ('dob', models.DateField(max_length=6, null=True)),
                ('relationship', models.CharField(default='', max_length=40)),
                ('extra_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
        ),
        migrations.CreateModel(
            name='EmpConfidentialDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar_no', models.IntegerField(default=0)),
                ('maritial_status', models.CharField(choices=[('MARRIED', 'MARRIED'), ('UN-MARRIED', 'UN-MARRIED'), ('WIDOW', 'WIDOW')], max_length=50)),
                ('bank_account_no', models.IntegerField(default=0)),
                ('salary', models.IntegerField(default=0)),
                ('extra_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
        ),
        migrations.CreateModel(
            name='EmpAppraisalForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField(blank=True, max_length=6, null=True)),
                ('appraisal_form', models.FileField(default=' ', null=True, upload_to='Hr2/appraisal_form')),
                ('extra_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
        ),
    ]