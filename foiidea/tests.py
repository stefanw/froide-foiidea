from django.utils.six import text_type as str
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils import timezone

from .models import Source, Article


class FoiideaTest(TestCase):
    def setUp(self):
        super(TestCase, self).setUp()
        self.source = Source.objects.create(
            name='Blog',
            homepage='http://blog.example.com/',
            url='http://blog.example.com/feed.rss',
            crawler='rss',
            last_crawled=timezone.now()
        )
        self.article = Article.objects.create(
            title='Title',
            text='text',
            date=timezone.now(),
            url='http://blog.example.com/article',
            source=self.source
        )

    def test_web(self):
        response = self.client.get(reverse('foiidea-index'))
        self.assertEqual(response.status_code, 200)

        article = Article.objects.get_ordered()[0]

        response = self.client.get(article.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_model(self):
        self.assertIn(self.article.title, str(self.article))
        self.assertIn(self.source.name, str(self.source))
