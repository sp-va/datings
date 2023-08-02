from myapi.models import UsersMatching


def matching_users(user1_email, user2_email):
    match_exsists = UsersMatching.objects.filter(user1_email=user2_email, user2_email=user1_email).exists()

    if not match_exsists:
        new_match = UsersMatching(user1_email=user1_email.email, user2_email=user2_email.email)
        new_match.save()


