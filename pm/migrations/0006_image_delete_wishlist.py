# Generated by Django 4.1.1 on 2023-03-29 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0005_wishlist_medicine_type_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='wishlist',
        ),
    ]