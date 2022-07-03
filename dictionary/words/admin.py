from django.contrib import admin
from .models import Words, TextWithWord,RandomWordForHomeView

admin.site.register(Words)
admin.site.register(TextWithWord)
admin.site.register(RandomWordForHomeView)
