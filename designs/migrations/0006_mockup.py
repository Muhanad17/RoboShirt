# Generated by Django 5.1.7 on 2025-04-16 13:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0005_merge_20250414_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mockup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('white', 'White'), ('black', 'Black'), ('red', 'Red'), ('blue', 'Blue'), ('green', 'Green'), ('yellow', 'Yellow'), ('purple', 'Purple'), ('gray', 'Gray')], max_length=20)),
                ('size', models.CharField(choices=[('xs', 'XS'), ('s', 'S'), ('m', 'M'), ('l', 'L'), ('xl', 'XL'), ('xxl', 'XXL')], max_length=10)),
                ('mockup_image', models.ImageField(upload_to='mockups/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('design', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mockups', to='designs.design')),
            ],
        ),
    ]
