from django.urls import path
from sms_messenger.views import (
    HomeView,
    Loginview,
    LogoutView,
    SendBulkSms,
    MessageHistoryView,
    TemplatesView,
    TemplatesListView,
    EditSMSView,
    EditTemplateView,
    send_sms,
)


urlpatterns = [
    path("home", HomeView.as_view(), name="home"),
    path("app/login", Loginview.as_view(), name="login"),
    path("app/logout", LogoutView.as_view(), name="logout"),
    path("app/messages/send_bulk_sms", SendBulkSms.as_view(), name="send_bulk_sms"),
    path("app/messages/history", MessageHistoryView.as_view(), name="history"),
    path(
        "app/messages/create-template", TemplatesView.as_view(), name="create-template"
    ),
    path("app/messages/template", TemplatesListView.as_view(), name="templates"),
    path("app/messages/edit/<uuid:pk>", EditSMSView.as_view(), name="edit_sms"),
    path(
        "app/templates/edit/<uuid:pk>", EditTemplateView.as_view(), name="edit_template"
    ),
    path(
        "app/messages/trigger_send/<str:content>/<str:recipients>",
        send_sms,
        name="trigger_send",
    ),
]
