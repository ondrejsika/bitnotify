# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitnotify', '0004_xpubwallet_is_used'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='xpubwallet',
            unique_together=set([('xpub', 'i')]),
        ),
    ]
