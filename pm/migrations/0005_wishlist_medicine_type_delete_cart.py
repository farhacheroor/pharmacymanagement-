# Generated by Django 4.1.1 on 2023-03-25 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0004_cart_price_alter_cart_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cust_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pm.customer')),
                ('med_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pm.pharmacy')),
            ],
        ),
        migrations.AddField(
            model_name='medicine',
            name='type',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='cart',
        ),
    ]
