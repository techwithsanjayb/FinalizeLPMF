from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="indexpage"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('vision/', views.vision, name="vision"),
    path('mission/', views.mission, name="mission"),
    path('services/', views.services, name="services"),
    path('faqs/', views.display_faq, name="faqs"),
#     path('tools/', views.display_tools, name="display_tools"),
    path('toolswithcategory/', views.display_tools_with_category, name="display_tools_with_category"),
    path('resources/', views.display_resources_with_category, name="display_resources_with_category"),
    #path('success-stories/', views.display_success_stories,
         #name="display_success_stories"),
    path('ap-success-stories/', views.display_ap_success_stories,
         name="display_ap_success_stories"),
    path('privacypolicy/', views.displayPrivacyPolicy,
         name='display_privacy_policy'),

    path('termsandconditions/', views.termsandconditions,
         name="terms_and_conditions"),
    path('disclaimer/', views.disclaimer, name="disclaimer"),
    path('register/', views.signup, name="register"),
    path('login_user/', views.login_user, name="login"),
    path('logout_user/', views.logout_user, name="logout"),
    path('profile/',views.profile , name="profile"),
    path('changepass/',views.user_change_pass,name="changepass"),
    path('userdetail/<int:id>',views.userdetail,name="userdetail"),
    path('contact/',views.contact,name="contact"), 
    path('success-stories/',views.success_stories,name="success_stories"),   
    path('newsandevents/',views.display_news_events,name="display_news_events"), 
    path('blogs/',views.display_blogs,name="display_blogs"), 

]
