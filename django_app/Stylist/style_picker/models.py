from django.db import models

from style_picker.widgets import ColorPickerWidget, TextFieldWidget

class ColorField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorPickerWidget
        return super(ColorField, self).formfield(**kwargs)

class TextField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 30
        super(TextField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = TextFieldWidget
        return super(TextField, self).formfield(**kwargs)
        
 
class TydgetField(models.Model):
    input_id = models.CharField(max_length=30)
    label = models.CharField(max_length=30)
    input_type = models.CharField(max_length=10)
    value = models.CharField(max_length=100)
    class_name = models.CharField(max_length=30)
    
    def __init__(self, obj, class_name):
#        input_id, input_label, input_type, value, class_name):
        self.input_id = class_name + '-' + obj['id']
        self.element = obj['id']
        self.label = obj['label']
        self.input_type = obj['type']
        self.value = obj['value']
        self.class_name = class_name
        self.quick_render = self.render()
        
        
    def render(self):
        if (self.input_type == 'color'):

            cp_widget = ColorPickerWidget()
            # always show the picker in case they want to pick again.
            return cp_widget.render(self.input_id, self.value, {
                'id': self.input_id,
            })
        else:
            txt_widget = TextFieldWidget()
            return txt_widget.render(self.input_id, self.value)



        
