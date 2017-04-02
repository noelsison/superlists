from django.shortcuts import redirect, render

from lists.models import Item

HOME_TEMPLATE_PATH = 'home.html'


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, HOME_TEMPLATE_PATH, {'items': items})
