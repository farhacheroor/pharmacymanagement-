# Generated by Django 4.1.1 on 2023-03-04 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=60)),
                ('type', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pharmacy_name', models.CharField(max_length=60)),
                ('pharmacist_name', models.CharField(max_length=60)),
                ('phone', models.BigIntegerField()),
                ('Reg_no', models.BigIntegerField()),
                ('email', models.CharField(max_length=60)),
                ('place', models.CharField(max_length=60)),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pm.login')),
            ],
        ),
        migrations.CreateModel(
            name='medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_no', models.BigIntegerField()),
                ('med_name', models.CharField(max_length=60)),
                ('company_name', models.CharField(max_length=60)),
                ('med_type', models.CharField(max_length=60)),
                ('uses', models.CharField(max_length=60)),
                ('side_effect', models.CharField(max_length=60)),
                ('prec_warning', models.CharField(max_length=60)),
                ('dosage', models.CharField(max_length=60)),
                ('lot_no', models.BigIntegerField()),
                ('tablet_price', models.BigIntegerField()),
                ('tablet_quantity', models.BigIntegerField()),
                ('issue_date', models.DateField()),
                ('exp_date', models.DateField()),
                ('pharmacy_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pm.pharmacy')),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=60)),
                ('phone', models.BigIntegerField()),
                ('email', models.CharField(max_length=60)),
                ('place', models.CharField(max_length=60)),
                ('house_name', models.CharField(max_length=60)),
                ('post', models.CharField(max_length=60)),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pm.login')),
            ],
        ),
    ]
