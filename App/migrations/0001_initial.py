# Generated by Django 4.2.1 on 2023-05-31 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('image', models.ImageField(blank=True, default='default/def.jpg', null=True, upload_to='Profile_pic/')),
                ('Email', models.EmailField(blank=True, max_length=20, null=True)),
                ('age', models.PositiveIntegerField()),
                ('address', models.TextField(blank=True, max_length=200, null=True)),
                ('phone_no', models.TextField(blank=True, max_length=15, null=True)),
                ('date_of_birth', models.TextField(blank=True, max_length=12, null=True)),
                ('religion', models.CharField(choices=[('Muslim', 'Muslim'), ('Hindu', 'Hindu'), ('Christian', 'Christian'), ('Bouddho', 'Bouddho')], max_length=9)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=6)),
            ],
        ),
    ]
