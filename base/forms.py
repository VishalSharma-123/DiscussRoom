from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'                      #will create every field in Room database model
        exclude = ['host', 'participants']