from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Show user registration date'

    def add_arguments(self, parser):
        parser.add_argument('user_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        user_ids = options.get('user_ids', [])
        users = User.objects.filter(id__in=user_ids)
        if not users:
            self.stdout.write('No users with this ids.')
        for user in users:
            self.stdout.write(f'id: {user.id} | register on: {user.date_joined.strftime("%m/%d/%Y, %H:%M:%S")}')
