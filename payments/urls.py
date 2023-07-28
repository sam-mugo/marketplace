from django.urls import path, include
from . import views

app_name = 'payments'

test_patterns = [
	path('$', views.index, name='django_daraja_index'),
	path('oauth/success', views.oauth_success, name='test_oauth_success'),
	path('payments/stk-push', views.stk_push_success, name='test_stk_push_success'),
	path('business-payment/success', views.business_payment_success, name='test_business_payment_success'),
	path('salary-payment/success', views.salary_payment_success, name='test_salary_payment_success'),
	path('promotion-payment/success', views.promotion_payment_success, name='test_promotion_payment_success'),
]

urlpatterns = [
	path('$', views.index, name='index'),
	path('tests/', include(test_patterns)),
]