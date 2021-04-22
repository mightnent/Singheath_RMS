from io import BytesIO
from os import remove
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives, get_connection
from django.conf import settings
from datetime import date
from email.mime.image import MIMEImage
from audit.models import ChecklistInstance, ScoreTable, RectificationTable
from django.contrib.staticfiles import finders
import xlsxwriter

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
    Export checklist in Excel and sends to staff email
    """
    @staticmethod
    def checklist_export(username, user_email, checklist_id):
        current_checklist = ChecklistInstance.objects.filter(checklist_id=checklist_id)
        header = current_checklist.first()

        filename = "temp_excel.xlsx"
        EmailHandler._createExcel(filename, header, current_checklist)
        output = BytesIO()
        with open(filename, 'rb') as fh:
            output = BytesIO(fh.read())
        
        remove(filename) # cleanup
        subject = f"Exported {header.checklist_type} checklist for {header.tenant}"
        message = "Exported checklist is attached"
        context = {
            'username': username,
            'logo_name': "logo",
            'checklist_type': header.checklist_type,
            'tenant_name': header.tenant
        }
        msg_html = render_to_string("email_templates/export_checklist.html", context)
        email = EmailMultiAlternatives(
            subject=subject,
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[user_email]
        )
        email.attach_alternative(msg_html, "text/html")
        email.mixed_subtype = "related"
        email.attach(f'{header.checklist_type}checklist_{header.date}_{header.tenant}.xlsx', output.getvalue(), 'application/ms-excel')
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

    """
    Sends notification email to tenant when a new audit is performed
    """
    @staticmethod
    def notify_audit_performed(owner_email, audit_link, owner_name, checklist_id):
        checklist_objects = ChecklistInstance.objects.filter(checklist_id=checklist_id)
        scoreTable = ScoreTable.objects.filter(checklist_id=checklist_id)[0]
        base = checklist_objects[0]
        auditor_name = base.auditor
        score_percentage = "{:0.2f}".format((scoreTable.score / scoreTable.total)*100)
        closest_date = EmailHandler._getClosestDate(checklist_objects)

        subject = "New Audit Performed"
        message = f"This email is to notify you that {auditor_name} has performed a {base.checklist_type} audit."
        context = {
            'view_audit_link': audit_link,
            'auditor_name': auditor_name,
            'owner_name': owner_name,
            'checklist_type': base.checklist_type,
            'is_noncompliance': date(date.today().year+2, 12, 30) != closest_date,
            'score_percentage': score_percentage,
            'closest_date': closest_date,
            'logo_name': "logo"
        }
        msg_html = render_to_string("email_templates/notify_audit_performed.html", context)
        email = EmailMultiAlternatives(
            subject=subject,
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[owner_email]
        )
        email.attach_alternative(msg_html, "text/html")
        email.mixed_subtype = "related"
        with open(finders.find("assets/img/Singhealth-logo.png"), mode='rb') as f:
            image = MIMEImage(f.read())
            image.add_header('Content-ID', "<logo>")
            email.attach(image)
        email.send()

    """
    Sends notification email to tenant with upcoming non-compliance deadline
    """
    @staticmethod
    def notify_non_compliance_deadline(owner_email, owner_name, connection):
        subject = "Upcoming Non-compliance Rectification Deadline"
        message = f"This email is to notify you of outstanding non-compliance item(s) that require rectification by tomorrow."
        context = {
            'owner_name': owner_name,
            'logo_name': "logo"
        }
        msg_html = render_to_string("email_templates/non_compliance_reminder.html", context)
        email = EmailMultiAlternatives(
            subject=subject,
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[owner_email],
            connection=connection
        )
        email.attach_alternative(msg_html, "text/html")
        email.mixed_subtype = "related"
        with open(finders.find("assets/img/Singhealth-logo.png"), mode='rb') as f:
            image = MIMEImage(f.read())
            image.add_header('Content-ID', "<logo>")
            email.attach(image)
        email.send()
    
    """
    Creates excel version of checklist
    """
    @staticmethod
    def _createExcel(filename, header, checklist_queryset):
        with xlsxwriter.Workbook(filename, {'constant_memory': True}) as workbook:
                row = 0
                worksheet = workbook.add_worksheet()
                worksheet.set_column(0, 0, 60)
                worksheet.set_column(2, 2, 25)

                ### SET FORMATTING OPTIONS
                bold = workbook.add_format({'bold': 1})
                section_header = workbook.add_format({'bold': 1, 'border': 1})
                subsection_header = workbook.add_format({'bold': 1, 'bg_color': "#ccffcc", 'border': 1})
                table_cell = workbook.add_format({'border': 1, 'text_wrap': True})
                score_footer = workbook.add_format({'bold': 1, 'bg_color': "#999999", 'border': 1, 'align': 'right'})
                rectification_header = workbook.add_format({'bold': 1, 'bg_color': "#D9D9D9", 'border': 1, 'text_wrap': True})
                ### END SET FORMATTING OPTIONS


                ### BEGIN WRITE GENERAL DATA
                worksheet.write(row, 0, 'Date: ', bold)
                worksheet.write(row, 1, header.date.strftime("%d %B %Y"))
                row += 1

                worksheet.write(row, 0, 'Auditee: ', bold)
                worksheet.write(row, 1,  f"{header.tenant} at {header.tenant_location}")
                row += 1

                worksheet.write(row, 0, 'Auditor: ', bold)
                worksheet.write(row, 1,  header.auditor)
                row += 1
                ### END WRITE GENERAL DATA
                section_dict = {}
                section_score = []
                ## GET SECTIONS AND SUBSECTIONS
                for instance in checklist_queryset:
                    if (instance.section not in section_dict):
                        section_dict[instance.section] = [instance.subsection]
                    if (instance.subsection not in section_dict[instance.section]):
                        section_dict[instance.section].append(instance.subsection)
                ## END GET SECTIONS AND SUBSECTIONS
                
                row += 1
                ### WRITE MAIN CONTENTS
                for (section_name, section_data) in section_dict.items():
                    worksheet.write(row, 0, section_name, section_header)
                    worksheet.write(row, 1, 'Result', section_header)
                    worksheet.write(row, 2, 'Comments (if any)', section_header)
                    row += 1

                    start_row = row + 1
                    for subsection in section_data:
                        worksheet.merge_range(row, 0, row, 2, subsection, subsection_header)
                        row += 1

                        subsection_data = checklist_queryset.filter(subsection = subsection)
                        ## FOR EACH QUESTION
                        for data in subsection_data:
                            worksheet.write(row, 0, data.question, table_cell)
                            worksheet.write(row, 1, data.score, table_cell)
                            worksheet.write(row, 2, data.comment, table_cell)
                            # CREATE IMAGE/RECTIFICATION SHEET
                            if (data.photo) or (data.date_due):
                                sheetImage = workbook.add_worksheet(f"rectificationThreadForA{row+1}")
                                rectification_row = 0
                                sheetImage.set_column(0, 0, 13)
                                sheetImage.merge_range(rectification_row, 0, rectification_row, 2, data.question, rectification_header)
                                rectification_row += 1
                                sheetImage.write(rectification_row, 0, "Date taken: ", bold)
                                sheetImage.write(rectification_row, 1, data.date.strftime("%d %B %Y"))
                                rectification_row += 1
                                if (data.photo):
                                    scale = 200/data.photo.height
                                    sheetImage.insert_image(rectification_row, 0, "."+data.photo.url, {'x_scale': scale, 'y_scale': scale})
                                    rectification_row += 11

                                if (data.comment):
                                    sheetImage.write(rectification_row, 0, "Comment: ", bold)
                                    sheetImage.write(rectification_row, 1, data.comment)
                                    rectification_row += 1
                               
                                rectification_row += 2
                                # RECTIFICATION FOLLOW UPS
                                rectificationTableData = RectificationTable.objects.filter(row_id = data.id).order_by("date_created")
                                if len(rectificationTableData) > 0:
                                    sheetImage.write(rectification_row, 0, "Tenant Follow ups", bold)
                                    rectification_row += 1
                                    for i in rectificationTableData:
                                        sheetImage.write(rectification_row, 0, "Date: ", bold)
                                        sheetImage.write(rectification_row, 1, i.date_created.strftime("%d %B %Y"))
                                        rectification_row += 1
                                        if (i.photo):
                                            scale = 200/i.photo.height
                                            sheetImage.insert_image(rectification_row, 0, "."+i.photo.url, {'x_scale': scale, 'y_scale': scale})
                                            rectification_row += 11
                                        if (i.update):
                                            sheetImage.write(rectification_row, 0, "Comment: ", bold)
                                            sheetImage.write(rectification_row, 1, i.comment)
                                            rectification_row += 1
                                        rectification_row += 2
                                # END RECTIFICATION FOLLOW UPS
                            # END CREATE IMAGE/RECTIFICATION SHEET
                            row += 1
                        ## END FOR EACH SECTION

                    ## WRITE SCORE FOOTER
                    worksheet.write(row, 0, "Score: ", score_footer)
                    worksheet.write_formula(row, 1, f'=SUM(B{start_row}:B{row})', score_footer)
                    section_score.append(row+1)
                    row += 2
                    ## END WRITE SCORE FOOTER
                ### END WRITE MAIN CONTENTS

                ### START FINAL OVERALL SCORE SECTION
                worksheet.write(row, 0, "Overall score: ", bold)
                row += 1
                score_section_start = row + 1
                for section_no, (section_name, section_data) in enumerate(section_dict.items()):
                    worksheet.write(row, 0, section_name)
                    worksheet.write_formula(row, 1, f"B{section_score[section_no]}")
                    row += 1
                worksheet.write(row, 0, "Total")
                worksheet.write_formula(row, 1, f'=SUM(B{score_section_start}:B{row})')
                ### END FINAL OVERALL SCORE SECTION

    """
    Get closest non-compliance date
    """
    @staticmethod
    def _getClosestDate(checklist_object):
        today = date.today()
        latest = date(today.year+2, 12, 30)
        for i in checklist_object:
            if (i.date_due):
                if (i.date_due - today) < (latest - today):
                    latest = i.date_due
        return latest
