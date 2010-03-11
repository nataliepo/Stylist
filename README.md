# Configuration

Make sure the django_app/Stylist/settings.py TEMPLATE_DIRS value references the correct absolute path for your django_frontend directory.


# Usage
First, take a json feed (example in web_utils/sample.json) of defined elements and place it in your localhost folder. Make sure you can view it here:
 	http://localhost/vanilla.json

Then, start up the django webserver:

    cd django_app/Stylist
    
    # run the server
    python manage.py runserver

View it in your browser - http://127.0.0.1:8000/ by default.  

Change the color or text elements and click 'Submit' to generate css.  The elements that you see on the form have the can_customize values set to 1; all other values are defaults.


# To Do
* add url picker to auto-insert the js scripts
* add in a preview
*  