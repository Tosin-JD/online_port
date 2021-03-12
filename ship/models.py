import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()


""" DOCK & SHIP MODELS """

class State(models.TextChoices):
    offloaded = ('oo', 'OFFLOADED')
    due_to_offload = ('dd', 'DUE TO OFFLOAD')
    not_offloaded = ('yy', 'NOT OFFLOADED')


class Dock(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    docked_ship = models.OneToOneField('Ship', related_name='dock', null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        name = self.name if self.name else '--'
        return '%s' % (self.name)


class DockManifest(models.Model):
    dock = models.ForeignKey(Dock,  on_delete=models.CASCADE,
                                     related_name='manifests')
    ship = models.ForeignKey('Ship', on_delete=models.CASCADE)
    arrival = models.DateTimeField(help_text='yyyy-mm-dd')
    departure = models.DateTimeField(null=True, blank=True, help_text='yyyy-mm-dd')
    current_position = models.CharField(max_length=2, choices=State.choices,
                                        default=State.not_offloaded)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def is_due_offload(self):
        if (self.current_position == 'dd'):
            return True
        return False

    def is_offloaded(self):
        if (self.current_position == 'oo'):
            return True
        return False

    def is_not_offloaded(self):
        if (self.current_position == 'yy'):
            return True
        return False

    def __str__(self):
        return 'Ship {} at dock {}\'s Manifest'.format(self.ship, self.dock)

    class Meta:
        ordering = ('-timestamp',)



class Ship(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    captain = models.ForeignKey('ShipCaptain', blank=True, null=True,\
                                on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='ship')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        name = self.name if self.name else '--'
        return '%s' % (self.name)


class Cargo(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    content = models.CharField(max_length=30)
    current_position = models.CharField(max_length=2, choices=State.choices, default=State.not_offloaded)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        name = self.name if self.name else '--'
        return '%s' % (self.name)


class Container(models.Model):
    hazards = models.ManyToManyField('CargoHazard')
    ship = models.ForeignKey('Ship', related_name='containers', null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.container_id)

    def get_hazards_string(self):
        return ", ".join([hazard.name for hazard in self.hazards.all()])


class CargoHazard(models.Model):
    name = models.CharField(max_length=50, unique=True)
    web_icon = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


""" STAKEHOLDER MODELS """


class DockSupervisor(models.Model):
    employee = models.OneToOneField('DockEmployee', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return '%s %s' % (self.employee.person.get_first_name(), self.employee.person.get_last_name())


class DockEmployee(models.Model):
    person = models.OneToOneField('Person', on_delete=models.CASCADE)
    dock = models.ForeignKey(Dock, on_delete=models.CASCADE,
                             related_name='employees', null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return '%s %s' % (self.person.get_first_name(), self.person.get_last_name())

    def is_supervisor(self):
        return bool(self.docksupervisor)
    is_supervisor.boolean = True


class ShipCaptain(models.Model):
    person = models.OneToOneField('Person', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return '%s %s ' % (self.person.get_first_name(), self.person.get_last_name())


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bank_account_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return '%s %s' % (self.get_first_name(), self.get_last_name())

    def get_first_name(self):
        return self.user.first_name

    def get_last_name(self):
        return self.user.last_name

    def get_email(self):
        return self.user.email


class Address(models.Model):
    ADDRESS_TYPE_CHOICES = (
        ('Home Address', 'Home Address'),
        ('Postal Address', 'Postal Address'),
        ('Other', 'Other'),
    )

    person = models.ForeignKey('Person', null=True, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=50, default='Home Address', choices=ADDRESS_TYPE_CHOICES)
    street_name = models.CharField(max_length=50)
    street_number = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    class Meta:
        unique_together = ('person', 'address_type',)
