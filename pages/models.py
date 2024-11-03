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
    available_tickets= models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# نموذج التذكرة
class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    purchase_date = models.DateTimeField(auto_now_add=True)
    is_refunded = models.BooleanField(default=False)
    
    
    def purchase_ticket(self):
        # التحقق من توفر العدد المطلوب من التذاكر في الحدث
        if self.event.available_tickets >= self.quantity:
            self.event.available_tickets -= self.quantity  # تقليل السعة المتاحة في الحدث
            self.is_refunded = False
            self.save()
            self.event.save()
        else:
            raise ValueError("Not enough tickets available for this event.")
    
    def print_ticket(self):
        # طباعة تفاصيل التذكرة
        return f"Ticket for {self.event.title} - Quantity: {self.quantity} - Purchased by {self.user.username} on {self.purchase_date}"

    def __str__(self):
        return f"Ticket for {self.event.title} - Quantity: {self.quantity} - Purchased by {self.user.username} on {self.purchase_date}"

# نموذج طلب الاسترداد
class RefundRequest(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('cancelled', 'Cancelled')])
    credit_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    # def cancel_ticket(self):
    #     # إلغاء التذكرة وزيادة السعة المتاحة في الحدث
    #     if self.status == 'active':
    #         self.status = 'cancelled'
    #         self.event.capacity += self.quantity  # استعادة السعة المتاحة
    #         self.save()
    #         self.event.save()
    #     else:
    #         raise ValueError("Ticket is already cancelled.")
            # self.is_refunded = False

    def __str__(self):
        return f"Ticket for {self.event.title} by {self.user.username} (Status: {self.status})"
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
