# Generated by Django 5.0.6 on 2024-06-20 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title1', models.CharField(max_length=50)),
                ('about_title2', models.CharField(max_length=50)),
                ('about_img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
