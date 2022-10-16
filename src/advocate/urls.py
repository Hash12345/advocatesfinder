from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    Signup,
    UpdateAdvocateBioView,
    AddLinksView
)
urlpatterns = [
    #JWT Token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('signup/', Signup.as_view(), name='signup'),
    path('update_bio/', UpdateAdvocateBioView.as_view(), name='update_bio'),
    path('add_links/', AddLinksView.as_view(), name='add_links'),

]
