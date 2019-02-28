from django.conf.urls import url
from basic_app import views


# TEMPLATE TAGGING
# Faz referência a tag usada em relative_url_templates.html
app_name = 'basic_app'

urlpatterns= [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
]
