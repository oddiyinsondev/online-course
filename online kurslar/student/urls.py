from django.urls import path
from .views import home_send, courses_send, Contact_up, about_send,  registertion, logout_user, loginUser, Postlist, post_detail, category_post

urlpatterns = [
    path('', home_send, name="home"),
    path('courses/', courses_send, name="courses"),
    path('contact/', Contact_up, name="contact"),
    path('about/', about_send, name="about"),
    path('login/', loginUser, name="login" ),
    path('register/', registertion, name='register'),
    path('logout/', logout_user, name="logout"),
    path('post_videos', Postlist.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', post_detail, name="post_detail"),
    path('category/<slug:slug>//', category_post, name='category_post'),
    
]



