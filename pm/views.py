from django.contrib import auth
from django.contrib.auth import login
from django.http import request, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from pm.models import *




def main(request):
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def logins(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    lob = login.objects.get(username=username, password=password)
    if lob.type=='customer':
        return render(request, 'custindex.html')
    else:
        return render(request, 'pharmacyindex.html')
def regcust(request):
    return render(request,'signup_cust.html')
def regpharmacy(request):
    return render(request, 'signup_pharmacy.html')
def signup_cust(request):
    name=request.POST['textfield']
    phone=request.POST['textfield2']
    email=request.POST['textfield3']
    place=request.POST['textfield4']
    house_name=request.POST['textfield5']
    post = request.POST['textfield6']
    username=request.POST['textfield7']
    password=request.POST['textfield8']
    lob=login()
    lob.username=username
    lob.password=password
    lob.type='customer'
    lob.save()
    bob=customer()
    bob.login_id=lob
    bob.cust_name=name
    bob.phone=phone
    bob.email=email
    bob.place=place
    bob.house_name=house_name
    bob.post=post
    bob.save()
    return HttpResponse('''<script>alert("REGISTERED");window.location='/'</script>''')
def signup_pharmacy(request):
    pharmacy_name=request.POST['textfield']
    pharmacist_name=request.POST['textfield2']
    phone=request.POST['textfield3']
    reg_no=request.POST['textfield4']
    email=request.POST['textfield5']
    place = request.POST['textfield6']
    username=request.POST['textfield7']
    password=request.POST['textfield8']
    pob=login()
    pob.username=username
    pob.password=password
    pob.type='pharmacy'
    pob.save()
    phob=pharmacy()
    phob.login_id=pob
    phob.pharmacy_name=pharmacy_name
    phob.pharmacist_name=pharmacist_name
    phob.phone=phone
    phob.Reg_no=reg_no
    phob.email=email
    phob.place=place
    phob.save()
    return HttpResponse('''<script>alert("REGISTER");window.location='/'</script>''')
def add_med(request):
    pharmacy_name=request.POST['select']
    ref_no=request.POST['textfield']
    med_name=request.POST['textfield2']
    company_name=request.POST['textfield3']
    med_type = request.POST['textfield4']
    uses = request.POST['textfield5']
    side_effect = request.POST['textfield6']
    prec_warning = request.POST['textfield7']
    dosage = request.POST['textfield8']
    lot_no = request.POST['textfield9']
    tablet_price = request.POST['textfield10']
    tablet_quantity = request.POST['textfield11']
    issue_date = request.POST['textfield12']
    exp_date = request.POST['textfield13']
    sob=medicine()
    sob.pharmacy_id=pharmacy.objects.get(id=pharmacy_name)
    sob.ref_no=ref_no
    sob.type='medicine'
    sob.med_name=med_name
    sob.company_name=company_name
    sob.med_type = med_type
    sob.uses = uses
    sob.side_effect = side_effect
    sob.prec_warning = prec_warning
    sob.dosage = dosage
    sob.lot_no = lot_no
    sob.tablet_price = tablet_price
    sob.tablet_quantity = tablet_quantity
    sob.issue_date = issue_date
    sob.exp_date = exp_date
    sob.save()
    return HttpResponse('''<script>alert("SUCCESSFULL");window.location='/home'</script>''')
def addmed(request):
    obg=pharmacy.objects.all()
    return render(request,'addmed.html',{"gval":obg})
def home(request):
    return render(request,'home_page.html')
def homecust(request):
    return render(request,'homecust.html')
def vmed(request):
    obv=medicine.objects.filter(type='medicine')
    return render(request,'viewmed.html',{"b":obv})
def searchmed(request):
    btn=request.POST['Submit']
    if btn=="SEARCH":
        medicine1=request.POST['select']
        obn=medicine.objects.filter(pharmacy_id__id=medicine1)
        obt = pharmacy.objects.all()
        return render(request,'custmedview.html',{"nval":obn,"tim":obt,'tm':int(medicine1)})

def search(request):
    obt=pharmacy.objects.all()
    return render(request,'custmedview.html',{"tim":obt})
def delete(request,id):
    obd=medicine.objects.get(id=id)
    obd.delete()
    return HttpResponse('''<script>alert("DELETED");window.location='/home'</script>''')
def updates(request,id):
    ob=medicine.objects.get(id=id)
    request.session['oid']=ob.id
    return render(request,"update.html",{'val':ob})
def edit(request):
    tablet_price=request.POST['textfield10']
    tablet_quantity= request.POST['textfield11']
    issue_date = request.POST['textfield12']
    exp_date = request.POST['textfield13']
    ob1 = medicine.objects.get(id=request.session['oid'])
    ob1.tablet_price=tablet_price
    ob1.tablet_quantity=tablet_quantity
    ob1.issue_date=issue_date
    ob1.exp_date=exp_date
    ob1.save()
    return HttpResponse('''<script>alert("UPDATED");window.location='/home'</script>''')
def outstock(request,id):
    obu=medicine.objects.get(id=id)
    obu.type='outstock'
    obu.save()
    return HttpResponse('''<script>alert("OUTSTOCK");window.location='/home'</script>''')
def instock(request,id):
    obu=medicine.objects.get(id=id)
    obu.type='medicine'
    obu.save()
    return HttpResponse('''<script>alert("INSTOCK");window.location='/home'</script>''')
def outstocks(request):
    obv=medicine.objects.filter(type='outstock')
    return render(request,'outstock.html',{"g":obv})
def order(request,id):
    ob=medicine.objects.get(id=id)
    request.session['oid']=ob.id
    return render(request,"order.html",{'val':ob})
def placeorder(request):
    name=request.POST['textfield7']
    address= request.POST['textfield8']
    phone = request.POST['textfield9']
    med_name = request.POST['textfield10']
    tablet_quantity = request.POST['textfield11']
    prescription = request.POST['image']
    ob1 = medicine.objects.get(id=request.session['oid'])
    ob1.med_name=med_name
    ob1.tablet_quantity=tablet_quantity
    ob1.prescription=prescription
    ob1.name = name
    ob1.house_name = address
    ob1.phone = phone
    ob1.save()
    return HttpResponse('''<script>alert("ORDER PLACED");window.location='/homecust'</script>''')