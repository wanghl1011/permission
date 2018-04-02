from django.conf.urls import url, include
from rbac import views
urlpatterns = [
    url(r'^login/$',views.login),
    # url(r'^index/$',views.index),
    # url(r'^add/user/$',views.func1),
    # url(r'^edit/user/(\d+)/$',views.func2),
    # url(r'^del/user/(\d+)/$',views.func3),
    url(r'^users/$',views.user_list),
    url(r'^menu/$',views.menu),
    url(r'^add/user/$',views.user_list),
    url(r'^edit/user/$',views.user_list),
    url(r'^del/user/$',views.user_list),
    url(r'^add/order/$',views.user_list),
    url(r'^orders/$',views.orders),
]