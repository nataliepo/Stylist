from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response

import simplejson, urllib
from Stylist.style_picker.models import ColorPickerWidget, TydgetField, TextFieldWidget


def index(request):
    color_chosen = ""
    submitted = 0
    cp_widget = ColorPickerWidget()
    
    tydget_list = load_styles_from_file()
    css_results = ""
#    site_list = load_sites_from_file()
#    chosen_site = ""
    
    # update the fields if this is a POST.
    if request.method == 'POST':
        # this is the submitted data
        form = request.POST
        submitted = 1

        for t in tydget_list:
            t['obj'].value = form[t['obj'].input_id]
            t['obj'].quick_render = t['obj'].render()
            
#        chosen_site = form['motion-choice']
    
    
    return render_to_response('color_picker.html', {
        
        'css': cp_widget.Media.css['all'],
        'js': cp_widget.Media.js,
        'field_list': tydget_list,
                
        'submitted': submitted,
        'css_results': css_results,
#        'site_list': site_list,
#        'chosen_site': chosen_site,
    })

def load_styles_from_file():
    url = 'http://localhost/vanilla.json'
    result = simplejson.load(urllib.urlopen(url))
    
    tydget = [ ] 

    keys = result.keys()

    for key in keys:
        # key is an array.
        class_tuple = result[key]
        for obj in class_tuple:
            class_name = "." + key
            if (obj['sub_class']):
                class_name = obj['sub_class'] + class_name
                
            tydget.append({'obj': TydgetField(obj, key),
#            'class': key,
            'class': class_name,
            'can_customize': obj['can_customize']})
 
    return tydget    
    
def load_sites_from_file ():
    url = 'http://localhost/sites.json'

    site_list = { }
    result = simplejson.load(urllib.urlopen(url))
    
#    for site in result['sites']:
#        site_list.append({'xid': site['xid'], 'name': site['name']})
    for site in result['sites']:
        site_list[site['xid']] = site['name']
        
    return site_list
    