from django.core.mail import EmailMessage
from django.conf import settings

def send_ticket_notification(ticket, sender_email, recipient_email, note):
    subject = f"Ticket Update: {ticket.title}"
    message = (f"Dear User,\n\n"
               f"Your ticket with the following details has been updated:\n\n"
               f"Title: {ticket.title}\n"
               f"Status: {ticket.status}\n"
               f"Note: {note}\n\n"
               f"Regards,\n"
               f"Support Team")
    
    email = EmailMessage(
        subject,
        message,
        sender_email,  # Sender email
        [recipient_email],  # Recipient email
        headers={'Reply-To': sender_email}  # This ensures replies go to the sender email
    )
    email.send(fail_silently=False)