from django.contrib.auth.models import User

TEST_GROUP = 'test'
ADMIN_GROUP = 'admin'


def get_tester():
    all_users = User.objects.all()
    tester = []
    for user in all_users:
        if user.groups.filter(name=TEST_GROUP).exists():
            tester.append(user)
    return tester

