from django.contrib.auth.models import User

from libbitcoin import get_balance, get_wallet_from_xpub, get_txs_count

from bitnotify.models import XpubWallet

BIP44_OFFSET = 20

def cron():
    for user in User.objects.all():
        # single wallets
        for wallet in user.wallet_set.all():
            balance = get_balance(wallet.wallet)
            if wallet.last_balance != balance:
                wallet.send_notification(balance)
                wallet.last_balance = balance
                wallet.save()

        # xpubs
        for xpub in user.xpub_set.all():
            for wallet in xpub.xpubwallet_set.all().order_by('i'):
                balance = get_balance(wallet.wallet)
                if get_txs_count(wallet.wallet):
                    wallet.is_used = True
                    wallet.save()
                if wallet.last_balance != balance:
                    wallet.send_notification(balance)
                    wallet.last_balance = balance
                    wallet.save()

            # Create new wallets from xpub
            try:
                last_used = xpub.xpubwallet_set.filter(is_used=True).order_by('i').last().i
            except AttributeError:
                last_used = 0
            try:
                last_generated = xpub.xpubwallet_set.all().order_by('i').last().i
            except AttributeError:
                last_generated = 0

            if last_used + BIP44_OFFSET > last_generated:
                for i in range(last_used + BIP44_OFFSET - last_generated):
                    i = i + last_generated + 1
                    XpubWallet(xpub=xpub, i=i, last_balance=0, wallet=get_wallet_from_xpub(xpub.xpub, i)).save()
