from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from pm import views

urlpatterns=[
    path('',views.main,name='main'),
    path('signup_cust',views.signup_cust,name='signup_cust'),
    path('signup_pharmacy',views.signup_pharmacy,name='signup_pharmacy'),
    path('signup',views.signup,name='signup'),
    path('regcust',views.regcust,name='regcust'),
    path('regpharmacy',views.regpharmacy,name='regpharmacy'),
    path('logins',views.logins,name='logins'),
    path('logout',views.logout,name='logout'),
    path('add_med',views.add_med,name='add_med'),
    path('addmed',views.addmed,name='addmed'),
    path('home',views.home,name='home'),
    path('homecust',views.homecust,name='homecust'),
    path('vmed',views.vmed,name='vmed'),
    path('searchmed',views.searchmed,name='searchmed'),
    path('search',views.search,name='search'),
    path('delete',views.delete,name='delete'),
    path('updates/<int:id>',views.updates,name='updates'),
    path('edit',views.edit,name='edit'),
    path('outstock/<int:id>',views.outstock,name='outstock'),
    path('instock/<int:id>',views.instock,name='instock'),
    path('outstock',views.outstocks,name='outstock'),
    path('order/<int:id>',views.order,name='order'),
    path('placeorder',views.placeorder,name='placeorder')
    ]
urlpatterns += staticfiles_urlpatterns()