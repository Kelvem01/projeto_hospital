# Generated by Django 4.2.7 on 2023-11-24 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anestesista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('cpf', models.CharField(blank=True, max_length=15, null=True)),
                ('crm', models.CharField(blank=True, max_length=15, null=True)),
                ('data_cadastro', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Anestesista',
            },
        ),
        migrations.CreateModel(
            name='Cirurgiao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('cpf', models.CharField(blank=True, max_length=15, null=True)),
                ('crm', models.CharField(blank=True, max_length=15, null=True)),
                ('data_cadastro', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Cirurgiao',
            },
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
    ]
