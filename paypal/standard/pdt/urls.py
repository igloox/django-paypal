from django.conf.urls import url, include, patterns

urlpatterns = patterns('paypal.standard.pdt.views',
    url(r'^$', 'pdt', name="paypal-pdt"),
)