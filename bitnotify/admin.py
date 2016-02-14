from django.contrib import admin

from bitnotify.models import Wallet, Xpub, XpubWallet


admin.site.register(Wallet)
admin.site.register(Xpub)
admin.site.register(XpubWallet)

