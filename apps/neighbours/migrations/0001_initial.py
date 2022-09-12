# Generated by Django 4.1.1 on 2022-09-12 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_neighbour', models.CharField(choices=[('B', 'Beneficioso'), ('P', 'Perjudicial')], default='B', max_length=30)),
                ('description_neigh', models.TextField(max_length=600)),
                ('id_crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crop.crop')),
            ],
        ),
    ]