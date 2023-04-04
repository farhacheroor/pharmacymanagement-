from django.db import models

class login(models.Model):
    username=models.CharField(max_length=60)
    password=models.CharField(max_length=60)
    type=models.CharField(max_length=60)


class pharmacy(models.Model):
    login_id = models.ForeignKey(login, on_delete=models.CASCADE)
    pharmacy_name = models.CharField(max_length=60)
    pharmacist_name = models.CharField(max_length=60)
    phone = models.BigIntegerField()
    Reg_no = models.BigIntegerField()
    email = models.CharField(max_length=60)
    place = models.CharField(max_length=60)

class customer(models.Model):
    login_id = models.ForeignKey(login, on_delete=models.CASCADE)
    cust_name = models.CharField(max_length=60)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=60)
    place = models.CharField(max_length=60)
    house_name = models.CharField(max_length=60)
    post = models.CharField(max_length=60)

class medicine(models.Model):
    pharmacy_id = models.ForeignKey(pharmacy, on_delete=models.CASCADE)
    ref_no = models.BigIntegerField()
    med_name = models.CharField(max_length=60)
    company_name = models.CharField(max_length=60)
    med_type = models.CharField(max_length=60)
    uses = models.CharField(max_length=60)
    side_effect = models.CharField(max_length=60)
    prec_warning = models.CharField(max_length=60)
    dosage = models.CharField(max_length=60)
    lot_no = models.BigIntegerField()
    tablet_price = models.BigIntegerField()
    tablet_quantity = models.BigIntegerField()
    issue_date = models.DateField()
    exp_date = models.DateField()
    type = models.CharField(max_length=60)

class Image(models.Model):
    image = models.ImageField(upload_to='images/')