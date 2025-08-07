from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='create-post'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='update-post'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete-post'),
    path('post/<int:pk>/comment/', views.add_comment, name='add-comment'),
    path('post/<int:pk>/like/', views.like_post, name='like-post'),
    
    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog_app/logout.html'), name='logout'),
    
    # Password Reset URLs
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='blog_app/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='blog_app/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='blog_app/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='blog_app/password_reset_complete.html'),
         name='password_reset_complete'),
    
    # Other URLs
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
] 