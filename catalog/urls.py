from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    ('books/', views.BookListView.as_view(), name='books'),
]
# urlpatterns += [
#     path('catalog/', include('catalog.urls')),
# ]