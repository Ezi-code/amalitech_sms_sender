from django.contrib import admin
from .models import MessageHistory, Messages

class MessageHistoryAdmin(admin.ModelAdmin):
    list_display = ('message','timestamp')


class MessageAdmin(admin.ModelAdmin):
    list_display = ("title", "timestamp", "is_template")

admin.site.register(MessageHistory, MessageHistoryAdmin)
admin.site.register(Messages, MessageAdmin)

