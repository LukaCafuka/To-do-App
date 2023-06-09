# Generated by Django 4.1.5 on 2023-04-27 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=40)),
                ('completed', models.BooleanField(default='False')),
            ],
            options={
                'verbose_name': 'Todo',
                'verbose_name_plural': 'Todos',
            },
        ),
    ]
