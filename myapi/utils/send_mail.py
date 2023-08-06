from django.core.mail import send_mail
import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datings_site.settings')
#settings.configure()


from_email = settings.EMAIL_HOST_USER


def send_email_to_users(user1_email, user2_email):
    to_user_2 = send_mail(
        'Прочти меня',
        f'Вы взаимно понравились пользователю {user1_email}',
        from_email,
        [user2_email],
        fail_silently=False,
    )

    to_user_1 = send_mail(
        'Прочти меня',
        f'Вы взаимно понравились пользователю {user2_email}',
        from_email,
        [user1_email],
        fail_silently=False,
    )

    return to_user_2, to_user_1