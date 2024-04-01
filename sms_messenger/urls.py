from django.urls import path
from sms_messenger import views

urlpatterns = [
    path("home", views.HomeView.as_view(), name="home"),
    path("app/login", views.Loginview.as_view(), name="login"),
    path("app/logout", views.LogoutView.as_view(), name="logout"),
    path("app/messages/send_sms", views.SendSmsView.as_view(), name="send_bulk_sms"),
    path(
        "app/messages/sms_history", views.MessageHistoryView.as_view(), name="history"
    ),
    path(
        "app/messages/create-sms-template",
        views.TemplatesView.as_view(),
        name="create-template",
    ),
    path(
        "app/messages/sms-templates",
        views.TemplatesListView.as_view(),
        name="templates",
    ),
    path("app/messages/edit/<uuid:pk>", views.EditSMSView.as_view(), name="edit_sms"),
    path(
        "app/templates/edit/<uuid:pk>",
        views.EditTemplateView.as_view(),
        name="edit_template",
    ),
    path(
        "app/messages/trigger_send/<uuid:pk>",
        views.send_sms,
        name="trigger_send",
    ),
]
