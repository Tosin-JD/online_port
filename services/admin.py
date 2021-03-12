from django.contrib import admin
from .models import (AnimatedIntro,
                    Service,
                     WelcomeNote)

# Register your models here.
admin.site.register(AnimatedIntro)
admin.site.register(Service)
admin.site.register(WelcomeNote)




