# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-03 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shader',
            fields=[
                ('shader_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('shader_vertexColor', models.BooleanField()),
                ('shader_uvSet', models.IntegerField(default=1)),
                ('shader_surfaceType', models.IntegerField(choices=[(0, b'Opqaue'), (1, b'Transparent'), (2, b'Translucent')], default=0)),
                ('shader_complexity', models.IntegerField(default=1)),
                ('shader_textures', models.IntegerField(default=0)),
                ('shader_diffuseTex', models.IntegerField(default=0)),
                ('shader_normalTex', models.IntegerField(default=0)),
                ('shader_SMDTex', models.IntegerField(default=0)),
                ('shader_uvTint', models.BooleanField()),
                ('shader_maskTint', models.BooleanField()),
                ('shader_globalDirt', models.BooleanField()),
                ('shader_emissive', models.BooleanField()),
                ('shader_wetness', models.BooleanField()),
                ('shader_parallax', models.BooleanField()),
                ('shader_retroReflect', models.BooleanField()),
            ],
        ),
    ]
