# BitNotify

Send email notification after change on your bitcoin wallet or bip44 account

- author: Ondrej Sika <ondrej@ondrejsika.com>


## Installation

Setup base project

    git clone git@github.com:ondrejsika/bitnotify.git
    cd bitnotify
    virtualenv .env
    source .env/bin/activate
    pip install -e .
    ./manage.py migrate

Run in gunicorn

    gunicorn wsgi -b 0.0.0.0:9999

Setup cron job

    # add to your crontab
    * * * * * cd /home/projects/bitnotify && .env/bin/python manage.py bitnotify_cron

## Live version

__<http://bitnotify.sikaapp.cz>__


