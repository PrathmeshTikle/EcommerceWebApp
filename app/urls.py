from django.urls import path
from .forms import Loginform,MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from app import views
urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/',views.plus_cart,name='pluscart'),
    path('minuscart/',views.minus_cart,name='minuscart'),
    path('removecart/',views.remove_cart,name='removecart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name="app/passwordchange.html",form_class=MyPasswordChangeForm,success_url='/passwordchangedone/'),name='passwordchange'),
    #path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="app/login.html",authentication_form=Loginform), name='login'),
    path('customerregistration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name="app/passwordchangedone.html"),name='passwordchangedone'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name="app/password_reset.html",form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="app/password_reset_done.html"),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="app/password_reset_confirm.html",form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name="app/password_reset_complete.html"),name='password_reset_complete'),
    path('checkout/', views.checkout, name='checkout'),
    path('buynow/',views.buy_now,name='buynow'),
    path('paymentdone/',views.payment_done,name='paymentdone'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
