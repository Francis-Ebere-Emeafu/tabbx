# Generated by Django 4.2.8 on 2023-12-29 22:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('surname', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('state', models.CharField(blank=True, choices=[('ANP', 'Andhra Pradesh'), ('ARP', 'Arunachal Pradesh'), ('ASS', 'Assam'), ('BIH', 'Bihar'), ('CHH', 'Chhattisgarh'), ('GOA', 'Goa'), ('GUJ', 'Gujarat'), ('HAR', 'Haryana'), ('HIP', 'Himachal Pradesh'), ('JHA', 'Jharkhand'), ('KAR', 'Karnataka'), ('KER', 'Kerala'), ('MAD', 'Madhya Pradesh'), ('MAH', 'Maharashtra'), ('MAN', 'Manipur'), ('MEG', 'Meghalaya'), ('MIZ', 'Mizoram'), ('NAG', 'Nagaland'), ('ODI', 'Odisha'), ('PUN', 'Punjab'), ('RAJ', 'Rajasthan'), ('SIK', 'Sikkim'), ('TAM', 'Tamil Nadu'), ('TEL', 'Telangana'), ('TRI', 'Tripura'), ('UTP', 'Uttar Pradesh'), ('UTT', 'Uttarakhand'), ('WEB', 'West Bengal'), ('ANI', 'Andaman and Nicobar Islands'), ('CHA', 'Chandigarh'), ('DNH', 'Dadra and Nagar Haveli and Daman and Diu'), ('LAK', 'Lakshadweep'), ('DEL', 'Delhi - National Capital Territory of Delhi'), ('PUD', 'Puducherry'), ('JAK', 'Jammu and Kashmir'), ('LAD', 'Ladakh')], max_length=3, null=True)),
                ('school', models.CharField(blank=True, max_length=20, null=True)),
                ('confirm_email', models.BooleanField(default=False)),
                ('date_registered', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('surname', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('available', models.BooleanField(default=False)),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('confirm_email', models.BooleanField(default=False)),
                ('date_registered', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
