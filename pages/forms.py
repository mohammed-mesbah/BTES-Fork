from django import forms

from .models import Event, Payment, RefundRequest, Ticket, User


# نموذج مستخدم
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_admin']  # يمكنك تخصيص الحقول كما تراه مناسبًا
        widgets = {
            'password': forms.PasswordInput(),  # لإدخال كلمة المرور بشكل آمن
        }

# نموذج حدث
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location', 'price', 'available_tickets', 'created_by']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
# نموذج تذكرة
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['event', 'user']

# نموذج طلب استرداد
class RefundRequestForm(forms.ModelForm):
    class Meta:
        model = RefundRequest
        fields = ['ticket', 'credit_amount', 'status']

# نموذج دفع
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['ticket', 'amount', 'payment_method']
