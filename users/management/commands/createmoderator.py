from django.core.management import BaseCommand
from users.models import User
from django.contrib.auth.models import Group


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email="moderator@sky.pro",
            first_name="moderator",
            last_name="content",
            is_staff=True,
            is_superuser=False,
            phone="777777777",
        )
        group = Group.objects.get(name="Модератор")
        user.groups.add(group)
        user.set_password("123")
        user.save()
