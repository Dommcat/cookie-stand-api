from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework_simplejwt import views as jwt_views
from .views import MyTokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),

    # Redirect URL
    path('', lambda req: redirect('api/v1/app/')),

    # DRF URLS
    path('api/v1/app/', include('cookie_stands.urls')),
    path('api-auth', include("rest_framework.urls")),

    # JWT URLS
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]


# urlpatterns = [
#     path("admin/", admin.site.urls),

#     path("api/v1/things/", include("things.urls")),
#     path("api-auth/", include("rest_framework.urls")),
#     path(
#         "api/token/",
#         MyTokenObtainPairView.as_view(),
#         name="token_obtain_pair",
#     ),
#     path(
#         "api/token/refresh/",
#         jwt_views.TokenRefreshView.as_view(),
#         name="token_refresh",
#     ),
#     path("things/", include("things.urls_front")),
#     path("", TemplateView.as_view(template_name="home.html"), name="home"),
#     path("about/", TemplateView.as_view(template_name="about.html"), name="about"),
#     path("accounts/", include("accounts.urls")),
#     path("accounts/", include("django.contrib.auth.urls")),
# ]
