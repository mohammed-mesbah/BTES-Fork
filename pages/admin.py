from django.contrib import admin

from .models import Event, Payment, RefundRequest, Ticket, User

# تسجيل النموذج المخصص للمستخدم
admin.site.register(User)

# تسجيل نماذج الأحداث
admin.site.register(Event)

# تسجيل نماذج التذاكر
admin.site.register(Ticket)

# تسجيل نماذج طلبات الاسترداد
admin.site.register(RefundRequest)

# تسجيل نماذج الدفع
admin.site.register(Payment)
