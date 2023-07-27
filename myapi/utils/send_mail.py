from django.core.mail import send_mail
import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datings_site.settings')
# settings.configure()


subject = 'Read this message'
message = 'Xyulo vanu4ee'
from_email = settings.EMAIL_HOST_USER
to_email = ['podpekaev@gmail.com']

def send_email_to_users(user_1, user_2):
    to_user_2 = send_mail(
        'Прочти меня',
        f'Вы взаимно понравились пользователю {user_1.username}',
        from_email,
        [user_2.email],
        fail_silently=False,
    )

    to_user_1 = send_mail(
        'Прочти меня',
        f'Вы взаимно понравились пользователю {user_2.username}',
        from_email,
        [user_1.email],
        fail_silently=False,
    )

    return to_user_2, to_user_1