# Generated by Django 4.1.1 on 2022-09-12 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=20)),
                ('type_category', models.CharField(choices=[('1', 'Hortalizas'), ('2', 'Hierbas aromáticas'), ('3', 'Especias')], default='1', max_length=1)),
            ],
        ),
    ]
