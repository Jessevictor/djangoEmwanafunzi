from django.urls import path
from .views import RegisterView, LoginView, ListCategory, DetailCategory, ListProduct, DetailProduct


urlpatterns =[
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),

    path('products', ListProduct.as_view(), name='products'),
    path('products/<int:pk>/', DetailProduct.as_view(), name='singleproduct'),

    path('categories', ListCategory.as_view(), name='categorie'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),
]