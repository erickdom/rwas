from django.contrib import admin

# Register your models here.
from requests.models import Request, Last_Whatsapp_Id

admin.site.register({Request, Last_Whatsapp_Id})