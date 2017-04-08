from django.shortcuts import redirect, render

from lists.models import Item

HOME_TEMPLATE_PATH = 'home.html'
LIST_TEMPLATE_PATH = 'list.html'


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/best-list-the-world-has-ever-seen/')
    return render(request, HOME_TEMPLATE_PATH)


def view_list(request):
    items = Item.objects.all()
    return render(request, LIST_TEMPLATE_PATH, {'items': items})
