from django.contrib import admin
from django.contrib import admin
from  .models import (CargoHazard,
                        Dock, DockManifest,
                        DockSupervisor,
                        ShipCaptain,
                        Person, Ship)

# Register your models here.
admin.site.register(Dock)
admin.site.register(CargoHazard)
admin.site.register(DockSupervisor)
admin.site.register(Person)
admin.site.register(Ship)
admin.site.register(ShipCaptain)
admin.site.register(DockManifest)
