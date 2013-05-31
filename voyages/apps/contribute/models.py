# Create your models here.
from django.db import models

class OtherFile(models.Model):
    file = models.FileField(upload_to='other')
    filetitle = models.CharField(('File name'),max_length=50)
    filenote = models.CharField(('File name'),max_length=100)

class DownloadFile(models.Model):
    file = models.FileField(upload_to='download')
    filetitle = models.CharField(('File name'),max_length=50)

    def __unicode__(self):
        return self.filetitle
