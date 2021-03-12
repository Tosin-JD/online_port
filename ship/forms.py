from django.forms import ModelForm
from .models import Cargo, DockManifest


class DockManifestForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(DockManifestForm, self).__init__(*args, **kwargs)
        self.fields['ship'].widget.attrs['class'] = 'form-control'
        self.fields['arrival'].widget.attrs['class'] = 'form-control'
        self.fields['departure'].widget.attrs['class'] = 'form-control'
        self.fields['dock'].widget.attrs['class'] = 'form-control'
        
        self.fields['arrival'].widget.attrs['placeholder'] = 'yyyy-mm-dd'
        self.fields['departure'].widget.attrs['placeholder'] = 'yyyy-mm-dd'
        
    class Meta:
        model = DockManifest
        fields = ('dock', 'ship', 'arrival', 'departure',)


class CargoForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(CargoForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['class'] = 'form-control'
        
    class Meta:
        model = Cargo
        fields = ('name', 'content',)
        






