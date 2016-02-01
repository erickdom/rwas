from django.db import models

class Request(models.Model):
    message = models.TextField()
    number = models.CharField(null=False, max_length=50)
    date_request = models.DateTimeField(null=False)
    request_type = models.IntegerField(null=False)
    response = models.CharField(null=True, max_length=2)
    description = models.TextField(null=True)
    code = models.IntegerField(null=True)
    date_received = models.DateTimeField(null=True)
    date_sent = models.DateTimeField(null=True)

    class Meta:
        verbose_name = u"Request"
        verbose_name_plural = u"Requests"

    def __unicode__(self):
        return "%s" % self.message

class Last_Whatsapp_Id(models.Model):
    whatsapp_id = models.IntegerField(default=0)
    class Meta:
        verbose_name = u"LastID"
        verbose_name_plural = u"LastID"

    def __unicode__(self):
        return "%s" % self.whatsapp_id
