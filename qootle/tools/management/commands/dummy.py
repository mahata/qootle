import polib
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    Usage = """
    $ python manage.py dummy /PATH/TO/POFILE.po
    """

    def handle(self, *args, **kwargs):
        """
        ToDo: Nicer Description

        from PO to DB
        """
        if len(args) != 1:
            raise CommandError(self.Usage)

        try:
            po_entries = polib.pofile(args[0])
        except OSError:
            raise CommandError("%s is not a proper PO file." % args[0])

        for entry in po_entries:
            print(entry)
