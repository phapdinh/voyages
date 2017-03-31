from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from django.utils.translation import ugettext_lazy as _


class FlatPageAdmin(FlatPageAdmin):
    save_as = True
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse', ),
            'fields': (
                'registration_required',
                'template_name',
            ),
        }),
    )
    class Media:
        js = ('scripts/tiny_mce/tinymce.min.js',
          'scripts/tiny_mce/textareas.js',
          )
# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)