# Generated by Django 2.1.1 on 2018-11-19 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=20)),
                ('quartier', models.CharField(max_length=50)),
                ('ecole', models.CharField(max_length=50)),
                ('classe', models.CharField(max_length=20)),
                ('matiere', models.CharField(max_length=30)),
            ],
        ),
    ]
