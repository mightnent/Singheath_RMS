from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives, get_connection
from django.conf import settings
from email.mime.image import MIMEImage
from app.models import Tenant
from django.contrib.staticfiles import finders

class EmailHandler:
    """
    Sends email to new tenant accounts created
    """
    @staticmethod
    def send_new_tenant_email(email, login_link, gen_password, owner_name, username):
        subject = "Account Created with Singhealth RMS"
        message = f"""Your account has been created with username: {username} and password: {gen_password}. 
            You can log in at {login_link}. Remember to change your password to a preferred one after logging in.
        """
        context = {
            'login_link': login_link,
            'gen_password': gen_password,
            'owner_name': owner_name,
            'username': username,
            'logo_name': "logo"
        }
        msg_html = render_to_string("email_templates/new_tenant_notice.html", context)
        email = EmailMultiAlternatives(
            subject=subject,
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[email]
        )
        email.attach_alternative(msg_html, "text/html")
        email.mixed_subtype = "related"
        with open(finders.find("assets/img/Singhealth-logo.png"), mode='rb') as f:
            image = MIMEImage(f.read())
            image.add_header('Content-ID', "<logo>")
            email.attach(image)
        email.send()

    """
    TODO: adjust for checklist export
    """
    @staticmethod
    def checklist_export(username, checklist):
        subject = "test email"
        message = "testing"
        context = {
            'username': username,
            'logo_name': "logo",
            'checklist_type': "FNB",
            'tenant_name': "Kopitiam",
            'is_checklist_scored': True,
            'checklist': {'section': [{'text': "thing", 'score': '4'}, {'text': "ds", 'score': '5'}]}
        }
        msg_html = render_to_string("email_templates/export_checklist.html", context)
        email = EmailMultiAlternatives(
            subject=subject,
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER]
        )
        email.attach_alternative(msg_html, "text/html")
        email.mixed_subtype = "related"
        with open(finders.find("assets/img/Singhealth-logo.png"), mode='rb') as f:
            image = MIMEImage(f.read())
            image.add_header('Content-ID', "<logo>")
            email.attach(image)
        email.send()


    """
    Sends email to tenant whose lease is expiring
    """
    @staticmethod
    def notify_tenant_lease_expiry(name, lease_end_date, email, time_left, connection):
        subject = "Upcoming Tenant Lease Expiry"
        message = f"""This email is to notify you on your upcoming lease expiry in {time_left} on {lease_end_date}.
        """
        context = {
            'expiry_date': lease_end_date,
            'owner_name': name,
            'time_left': time_left,
            'logo_name': "logo"
        }
        msg_html = render_to_string("email_templates/notify_lease_expiry.html", context)
        email = EmailMultiAlternatives(
            subject=subject,
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[email],
            connection=connection
        )
        email.attach_alternative(msg_html, "text/html")
        email.mixed_subtype = "related"
        with open(finders.find("assets/img/Singhealth-logo.png"), mode='rb') as f:
            image = MIMEImage(f.read())
            image.add_header('Content-ID', "<logo>")
            email.attach(image)
        email.send() 
