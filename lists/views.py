from django.shortcuts import redirect, render

from lists.models import Item, List

HOME_TEMPLATE_PATH = 'home.html'
LIST_TEMPLATE_PATH = 'list.html'


def home_page(request):
    return render(request, HOME_TEMPLATE_PATH)


def view_list(request):
    items = Item.objects.all()
    return render(request, LIST_TEMPLATE_PATH, {'items': items})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('view_list')
