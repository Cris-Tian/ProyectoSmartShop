from django.urls import path 
from . import views

urlpatterns=[
	path('',views.index,name='index'),
	path('store/', views.store, name='store'),
	path('ofertas/', views.ofertas, name='ofertas'),
	path('telefonos/', views.TelefonoListView.as_view(), name='telefonos'),
	path('smartphones/', views.smartphones, name='smartphones'),
	path('accesorios/', views.accesorios, name='accesorios'),
	path('checkout/', views.checkout, name='checkout'),
	path('caracteristicas/', views.caracteristicas, name='caracteristicas'),
	path('telefono/<int:pk>', views.TelefonoDetailView.as_view(), name='telefono-detail'),
	path('check/', views.check, name='check'),
	
]

urlpatterns +=[
	path('telefono/create/', views.TelefonoCreate.as_view(), name='telefono_create'),
	path('telefono/<int:pk>/update/', views.TelefonoUpdate.as_view(), name='telefono_update'),
	path('telefono/<int:pk>/delete/', views.TelefonoDelete.as_view(), name='telefono_delete'),

]
