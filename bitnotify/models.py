from django.db import models
from django.conf import settings

from libbitcoin import satoshi_to_btc

from bitnotify import emails

class Wallet(models.Model):
    user = models.ForeignKey('auth.User')

    wallet = models.CharField(max_length=40)
    last_balance = models.IntegerField()

    def __unicode__(self):
        return u'%s %s %s' % (self.user, self.wallet, self.last_balance)

    def send_notification(self, balance):
        change = satoshi_to_btc(balance - self.last_balance)
        emails.send_wallet_notification(self.user.email, self.wallet, change)
