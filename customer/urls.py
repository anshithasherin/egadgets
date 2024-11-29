
from django.urls import path
from customer.views import *

urlpatterns = [
    path('chome',CustomerHomeView.as_view(),name='home'),
    path('productlist/<str:cat>',ProductListView.as_view(),name='pro'),
    path('pdetails/<int:id>',ProductDetailView.as_view(),name='pdetails'),
    path('cart/<int:id>',addToCart,name='cart'),
    path('cartlist',CartlistView.as_view(),name='cartlist'),
    path('incrsqnty/<int:id>',IncreaseQuantity,name='incrsqnty'),
    path('decrsqnty/<int:id>',DecreaseQuantity,name='decrsqnty'),
    path('deleteitem/<int:id>',Deleteitem,name='deleteitem'),
    path('Orderplaced/<int:id>',PlaceorderView,name='porder'),
    path('orderlist',OrderlistView.as_view(),name='orderlist'),
    path('cancelorder/<int:id>',cancelorder,name='ocancel'),
    path('search',searchproduct,name="search"),
]