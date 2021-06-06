from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views
from .views import UserRegisterView
from django.conf import settings


urlpatterns = [
  path('',views.indexVIEW, name='index'),
  path('Choice/',views.categoryVIEW, name='choice'),
  path('display/',views.display, name='display'),
  path('Trending/post/',views.trendingVIEW, name='trending'),
  path('display/blog/<str:choice>',views.Filter_DisplayVIEW, name='Filter_Display'),
  path('user/',views.UserInfo, name='userProfile'),
  path('userinfoform/',views.UserInfo, name='userProfileform'),
  path('details/<int:id>',views.detailsView, name='details'),
  path('details/Update/<int:pk>/edit', views.updateVIEW.as_view(), name='update'),
  path('details/delete/<int:pk>/edit', views.DeleteVIEW.as_view(), name='delete'), 
  path('author/<int:id>',views.AdminView, name='author'),  #not using for now
  path('like/<int:id>',views.likeView, name='like'),
  path('clicking/<int:id>',views.addsView, name='add'),
  path('register', UserRegisterView.as_view(), name='register'),
  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

