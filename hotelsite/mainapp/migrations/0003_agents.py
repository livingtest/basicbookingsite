# Generated by Django 3.2.9 on 2021-12-15 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('numoflisting', models.IntegerField()),
                ('agentdescription', models.TextField(max_length=255)),
                ('agentphoto', models.ImageField(upload_to='agents')),
            ],
        ),
    ]
