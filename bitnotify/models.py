from django.db import models

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


class Xpub(models.Model):
    user = models.ForeignKey('auth.User')

    xpub = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s %s' % (self.user, self.xpub)


class XpubWallet(models.Model):
    xpub = models.ForeignKey(Xpub)
    i = models.IntegerField()
    is_used = models.BooleanField(default=False)

    wallet = models.CharField(max_length=40)
    last_balance = models.IntegerField()

    class Meta:
        unique_together = ('xpub', 'i')

    def __unicode__(self):
        return u'%s %s %s %s %s %s' % (self.xpub.user, self.xpub.xpub[:10], self.is_used, self.i, self.wallet, self.last_balance)

    def send_notification(self, balance):
        change = satoshi_to_btc(balance - self.last_balance)
        emails.send_xpub_notification(self.xpub.user.email, self.xpub.xpub, self.wallet, change)
