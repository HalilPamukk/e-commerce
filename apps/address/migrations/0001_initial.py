# Generated by Django 5.1.2 on 2024-11-25 12:37

import core.cache
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated At')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('data', models.JSONField(blank=True, default=dict, null=True)),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Name')),
                ('alpha2Code', models.CharField(blank=True, max_length=2, null=True, verbose_name='Alpha 2 Code')),
                ('alpha3Code', models.CharField(blank=True, max_length=3, null=True, verbose_name='Alpha 3 Code')),
                ('calling_code', models.CharField(blank=True, max_length=5, null=True, verbose_name='Calling Code')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_deleted_by', to=settings.AUTH_USER_MODEL, verbose_name='Deleted By')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'ordering': ['name'],
            },
            bases=(models.Model, core.cache.BaseCache),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated At')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('data', models.JSONField(blank=True, default=dict, null=True)),
                ('name', models.CharField(db_index=True, max_length=128, verbose_name='Name')),
                ('code', models.CharField(blank=True, max_length=32, null=True, verbose_name='Code')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_deleted_by', to=settings.AUTH_USER_MODEL, verbose_name='Deleted By')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='address.country', verbose_name='Country')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model, core.cache.BaseCache),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated At')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('data', models.JSONField(blank=True, default=dict, null=True)),
                ('name', models.CharField(blank=True, max_length=512, null=True, verbose_name='Region Name')),
                ('code', models.CharField(blank=True, max_length=32, null=True, verbose_name='Region Code')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_deleted_by', to=settings.AUTH_USER_MODEL, verbose_name='Deleted By')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regions',
                'ordering': ['name'],
            },
            bases=(models.Model, core.cache.BaseCache),
        ),
        migrations.AddField(
            model_name='country',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='address.region', verbose_name='Region'),
        ),
        migrations.CreateModel(
            name='Township',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated At')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('data', models.JSONField(blank=True, default=dict, null=True)),
                ('name', models.CharField(db_index=True, max_length=128, verbose_name='Name')),
                ('code', models.CharField(blank=True, max_length=32, null=True, verbose_name='Code')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='address.city', verbose_name='City')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_deleted_by', to=settings.AUTH_USER_MODEL, verbose_name='Deleted By')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model, core.cache.BaseCache),
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated At')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('data', models.JSONField(blank=True, default=dict, null=True)),
                ('name', models.CharField(db_index=True, max_length=128, verbose_name='Name')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_deleted_by', to=settings.AUTH_USER_MODEL, verbose_name='Deleted By')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
                ('township', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='address.township', verbose_name='Township')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model, core.cache.BaseCache),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated At')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('data', models.JSONField(blank=True, default=dict, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('address_title', models.CharField(max_length=128, verbose_name='Address Title')),
                ('address', models.TextField(verbose_name='Address')),
                ('postal_code', models.CharField(max_length=32, verbose_name='Postal Code')),
                ('phone', models.CharField(blank=True, help_text='Ex: 530 111 1111', max_length=32, null=True, verbose_name='Phone')),
                ('internal', models.CharField(blank=True, max_length=16, null=True, verbose_name='Internal')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Last Name')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_deleted_by', to=settings.AUTH_USER_MODEL, verbose_name='Deleted By')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='address.city', verbose_name='City')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='address.country', verbose_name='Country')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='address.district', verbose_name='District')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='address.region', verbose_name='Region')),
                ('township', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='address.township', verbose_name='Township')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
                'ordering': ['-created_at'],
            },
            bases=(models.Model, core.cache.BaseCache),
        ),
        migrations.AddConstraint(
            model_name='region',
            constraint=models.UniqueConstraint(fields=('name', 'code'), name='unique_region'),
        ),
    ]