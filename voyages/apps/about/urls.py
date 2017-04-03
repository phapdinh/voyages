from django.conf.urls import url
from django.views.generic import TemplateView

import voyages.apps.static_content.views

urlpatterns = [
    url(r'^$', voyages.apps.common.views.flatpage_language, {'url' : "/about/index/"}, name='index'),
    url(r'^history', voyages.apps.common.views.flatpage_language, {'url' : "/about/history/"}, name='history'),
    url(r'^team', voyages.apps.common.views.flatpage_language, {'url' : "/about/team/"}, name='team'),
    url(r'^data', voyages.apps.common.views.flatpage_language, {'url' : "/about/data/"}, name='data'),
    url(r'^acknowledgements', voyages.apps.common.views.flatpage_language, {'url' : "/about/acknowledgements/"}, name='acknowledgements'),
    url(r'^origins', voyages.apps.common.views.flatpage_language, {'url' : "/about/origins/"}, name='origins'),
    url(r'^contacts', voyages.apps.common.views.flatpage_language, {'url' : "/about/contacts/"}, name='contacts')]
