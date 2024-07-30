from django.urls import path
from . import views
from . views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    path('',views.getRoutes),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('groceries/',views.getGroceries),
    path('calculate_total_price/', views.calculate_total_price, name='calculate_total_price'),

]