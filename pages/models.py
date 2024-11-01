from django.contrib.auth.models import AbstractUser
from django.db import models


# نموذج المستخدم
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

# نموذج الحدث
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_tickets = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# نموذج التذكرة
class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    is_refunded = models.BooleanField(default=False)

    def __str__(self):
        return f'Ticket for {self.event.title} by {self.user.username}'

# نموذج طلب الاسترداد
class RefundRequest(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])
    credit_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Refund request for {self.ticket}'

# نموذج الدفع
class Payment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[('Sadad', 'Sadad'), ('Edfa3li', 'Edfa3li'), ('Ghodoon', 'Ghodoon')])

    def __str__(self):
        return f'Payment for {self.ticket}'
