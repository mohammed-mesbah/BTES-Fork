from django import forms

from .models import Event, Payment, RefundRequest, Ticket, User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_admin']
        widgets = {
            'password': forms.PasswordInput(),  # تأمين إدخال كلمة مرور مخفية بالنجوم
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location', 'price', 'available_tickets', 'created_by']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['event','quantity', 'user']

class RefundRequestForm(forms.ModelForm):
    class Meta:
        model = RefundRequest
        fields = ['ticket', 'credit_amount', 'status']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['ticket', 'amount', 'payment_method']
