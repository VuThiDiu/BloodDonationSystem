from django.urls import path

from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    path('hospitallogin', LoginView.as_view(template_name='hospital/hospitallogin.html'),name='hospitallogin'),
    path('hospitalsignup', views.hospital_signup_view,name='hospitalsignup'),
    path('hospital-dashboard', views.hospital_dashboard_view,name='hospital-dashboard'),
    path('make-request', views.make_request_view,name='make-request'),
    path('my-request', views.my_request_view,name='my-request'),
    path('request-Blood-Donation-Organization', views.request_Blood_Donation_Organization, name='request-Blood-Donation-Organization'),
    path('my-request-Blood-Donation-Organization', views.my_request_Blood_Donation_Organization, name='my-request-Blood-Donation-Organization'),
    path('process-request', views.process_request, name='process-request'),
]