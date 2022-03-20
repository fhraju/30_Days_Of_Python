from http import server
from logging import raiseExceptions
from math import fabs
from operator import truediv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from templates import Template

# environment variables
username = 'email@gmail.com'
password = 'email_password'

class Emailer():
    subject = ""
    context = {}
    to_emails = []
    from_email="email_name"
    has_html = False
    test_send = False
    template_html = None
    template_name = None

    def __init__(self, subject="", template_name=None, context={}, template_html=None, to_emails=None, test_send=False):
        if template_name==None and template_html==None:
            raise Exception("You must set a template name")
        assert isinstance(to_emails, list)
        self.to_emails = to_emails
        self.subject = subject
        if template_html  != None:
            self.has_html = True
            self.template_html = template_html
        self.template_name = template_name
        self.context = context
        self.test_send = test_send

    def format_msg(self):
        msg = MIMEMultipart('alternative')
        msg['From'] = self.from_email
        msg['To'] = ", ".join(self.to_emails)
        msg['Subject'] = self.subject

        if self.template_name != None:
            temple_string = Template(template_name=self.template_name, context = self.context)
            txt_part = MIMEText(temple_string.render(), 'plain')
            print(txt_part)
            msg.attach(txt_part)

        if self.template_html != None:
            temple_string = Template(template_name=self.template_html, context = self.context)
            html_part = MIMEText(temple_string.render(), 'html')
            print(html_part)
            msg.attach(html_part)
        msg_string = msg.as_string()
        return msg_string

    def send(self):
        msg = self.format_msg()
        # login to my smtp server
        did_send = False
        if not self.test_send:
            with smtplib.SMTP(host = 'smtp.gmail.com', port=587) as server:
                server.ehlo()
                server.starttls()
                server.login(username, password)
                try:
                    server.sendmail(from_email, to_emails, msg_string)
                    did_send = True
                except:
                    did_send = False
        return did_send

