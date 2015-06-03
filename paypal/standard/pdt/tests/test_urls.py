from django.conf.urls import url, include, patterns

urlpatterns = patterns('paypal.standard.pdt.views',
    (r'^pdt/$', 'pdt'),
)
