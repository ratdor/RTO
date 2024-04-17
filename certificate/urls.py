from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.login_view,name="login"),
    path('home/',views.home_view,name="home"),
    path('success/',views.success_view,name="success"),
    path('logout/',views.logout_view,name="logout"),
    path('search/',views.search_view,name="search"),
    path('certificate/<int:id>',views.certificate_view,name="certificate"),
    path('user_data/<int:user_id>/',views.user_data_view, name='user_data'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)