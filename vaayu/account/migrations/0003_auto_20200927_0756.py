# Generated by Django 3.0.8 on 2020-09-27 02:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_auto_20200927_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donar',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='donations',
            name='ngo_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.NGO'),
        ),
        migrations.AlterField(
            model_name='requirements',
            name='ngo_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.NGO'),
        ),
    ]