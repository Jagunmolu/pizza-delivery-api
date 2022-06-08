# Generated by Django 4.0.5 on 2022-06-04 21:44

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
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('SMALL', 'small'), ('MEDIUM', 'medium'), ('LARGE', 'large'), ('EXTRA_LARGE', 'extra_large')], max_length=20)),
                ('order_status', models.CharField(choices=[('PENDING', 'pending'), ('IN_TRANSIT', 'in_transit'), ('DELIVERED', 'delivered')], max_length=20)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
