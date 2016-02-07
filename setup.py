from setuptools import setup, find_packages


setup(
    name='bitnotify',
    version='0.0.0',
    description='Send email notification after change on your bitcoin wallet or bip44 account',
    url='https://github.com/ondrejsika/bitnotify',
    author='Ondrej Sika',
    author_email='ondrej@ondrejsika.com',
    packages=find_packages(),
    install_requires=[
        'django==1.8.8',
        'requests==2.9.1',
        'gunicorn==19.4.5',
    ],
)

