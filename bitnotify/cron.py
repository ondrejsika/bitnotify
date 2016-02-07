from django.contrib.auth.models import User

from libbitcoin import get_balance


def cron():
    for user in User.objects.all():
        for wallet in user.wallet_set.all():
            balance = get_balance(wallet.wallet)
            if wallet.last_balance != balance:
                wallet.send_notification(balance)
                wallet.last_balance = balance
                wallet.save()

