from django.shortcuts import render

HOME_TEMPLATE_PATH = 'home.html'


def home_page(request):
    return render(request, HOME_TEMPLATE_PATH, {
        'new_item_text': request.POST.get('item_text', '')
    })
