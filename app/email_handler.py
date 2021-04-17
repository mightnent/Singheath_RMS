from io import BytesIO
from os import remove
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives, get_connection
from django.conf import settings
from email.mime.image import MIMEImage
from audit.models import ChecklistInstance
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
                ## GET SECTIONS AND SUBSECTIONS
                for instance in checklist_queryset:
                    if (instance.section not in section_dict):
                        section_dict[instance.section] = [instance.subsection]
                    if (instance.subsection not in section_dict[instance.section]):
                        section_dict[instance.section].append(instance.subsection)
                ## END GET SECTIONS AND SUBSECTIONS
                
                row += 1
                ### WRITE MAIN CONTENTS
                for section_no, (section_name, section_data) in enumerate(section_dict.items(), 1):
                    worksheet.write(row, 0, f'{section_no}: {section_name}', section_header)
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
                            # CREATE IMAGE SHEET
                            if (data.photo):
                                sheetImage = workbook.add_worksheet(f"imageForA{row+1}")
                                sheetImage.set_column(0, 0, 13)
                                scale = 400/data.photo.height
                                sheetImage.write(0, 0, "Date taken: ", bold)
                                sheetImage.write(0, 1, data.date.strftime("%d %B %Y"))
                                sheetImage.insert_image(1, 0, "."+data.photo.url, {'x_scale': scale, 'y_scale': scale})
                                sheetImage.write(11, 0, "Comment: ", bold)
                                sheetImage.write(11, 1, data.comment)
                            # END CREATE IMAGE SHEET
                            row += 1
                        ## END FOR EACH SECTION

                    ## WRITE SCORE FOOTER
                    worksheet.write(row, 0, "Score: ", score_footer)
                    worksheet.write_formula(row, 1, f'=SUM(B{start_row}:B{row})', score_footer)
                    row += 1
                    row += 1 # give empty line
                    ## END WRITE SCORE FOOTER
                ### END WRITE MAIN CONTENTS

                ### START FINAL OVERALL SCORE SECTION
                worksheet.write(row, 0, "Overall score: ", bold)
                row += 1
                score_section_start = row + 1
                for section_name, section_data in section_dict.items():
                    worksheet.write(row, 0, section_name)
                    worksheet.write(row, 1, 10)
                    row += 1
                worksheet.write(row, 0, "Total")
                worksheet.write_formula(row, 1, f'=SUM(B{score_section_start}:B{row})')
                ### END FINAL OVERALL SCORE SECTION
