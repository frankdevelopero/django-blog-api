from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

from django.urls import path
from users.api.views import *

urlpatterns = [
    path('user/auth/register', RegisterView.as_view()),
    path('user/auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/auth/me', UserView.as_view())
]