from django.contrib import admin

from .models import Event, Payment, RefundRequest, Ticket, User

#register models for definition it in database
admin.site.register(User)

admin.site.register(Event)

admin.site.register(Ticket)

admin.site.register(RefundRequest)

admin.site.register(Payment)
