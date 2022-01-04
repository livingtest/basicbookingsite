# Generated by Django 3.2.9 on 2021-12-20 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_agents'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agents',
            options={'verbose_name': 'agent', 'verbose_name_plural': 'agents'},
        ),
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
