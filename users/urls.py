from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.apps import UsersConfig
from users.views import UserCreateView, email_verification, LoginUser, reset_password, ProfileView

app_name = UsersConfig.name

urlpatterns = [
    # path('login/', LoginView.as_view(template_name='login.html'), name='login' ),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    # path('password-reset/', PasswordResetView.as_view(
    #      template_name='users/password_reset_form.html',
    #      email_template_name = 'users/password_reset_email.html',
    #      success_url=reverse_lazy('users:password_reset_done')),
    #      name='password_reset'),
    # path('password-reset/done/', PasswordResetDoneView.as_view(template_name = "users/password_reset_done.html"),
    #      name='password_reset_done'),
    # path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
    # template_name="users/password_reset_confirm.html", success_url=reverse_lazy('users:password_reset_complete')),
    #      name='password_reset_confirm'),
    # path('password-reset/complete/', PasswordResetCompleteView.as_view(
    #     template_name="users/password_reset_complete.html"), name='password_reset_complete'),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("reset_password/", reset_password, name="reset_password"),
]