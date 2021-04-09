from app.models import Tenant
from datetime import date
from django.core.mail import get_connection
from app.email_handler import EmailHandler

def handle():
    connection = get_connection()
    date_now = date.today()
    date_exp_day = date_now.day
    _findExpiry(6, date_now, date_exp_day, connection)
    _findExpiry(3, date_now, date_exp_day, connection)
    _findExpiry(1, date_now, date_exp_day, connection)
    connection.close()

def _getDateExp(date_now, num_months):
    date_exp_month = date_now.month + num_months
    date_exp_year = date_now.year
    if (date_exp_month > 12):
        date_exp_month -= 12
        date_exp_year += 1
    return (date_exp_month, date_exp_year)

def _findExpiry(num_months, date_now, date_exp_day, connection):
    date_exp_month, date_exp_year = _getDateExp(date_now, num_months)
    for tenant in Tenant.objects.filter(
            lease_end_date__day=date_exp_day,
            lease_end_date__month=date_exp_month,
            lease_end_date__year=date_exp_year):
        EmailHandler.notify_tenant_lease_expiry(tenant.name, tenant.lease_end_date, tenant.email, f"{num_months} month(s)", connection)
        print(f"Email sent to {tenant.name} at email {tenant.email}")
