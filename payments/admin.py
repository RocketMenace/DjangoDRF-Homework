from django.contrib import admin
from .models import Payment

# Register your models here.


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "payment_date",
        "paid_course",
        "paid_lesson",
        "amount_paid",
        "payment_method",
    ]
    list_filter = ["user", "payment_date", "payment_method"]
    raw_id_fields = ["paid_course", "paid_lesson"]
    date_hierarchy = "payment_date"
    ordering = ["payment_date"]
