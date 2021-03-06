# Generated by Django 3.1.5 on 2021-01-20 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(max_length=255)),
                ('first_description', models.TextField()),
                ('second_description', models.TextField()),
                ('third_description', models.TextField()),
                ('about_image', models.ImageField(upload_to='about')),
                ('conclusion', models.TextField()),
            ],
        ),
    ]
