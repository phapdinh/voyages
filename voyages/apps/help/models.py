from django.db import models
from django.utils.translation import ugettext as _


class Glossary(models.Model):
    """
    A single glossary entry used to explain a particular term

    """
    term = models.CharField(_('Term'), max_length=50)
    description = models.CharField(_('Description'), max_length=1000)

    class Meta:
        ordering = ['term']
        verbose_name = 'Glossary Item'
        verbose_name_plural = "Glossary Items"

    def __unicode__(self):
        return self.term

class FaqCategory(models.Model):
    """
    A FAQ question category, may contain many faq questions
    related to :class:`~voyages.apps.help.models.Faq`

    """
    text = models.CharField(_('Category'), max_length=100)
    type_order = models.IntegerField('Category Order')
    
    class Meta:
        ordering = ['type_order']
        verbose_name = 'FAQ category'
        verbose_name_plural = 'FAQ categories'
    
    def __unicode__(self):
        return self.text


class Faq(models.Model):
    """
    A single FAQ question and answer to it
    related to :class:`~voyages.apps.help.models.FaqCategory`

    """
    question = models.TextField(_('Question'), max_length=300)
    answer = models.TextField(_('Answer'), max_length=2000)
    category = models.ForeignKey('FaqCategory')
    question_order = models.IntegerField()
    
    def __unicode__(self):
        return "%s %s" % (self.category.text ,self.question)
    
    class Meta:
        ordering = ['category', 'question_order']
        verbose_name = 'Frequently Asked Question (FAQ)'
        verbose_name_plural = 'FAQs'


from .search_indexes import FaqIndex

# We are using this instead of the real time processor, since automatic update seems to fail (serializing strings)
def reindex_faqCategory(sender, **kwargs):
    FaqIndex().update()
    for obj in Faq.objects.filter(category=kwargs['instance']):
        FaqIndex().update_object(obj)

models.signals.post_save.connect(reindex_faqCategory, sender=FaqCategory)
