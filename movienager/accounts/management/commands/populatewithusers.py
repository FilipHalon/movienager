from django.core.management.base import BaseCommand

from accounts.factory.user_factory import UserFactory


class Command(BaseCommand):
    help = "Populates the database with users."

    def add_arguments(self, parser):
        parser.add_argument(
            "--num",
            default=100,
            type=int,
            help="You can specify the number of users to create.",
        )

    def handle(self, *args, **options):
        for _ in range(options["num"]):
            UserFactory.create()
