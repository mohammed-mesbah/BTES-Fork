from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("", views.link_list, name="link_list"),  # رابط جديد لعرض الروابط
    path("create_event/", views.create_event, name="create_event"),
    path("create_ticket/", views.create_ticket, name="create_ticket"),
    path(
        "create_refund_request/",
        views.create_refund_request,
        name="create_refund_request",
    ),
    path("create_user/", views.create_user, name="create_user"),
    path("create_payment/", views.create_payment, name="create_payment"),
]
