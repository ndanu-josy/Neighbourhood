# Generated by Django 3.2.5 on 2021-07-24 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighapp', '0002_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=100)),
                ('business_email', models.CharField(max_length=50)),
                ('neighbourhood_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='neighapp.neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_owner', to='neighapp.userprofile')),
            ],
        ),
    ]
