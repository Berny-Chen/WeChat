from django.conf.urls import patterns, include, url
from django.contrib import admin
from weixin import views
urlpatterns = [
	url(r'^wechat/', views.wechat_home),
]
