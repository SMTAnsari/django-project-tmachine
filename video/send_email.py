from django.core.mail import send_mail

recipient_email = 'recipient@example.com'
recipient_name = 'John Doe'

subject = 'Thanks for Registration'
message = f"Dear {recipient_name},\n\nThank you for registering. We appreciate your interest in our service.\n\nBest regards,\nThe Team"

send_mail(
    subject,
    message,
    'maheshreddyqq@gmail.com',
    [recipient_email],
    fail_silently=False,
)
