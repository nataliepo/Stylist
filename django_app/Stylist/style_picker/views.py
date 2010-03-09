from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response

import simplejson, urllib
from Stylist.style_picker.models import ColorPickerWidget, TydgetField, TextFieldWidget


def index(request):
    color_chosen = ""
    submitted = 0
    cp_widget = ColorPickerWidget()
    
    tydget_list = initialize_form_data()
    css_results = ""
    
    # update the fields if this is a POST.
    if request.method == 'POST':
        # this is the submitted data
        form = request.POST
        submitted = 1

        for t in tydget_list:
            t['obj'].value = form[t['obj'].input_id]
            t['obj'].quick_render = t['obj'].render()
    
    
    return render_to_response('color_picker.html', {
        
        'css': cp_widget.Media.css['all'],
        'js': cp_widget.Media.js,
        'field_list': tydget_list,
                
        'submitted': submitted,
        'css_results': css_results,
    })
    

def initialize_form_data():
    
    tydget_list = load_from_file()
    
    return tydget_list
    


def load_from_file():
    url = 'http://localhost/sample.json'
    result = simplejson.load(urllib.urlopen(url))
    
    tydget = [ ] 

    for t in result['entries']:
        obj = t['obj']
        tydget.append({'obj' : TydgetField(t['obj']), 
            'class': t['section'],
            'can_customize': t['can_customize'] })


    return tydget    
    
    