from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone

@view_function
def process_request(request):

    #process the form
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            #do the work of the form
            #make the payment
            #create the user
            return HttpResponseRedirect('/')

    else:
        form = TestForm()

    #render the template
    context = {
        #'form' = form,
    }
    return request.dmp_render('testform.html', context)

class testForm(forms.Form):
    comment = forms.CharField(label="your comment")
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
