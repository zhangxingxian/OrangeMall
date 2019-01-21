import xadmin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

from OrangeMall import settings

urlpatterns = [
    url(r'^xadmin/',xadmin.site.urls),
    # url(r'^$',  RedirectView.as_view(url="/home/index"),name='index'),
    url(r'^account/',include("account.urls",namespace="account")),
    url(r'^order/', include("order.urls", namespace="order")),
    url(r'^comment/',include("comment.urls",namespace="comment")),
    url(r'^detail/',include("detail.urls",namespace="detail")),
    url(r'^home/',include("home.urls",namespace="home")),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
