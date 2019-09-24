from django.db import models

# Create your models here.
class Paste(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=40, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name or str(self.id)

    def get_absolute_url(self):
        return ('pastebin:paste_detail', [self.id])