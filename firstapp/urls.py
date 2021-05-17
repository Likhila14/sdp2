from django.urls import path
from . import views

urlpatterns = [
   
   path('' , views.home, name = "home"),
    path('home/' , views.home, name = "hhome"),
     path('bday/' , views.bday, name = "bday"),
      path('anniversary/' , views.anni, name = "anniversary"),
    path("login/", views.login, name="login"),
    path("register/",views.register,name="register"),
  path('logout/',views.logoutUser,name="logout"),
  path('contactus/' , views.contactus, name="contactus"),
  path('book/<int:id>', views.book, name="book"),
   path('profile/<int:id>/<str:username>', views.profile, name="profile"),
    path('editprofile/<int:id>', views.update, name="editprofile"),
     path('delete/<int:id>', views.destroy, name = "delete"),
]