# Generated by Django 2.2.6 on 2020-03-22 20:36

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
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_from', models.CharField(max_length=75)),
                ('number_to', models.CharField(max_length=75)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
