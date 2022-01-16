from django.test import SimpleTestCase
from django.urls import reverse, resolve
from europeanfootball.views import matchstat_form, matchstat_del, update_matchstats

class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func,matchstat_form)
    
    """def test_matchdel_url_is_resolved(self):
        url = reverse('matchstatsupdate')
        self.assertEquals(resolve(url).func,matchstat_del)"""