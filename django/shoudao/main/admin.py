from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(ContactGroup)
admin.site.register(Message)
admin.site.register(MessageDataNotice)
admin.site.register(Link)