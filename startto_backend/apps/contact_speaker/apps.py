from django.apps import AppConfig

class ContactSpeakerConfig(AppConfig):
    name = 'startto_backend.apps.contact_speaker'

    def ready(self):
        import startto_backend.apps.contact_speaker.signals