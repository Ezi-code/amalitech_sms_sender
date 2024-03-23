from django.contrib import admin
from .models import MessageHistory, Messages, Templates


# class MessageHistoryAdmin(admin.ModelAdmin):
#     list_display = ["id", "message", "sent_date"]
#     search_fields = ["message", "sent_date"]
#     list_filter = ["sent_date"]


# class MessagesAdmin(admin.ModelAdmin):
#     list_display = ["id", "message", "sent_at"]
#     search_fields = ["message", "sent_at"]
#     list_filter = ["sent_at"]


# class TemplatesAdmin(admin.ModelAdmin):
#     list_display = ["id", "title", "content"]
#     search_fields = ["title", "content"]
#     list_filter = ["title"]


admin.site.register([MessageHistory, Messages, Templates])
# Register your models here.
