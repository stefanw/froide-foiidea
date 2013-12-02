from django.conf.urls import patterns


urlpatterns = patterns("foiidea.views",
    (r'^$', 'index', {}, 'foiidea-index'),
    (r'^(?P<article_id>\d+)/$', 'show', {}, 'foiidea-show'),
)
