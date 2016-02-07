from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail


def _send_mail_base(email_from, email_to, subject, body):
    send_mail(subject, body, email_from, [email_to], fail_silently=False)


def _send_mail(email_to, subject_template, body_template, context):
    _send_mail_base(settings.DEFAULT_EMAIL_FROM,
                   email_to,
                   render_to_string(subject_template, context).replace('\n', ''),
                   render_to_string(body_template, context))


def send_wallet_notification(email, wallet, change):
    subject_template = 'bitnotify/emails/send_wallet_notification_subject.txt'
    subject_body = 'bitnotify/emails/send_wallet_notification_body.txt'

    context = {
        'wallet_short': wallet[:8],
        'wallet': wallet,
        'change': change,
    }
    _send_mail(email, subject_template, subject_body, context)

