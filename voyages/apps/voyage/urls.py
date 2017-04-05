from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView

import voyages.apps.common.views
import voyages.apps.voyage.views
import voyages.apps.static_content.views

urlpatterns = [
    url(r'^c(?P<chapternum>\w{2})_s(?P<sectionnum>\w{2})_p(?P<pagenum>\w{2})',
        voyages.apps.voyage.views.get_page, name='get-page'),
    url(r'^source/(?P<category>\w+)/(?P<sort>\w+)',
        voyages.apps.voyage.views.sources_list, name='sources-list-sort'),
    url(r'^source/(?P<category>\w+)',
        voyages.apps.voyage.views.sources_list, name='sources-list'),
    url(r'^source',
        voyages.apps.voyage.views.sources_list, name='sources-list-default'),
    url(r'^$', voyages.apps.static_content.views.get_static_content, {'group': 'Voyage'}, name='index'),

    #These are Flat pages. Make sure to include the methodology number in num
    url(r'^understanding-db/methodology-1$', voyages.apps.common.views.flatpage_language, {'url' : "/voyage/methodology/", 'num': 1}, name='meth-intro'),
    url(r'^understanding-db/methodology-2$', voyages.apps.common.views.flatpage_language, {'url' : "/voyage/methodology/", 'num': 2}, name='meth-coverage'),
    url(r'^understanding-db/methodology-3$', voyages.apps.common.views.flatpage_language, {'url' : "/voyage/methodology/", 'num': 3}, name='meth-sources'),
    url(r'^understanding-db/methodology-4$', voyages.apps.common.views.flatpage_language, {'url' : "/voyage/methodology/", 'num': 4}, name='meth-cases-variables'),
    url(r'^understanding-db/methodology-5$', voyages.apps.common.views.flatpage_language, {'url' : "/voyage/methodology/", 'num': 5}, name='meth-data-variables'),
    url(r'^understanding-db/methodology-15$', voyages.apps.common.views.flatpage_language, {'url' : "/voyage/methodology/", 'num': 15}, name='imputing-slaves'),
    url(r'^understanding-db/methodology-21$', voyages.apps.common.views.flatpage_language, {'url' : "/voyage/methodology/", 'num': 21}, name='methappendix'),

    # The rest of these are processed by this view
    url(r'^understanding-db/(?P<name>.*)', voyages.apps.voyage.views.understanding_page, name='understanding-page'),

    url(r'^understanding-db', voyages.apps.voyage.views.understanding_page, name='guide'),

    url(r'^c01_s01_cover', TemplateView.as_view(template_name='voyage/guide.html'), name='voyage-guide-intro'),
    #url(r'^c01_s03_cover', voyages.apps.voyage.views.variable_list, name='variables'),
    url(r'^reload-cache', voyages.apps.voyage.views.reload_cache, name='reload_cache'),

    url(r'^search', voyages.apps.voyage.views.search, name='search'),

    url(r'^permalink', voyages.apps.voyage.views.get_permanent_link, name='permanent-link'),

    url(r'^contribute', RedirectView.as_view(url='/contribute'), name='submission-login'),
    
    url(r'^voyage', TemplateView.as_view(template_name='under_constr.html'), name='voyage'),
    url(r'^(?P<voyage_id>[0-9]+)/variables', voyages.apps.voyage.views.voyage_variables, name='voyage_variables'),
    url(r'^(?P<voyage_id>[0-9]+)/map', voyages.apps.voyage.views.voyage_map, name='voyage_map'),
    url(r'^(?P<voyage_id>[0-9]+)/images', voyages.apps.voyage.views.voyage_images, name='voyage_images'),

    url(r'^csv_stats_download', voyages.apps.voyage.views.csv_stats_download, name='csv_stats_download'),
    url(r'^download', voyages.apps.common.views.flatpage_language, {'url' : "/voyage/download/"}, name='download')
]
