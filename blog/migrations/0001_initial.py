# Generated by Django 4.1.5 on 2023-02-13 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, default='my.jpeg', null=True, upload_to='')),
                ('category', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=100)),
                ('Content', models.CharField(max_length=2000)),
            ],
        ),
    ]
