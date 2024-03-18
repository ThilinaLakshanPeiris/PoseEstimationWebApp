from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from WebApp.views import ChangePasswordView, LogoutAllView, LogoutView, MyObtainTokenPairView, RegisterView, UpdateProfileView, userDetail, userList


urlpatterns = [
      
    # path('depot/', DepotDetail.as_view()),
    # path('depot/<int:pk>/', DepotList.as_view()),
    path('user/', userDetail.as_view()),
    path('user/<int:pk>/', userList.as_view()),

    # path('userun/', FulUserUn.as_view()),
    # path('user/', UserDetail.as_view()),
    # path('user/<int:pk>/', UserList.as_view()),

    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
]