from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from item.forms import ItemForm
from item.models import Item
from .forms import CreateUserForm


# Create your views here.

@login_required(login_url='/login')
def item_list_view(req):
    keyword = req.GET.get('keyword')
    field = req.GET.get('field')

    if keyword:
        if field == 'code':
            items = Item.objects.filter(code__icontains=keyword)
        elif field == 'name':
            items = Item.objects.filter(name__icontains=keyword)
        elif field == 'category':
            items = Item.objects.filter(category__name__icontains=keyword)
    else:
        items = Item.objects.all()

    fields = [field.name for field in Item._meta.get_fields() if field.name != 'id' and field.name !=
              'count' and field.name != 'cost' and field.name != 'description']

    context = {
        'keyword': keyword,
        'items': items.order_by('code'),
        'fields': fields,
        'field_selected': field,
    }

    return render(req, 'item_list.html', context)

@login_required(login_url='/login')
def item_create_view(req):
    form = ItemForm(req.POST or None)

    if form.is_valid():
        form.save()
        form = ItemForm()

    context = {
        'form': form,
    }

    return render(req, 'item_create.html', context)

@login_required(login_url='/login')
def item_detail_view(req, id):
    item = get_object_or_404(Item, id=id)

    context = {
        'item': item
    }

    return render(req, 'item_detail.html', context)

@login_required(login_url='/login')
def item_update_view(req, id):
    item = get_object_or_404(Item, id=id)
    form = ItemForm(req.POST or None, instance=item)

    if req.method == 'POST':
        form.save()
        return redirect('item_list')

    context = {
        'form': form
    }

    return render(req, 'item_update.html', context)

@login_required(login_url='/login')
def item_delete_view(req, id):
    item = get_object_or_404(Item, id=id)

    if req.method == 'POST':
        item.delete()
        return redirect('item_list')

    context = {
        'item': item
    }

    return render(req, 'item_delete.html', context)


def register_account(req):
    if req.user.is_authenticated:
        return redirect('item_list')

    form = CreateUserForm()

    if req.method == 'POST':
        form = CreateUserForm(req.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('login')

    context = {
        'form': form,
    }

    return render(req, 'registration/register.html', context)


def login_account(req):
    if req.user.is_authenticated:
        return redirect('item_list')

    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(req, user)
            return redirect('item_list')

    context = {}
    return render(req, 'registration/login.html', context)


def logout_account(req):
    logout(req)
    return redirect('login')
