from haystack import indexes
from .models import Image

class ImagesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    image_id = indexes.IntegerField(model_attr="image_id", null=True)
    file = indexes.CharField(model_attr="file")
    ready_to_go = indexes.BooleanField(model_attr="ready_to_go", default=False)
    date = indexes.IntegerField(model_attr="date", null=True)
    title = indexes.CharField(model_attr="title")
    description = indexes.CharField(model_attr="description", null=True)
    category_label = indexes.CharField()
    voyage_id = indexes.IntegerField(null=True)
    voyage_vessel_name = indexes.CharField(null=True)
    voyage_year = indexes.CharField(null=True)

    def get_model(self):
        return Image

    def prepare_category_label(self, obj):
        return obj.category.label

    def prepare_voyage_id(self, obj):
        return obj.voyage.voyage_id

    def prepare_voyage_vessel_name(self, obj):
        return obj.voyage.voyage_ship.ship_name

    def prepare_voyage_year(self, obj):
        return obj.voyage.voyage_dates.imp_voyage_began

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()