import os
from django.core.management import BaseCommand
from dotenv import load_dotenv

from users.models import User

load_dotenv()


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create()

        user.set_password(os.getenv('SU_PASSWORD'))
        user.save()
