from django.shortcuts import render

from ContactApp.Forms import ContactForm

def getcontactpage(request):
    contact = ContactForm()
    return render(request, 'context.html', {'form': contact})

def validationdata(request):
    cf = ContactForm(request.POST)
    if cf.is_valid():
        input_data = cf.cleaned_data
        return render(request, 'display.html', {'data': input_data})
    else:
          return render(request, 'context.html', {'form': cf})

