from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.template.loader import render_to_string

import simplejson, urllib
from Stylist.style_picker.models import ColorPickerWidget, TydgetField, TextFieldWidget


def index(request):
    color_chosen = ""
    submitted = 0
    cp_widget = ColorPickerWidget()
    
    tydget_list = load_styles_from_file()
    css_results = ""
    
    # update the fields if this is a POST.
    if request.method == 'POST':
        # this is the submitted data
        form = request.POST
        submitted = 1

        for t in tydget_list:
            t['obj'].value = form[t['obj'].input_id]
            t['obj'].quick_render = t['obj'].render()
            
#        chosen_site = form['motion-choice']
    
    css_results = render_to_string('resulting_css.html', { 'field_list': tydget_list })
    
    return render_to_response('color_picker.html', {
        
        'css': cp_widget.Media.css['all'],
        'js': cp_widget.Media.js,
        'field_list': tydget_list,
                
        'submitted': submitted,
        'resulting_css': css_results,
#        'site_list': site_list,
#        'chosen_site': chosen_site,
    })

def load_styles_from_file():
    url = 'http://localhost/vanilla.json'
    result = simplejson.load(urllib.urlopen(url))
    
    tydget = [ ] 

    headings = result.keys()
    
    for heading in headings:
        classes = result[heading]
        
        # classes is a hash of class names.
        class_keys = classes.keys()
        
        for class_key in class_keys:
            # key is an array.
            class_tuple = classes[class_key]
            for obj in class_tuple:              
                tydget.append({'obj': TydgetField(obj, class_key),
                'class': class_key,
                'heading': heading,
                'can_customize': obj['can_customize']})
 
    return tydget    
    
def load_sites_from_file ():
    url = 'http://localhost/sites.json'

    site_list = { }
    result = simplejson.load(urllib.urlopen(url))
    
    for site in result['sites']:
        site_list[site['xid']] = site['name']
        
    return site_list
    