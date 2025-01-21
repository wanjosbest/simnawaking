from django.urls import path
from. import views

urlpatterns = [
   
    path("", views.index, name ="index"),
    path('play/<int:song_id>/', views.play_song, name='play_song'),
    path('download/<int:song_id>/', views.download_song, name='download_song'),
    path("songstat", views.user_song_stats, name="song_stats"),
    path("all-songs/", views.allposts, name="all_songs"),
    path("posts/<slug>/",views.postdetails, name="post_details"),
    path("search/", views.search, name="search"),
   
   
]
"""
urlpatterns = [
   
    path("api/register/",views.register, name= "register"),
    path("api/view-user/",views.viewusers, name= "view-user"),
    path("api/delete-user/<str:id>/",views.deleteusers, name= "delete-user"),
    path("api/update-user/<str:id>/",views.updateusers, name= "update-user"),
    path("api/user-login/",views.user_login, name= "user-login"),
    path("api/user-logout/",views.user_logout, name="user-logout"),
    path("api/user-change-password/",views.changepassword, name="user-change--password"),
]
"""