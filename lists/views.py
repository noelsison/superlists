from django.shortcuts import redirect, render

from lists.models import Item, List

HOME_TEMPLATE_PATH = 'home.html'
LIST_TEMPLATE_PATH = 'list.html'


def home_page(request):
    return render(request, HOME_TEMPLATE_PATH)


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(
        request,
        LIST_TEMPLATE_PATH,
        {
            'list': list_
        }
    )


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')
