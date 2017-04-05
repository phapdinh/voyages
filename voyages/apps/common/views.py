from datetime import date

import django
from django.contrib.flatpages.models import FlatPage
from django.shortcuts import render
from django.utils.translation import get_language

from voyages.apps.voyage.models import Voyage
from voyages.apps.voyage.globals import methodology_items as meth


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


def flatpage_language(request, url, num=None):
    lang = get_language()

    #make sure url starts and end with /
    url  = "/" + url if not url.startswith('/') else url
    url = url + "/" if not url.endswith('/') else url

    #case for methodology urls
    left=None
    right=None
    pagename=None
    if num:
        url += '%s/' % num
        left = meth[num-2] if num !=1 else ''
        right = meth[num] if num != len(meth) else ''
        pagename = meth[num-1]['page']

    non_lang_url = url # for pages that will not be translated

    #get page for current language
    url += lang +  "/"

    flatpage = None
    try:
        flatpage = FlatPage.objects.get(url=url)
    # if flatpage does no have language varents
    except:
        flatpage = FlatPage.objects.get(url=non_lang_url)

    return render(request, flatpage.template_name,
                  {'flatpage': flatpage, 'num_voyages': Voyage.objects.count(), 'year': str(date.today().year),
                   'left': left, 'right': right, 'pagename': pagename})