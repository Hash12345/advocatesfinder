from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    Signup,
    UpdateAdvocateBioView,
    AddLinksView,
    AdvocateView,
    AdvocateDetailView,
    CompaniesView,
    CompanyDetailView,
    SearchAdvocateView,
    AddReviewView,
    generateRTMToken,
    generateRTCToken,
    ShowReviewsView,
)
urlpatterns = [
    #JWT Token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('signup/', Signup.as_view(), name='signup'),
    path('update_bio/', UpdateAdvocateBioView.as_view(), name='update_bio'),
    path('add_links/', AddLinksView.as_view(), name='add_links'),
    path('advocates/', AdvocateView.as_view(), name='advocates'),
    path('advocates/<uuid:pk>/', AdvocateDetailView.as_view(), name='advocates_detail'),
    path('search_advocates/', SearchAdvocateView.as_view(), name='search_advocates'),
   
    path('companies/', CompaniesView.as_view(), name='companies'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='companies_detail'),

    path('add_reviews/', AddReviewView.as_view(), name='add_review'),
    path('show_advocate_reviews/<uuid:pk>/', ShowReviewsView.as_view(), name='show_advocate_reviews'),

    # Agora RTM|RTC token generation link for realtime communication between advocates
    path('generate_rtm_token/', generateRTMToken.as_view(), name="generate_rtm_token"),
    path('generate_rtc_token/', generateRTCToken.as_view(), name="generate_rtc_token"),
]
