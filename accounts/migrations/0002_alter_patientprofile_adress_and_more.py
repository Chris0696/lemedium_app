# Generated by Django 5.0.1 on 2024-02-26 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientprofile',
            name='adress',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='adress'),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='date_of_birth'),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='profile_image',
            field=models.ImageField(blank=True, default='profiles/user-default.png', null=True, upload_to='profiles/customers_profile', verbose_name='profile_image'),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Username'),
        ),
    ]