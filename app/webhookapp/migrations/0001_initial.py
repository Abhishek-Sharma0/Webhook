# Generated by Django 5.0.1 on 2024-02-02 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Webhook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=500)),
                ('created_at', models.CharField(max_length=500)),
                ('updated_at', models.CharField(max_length=500)),
                ('is_active', models.BooleanField()),
            ],
        ),
    ]
