from datetime import date

import django
from django.contrib.flatpages.models import FlatPage
from django.shortcuts import render
from django.utils.translation import get_language

from voyages.apps.voyage.models import Voyage


def set_language(request, lang_code):
    """
    A wrapper around django.views.i18n.set_language suitable for an AJAX GET request.
    :param request: web request.
    :param lang_code: language code of the new language to use site-wise.
    :return: a plain text response with the given lang_code.
    """
    request.method = 'POST'
    request.POST = {'language': lang_code}
    django.views.i18n.set_language(request)
    return django.http.HttpResponse(lang_code, content_type="text/plain")


def flatpage_language(request, url):
    lang = get_language()

    #make sure url starts and end with /
    url  = "/" + url if not url.startswith('/') else url
    url = url + "/" if not url.endswith('/') else url

    #get corret language
    url += lang +  "/"

    flatpage = FlatPage.objects.get(url=url)

    return render(request, flatpage.template_name,
                  {'flatpage': flatpage, 'num_voyages': Voyage.objects.count(), 'year': str(date.today().year)})