from django_mako_plus import view_function
from django import forms

@view_function
def process_request(request):
    #process the form
    form = testForm()

    #render the form
    context = {
        'form': form,
    }
    return request.dmp.render('formtest.html', context)


class testForm(forms.Form):
    name = forms.CharField(label = "Name")
    date = forms.DateField(label = "Date")
    comment = forms.CharField(label = "Your comment")
