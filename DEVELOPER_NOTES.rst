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
  Example: ``/about/en/`` or  ``/about/pt/`` . If the page does not need to be translated, there should only be one version
  of the flatpage and the url field should not contain a language code Example: ``/education/new-page/``
  The value of the url field must start and end with a ``/``
  Current laguages and codes are in **settings.LANGUAGES**.
  Variables ``{{ STATIC_UR }}`` and ``{{ MEDIA_URL }}`` can be stored in the Flatpage object. It recomended to retain
  these variables in the Flatpage in case there are config changes in the future.
  Template tags and filters will not be resolved. To add additional variables to be resolved, modify the *parse_blocks* template filter.


Make reference to the link *{ url ‘new-page’}* somewhere on the website

Export to initial data::

  $ python ./manage.py dumpdata flatpages --indent=4 > initialdata/flatpages.json

Load data to QA or Prod database:
  | Make a copy of the initialdata/flatpages.json.
  | Remove the entries that are NOT new so any previous modifications are not overwritten

Load the remaing entries::

  $ python ./manage.py loaddata <PATH-TO-INPUT-FILE>



To obtain the html content
--------------------------
* Option 1: Edit the content directly in the GUI editor. This is good for small sections or making corrections.
* Option 2: In the GUI editor select **Tools > Source** to edit or paste HTML directly. This is good for entire pages
  or large sections.

.. NOTE::

  If you do not have the source HTML (or it is not fully resolved due to variables) you can use the *Chrome* browser to
  inspect and extract the section of HTML you need.
#. Right click on the section of the page you want to copy
#. Select *inspect* from the contenxt menu
#. locate the block of code you want to copy
#. Right click and select Edit HTML
#. Select all the HTML in the new window
#. You can paste that directly into the editor (Option 2 above)