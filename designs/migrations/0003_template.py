# Generated by Django 5.1.7 on 2025-04-14 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0002_rename_custmor_design_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('movies', 'Movies'), ('music', 'Music'), ('quotes', 'Quotes'), ('family', 'Family'), ('gamers', 'Gamers'), ('sports', 'Sports'), ('funny', 'Funny'), ('spooky', 'Spooky')], max_length=50)),
                ('image', models.ImageField(upload_to='templates/')),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
