# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitnotify', '0003_xpubwallet_i'),
    ]

    operations = [
        migrations.AddField(
            model_name='xpubwallet',
            name='is_used',
            field=models.BooleanField(default=False),
        ),
    ]
