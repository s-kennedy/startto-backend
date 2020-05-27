from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'startto_backend.apps.accounts'

    def ready(self):
        from startto_backend.apps.accounts import signals
