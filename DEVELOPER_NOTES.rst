Image Cache
===========

When using the `PIL <https://pypi.python.org/pypi/PIL/>`_ python library, thumbnail images are cached in ``/documents/cache``
Sometimes (especally after a code deploy) these files get out of sync and the thumbnail
images do not display. To correct this run the command::

  $ python manage.py thumbnail cleanup

Add Flat Page
=============
This example creates a new flat page that can be accessed at */education/new-page* in the education app.

create url.py entry in education/urls.py file::

  url(r'^new-page', voyages.apps.common.views.flatpage_language, {'url' : "/education/new-page/"}, name='new-page')

.. NOTE::

  The **url** parameter must start and end with a ``/``

In the Live Admin navigate to Flatpages and create a new entry. You can make a copy of an existing object by
 using the ``Save As New`` button. Create the new FlatPage with the following fields:
  | **URL:** /education/new-page/``<LANG-CODE>``
  | **Title:** New Page
  | **Content:** HTML CONTENT FOR THAT LANGUAGE
  | **Template_Name:** flatpages/education_flatpage.html

.. NOTE::
  The Template_Name field is under *Advanced > Show* on each flat page record.
  Since each app has its own styling requirements, each app should have its own flatpage template file.
  ``flatpages/education_flatpage.html``  can be used as a starting point if additional templae files need to be added.
  Each language version must have its own Flatpage entry in the database with a unique value in the url field. The
  last level of the url indicates the language.
  Example: ``/about/en/`` or  ``/about/pt/`` .
  The value of the url field must start and end with a ``/``
  Current laguages and codes are in **settings.LANGUAGES**.
  Variables referenced like ``{{name}}`` can be stored in the Flatpage object, template tags or filters will not be resolved.

Make reference to the link *{ url ‘new-page’}* somewhere on the website

Export to initial data::

  $ python ./manage.py dumpdata flatpages --indent=4 > initialdata/flatpages.json

Load data to QA or Prod database:
  | Make a copy of the initialdata/flatpages.json.
  | Remove the entries that are NOT new so any previous modifications are not overwritten

Load the remaing entries::

  $ python ./manage.py loaddata <PATH-TO-INPUT-FILE>

