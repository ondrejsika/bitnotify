# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitnotify', '0002_xpub_xpubwallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='xpubwallet',
            name='i',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
