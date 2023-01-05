from django.urls import path, include
from .views import SignupView

app_name = 'accounts'
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls'))
]
