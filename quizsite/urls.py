from django.conf.urls import include, url
from django.contrib import admin
from quiz import views

urlpatterns = [
    url(r"^$", views.startpage, name="start_page"),
    url(r"^quiz/([a-z-]+)/$", views.quiz, name="quiz_page"),
    url(r"^quiz/([a-z-]+)/question/([0-9]+)/$", views.question, name="question_page"),
    url(r"^quiz/([a-z-]+)/completed/$", views.completed, name="completed_page"),
    url(r'^admin/', include(admin.site.urls)),
]
