import xadmin
from django.conf.urls import url, include
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^xadmin/',xadmin.site.urls),
    # url(r'^$',  RedirectView.as_view(url="/home/index"),name='index'),
    url(r'^account/',include("account.urls",namespace="account")),
    url(r'^cart/',include("cart.urls",namespace="cart")),
    url(r'^comment/',include("comment.urls",namespace="comment")),
    url(r'^detail/',include("detail.urls",namespace="detail")),
    url(r'^home/',include("home.urls",namespace="home")),
]
