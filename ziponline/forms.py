from django.forms import ModelForm


from .models import Moving


class MvForm(ModelForm):
    class Meta:
        model = Moving
        fields = ('Moving_type', 'move_good', 'move_from', 'move_to', 'move_task', 'move_date')
