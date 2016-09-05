# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 18:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cedente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=14)),
                ('banco', models.CharField(max_length=3)),
                ('agencia', models.CharField(max_length=5)),
                ('agencia_dv', models.CharField(max_length=1)),
                ('conta', models.CharField(max_length=12)),
                ('conta_dv', models.CharField(max_length=1)),
                ('convenio', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=14)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=11)),
                ('multa', models.DecimalField(decimal_places=2, max_digits=5)),
                ('juros', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boleto.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Prestacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_vencimento', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=11)),
                ('data_pagamento', models.DateField()),
                ('valor_multa', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valor_juros', models.DecimalField(decimal_places=2, max_digits=5)),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boleto.Contrato')),
            ],
        ),
        migrations.CreateModel(
            name='Sacado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=14)),
                ('nome', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('uf', models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='contrato',
            name='sacado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boleto.Sacado'),
        ),
        migrations.AddField(
            model_name='cedente',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boleto.Cliente'),
        ),
    ]