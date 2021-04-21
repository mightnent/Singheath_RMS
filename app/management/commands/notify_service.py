from django.core.management.base import BaseCommand, CommandError
from app.models import Tenant
from audit.models import ChecklistInstance, ScoreTable
from datetime import date
from django.db.models import F
from django.core.mail import get_connection
from app.email_handler import EmailHandler

class Command(BaseCommand):
    help = """
    Sends tenant expiry notification
    permissions may have to be set for sh file using
    `chmod +x /home/ubuntu/pyapps/Singheath_RMS/notify.sh`
    then use `crontab -e` to open crontab editor then insert 
    `0 0 * * * /home/ubuntu/pyapps/Singheath_RMS/notify.sh >> /home/ubuntu/pyapps/Singheath_RMS/notifylog.txt 2>&1`
    """
    def _getDateExp(self, date_now, num_months):
        date_exp_month = date_now.month + num_months
        date_exp_year = date_now.year
        if (date_exp_month > 12):
            date_exp_month -= 12
            date_exp_year += 1
        return (date_exp_month, date_exp_year)

    def _getNextDay(self, date_today):
        return (date_today.day + 1, date_today.month, date_today.year)

    def _findExpiry(self, num_months, date_now, date_exp_day, connection):
        date_exp_month, date_exp_year = self._getDateExp(date_now, num_months)
        #self.stdout.write(date_exp_day, date_exp_month, date_exp_year)
        for tenant in Tenant.objects.filter(
            lease_end_date__day=date_exp_day,
            lease_end_date__month=date_exp_month,
            lease_end_date__year=date_exp_year):
            EmailHandler.notify_tenant_lease_expiry(tenant.name, tenant.lease_end_date, tenant.email, f"{num_months} month(s)", connection)
            self.stdout.write(f"Email sent to {tenant.name} at email {tenant.email}")

    def _findNoncompliance(self, date_today, connection):
        (day, month, year) = self._getNextDay(date_today)
        scoreTable = ScoreTable.objects.filter(
            num_visited=F('page_num'))
        print(day, month, year)
        checklistTable = ChecklistInstance.objects.filter(
            checklist_id__in = [x.checklist_id for x in scoreTable],
            date_due__year=year,
            date_due__month=month,
            date_due__day=day).values("tenant", "tenant_location").distinct()
        for i in checklistTable:
            tenant = Tenant.objects.get(business_name=i.get("tenant"), institution=i.get("tenant_location"))
            EmailHandler.notify_non_compliance_deadline(tenant.email, tenant.business_name, connection)

        
                
    def handle(self, *args, **options):
        connection = get_connection()
        date_now = date.today()
        date_exp_day = date_now.day
        self._findExpiry(6, date_now, date_exp_day, connection)
        self._findExpiry(3, date_now, date_exp_day, connection)
        self._findExpiry(1, date_now, date_exp_day, connection)
        self._findNoncompliance(date_now, connection)
        connection.close()

