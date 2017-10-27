import os
from time import sleep
from random import randint

os.environ.setdefault ('DJANGO_SETTINGS_MODULE', 'guestbook.settings')

import django
django.setup ()

from django.utils import timezone
from guestbookapp.models import Entry

Entry.objects.all ().delete ()

names = ('Catrin Morgan', 'Cletus Spalding', 'Grigor Martel', 'Finnegan Draper', 'Zac Quincy',
         'Grigor Martel', 'Terrence Sutherland', 'Terrence Sutherland', 'Zac Quincy',
         'Grigor Martel', 'Katharine McKenzie', 'Zac Quincy',
         )
comments = ('Nice use of contrast in this colour palette.',
            'It\'s splendid not just sleek!', 'This is alluring work!',
            'Super thought out! Leading the way, mate.',
            'My 49 year old daughter rates this shot very splendid :)', 'Such shot, many button, so simple.',
            'Looks revolutionary and admirable, friend.', 'I want to learn this kind of shot! Teach me.',
            'Incredible work you have here.', 'Engaging. It keeps your mind occupied while you wait.',
            'White. This is new school.', 'I approve your shot.',
            )

for i in range (len (names)):
    sleep (randint (5, 12))
    print ('#', end = '', flush = True)
    now = timezone.now ()
    Entry.objects.get_or_create (user = names [i], comment = comments [i], created_at = now, updated_at = now)

print ()