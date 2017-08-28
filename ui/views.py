from django.shortcuts import render

# Create your views here.
def index(request):
    context_built = {'data': 'I am data'}
    return render(request, template_name='ui/index.html', context=context_built)