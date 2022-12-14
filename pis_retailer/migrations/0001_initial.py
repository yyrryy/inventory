# Generated by Django 3.0.7 on 2022-11-25 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Retailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('package', models.CharField(blank=True, max_length=200, null=True)),
                ('package_price', models.CharField(blank=True, max_length=200, null=True)),
                ('package_expiry', models.DateField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, max_length=1024, null=True, upload_to='images/retailer/logo/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RetailerUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_type', models.CharField(choices=[('owner', 'Owner'), ('data_entry_user', 'Data Entry User'), ('salesman', 'Salesman'), ('account_viewer', 'Account Viewer'), ('ledger_viewer', 'Ledger Viewer')], default='owner', max_length=100)),
                ('retailer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_retailer', to='pis_retailer.Retailer')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='retailer_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
