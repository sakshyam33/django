from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect
from .models import ChaiVarity,Cart
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from .forms import store
def all(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'sakshyam/all_item.html', {'chais': chais})

@login_required(login_url='login')  # Ensure the user is logged in before accessing this view
def buy_chai(request, chai_id):
    # Retrieve the chai by its ID
    chai = get_object_or_404(ChaiVarity, id=chai_id)

    if chai.amount > 0:
        # Reduce the chai stock by 1
        chai.reduce_amount(quantity=1)

        # Add the item to the user's cart
        cart_item, created = Cart.objects.get_or_create(user=request.user, chai=chai)
        if not created:
            # If the item already exists in the cart, increase the quantity
            cart_item.quantity += 1
            cart_item.save()

        return redirect('menu')  # Redirect to the menu page after purchase
    else:
        # If out of stock, show an appropriate message or redirect to an error page
        return HttpResponse("Sorry, this chai is out of stock!")
def contact_view(request):
    if request.method == 'POST':
        form = store(request.POST)
        if form.is_valid():
            form.save()  # Saves the form data directly to the database
            return render(request, 'success.html', {'name': form.cleaned_data['name']})
    else:
        return 

    return render(request, 'contact.html', {'form': form})

def view_description(request, chai_id):
    # Fetch the chai item by its primary key
    chai = get_object_or_404(ChaiVarity, id=chai_id)
    return render(request, 'sakshyam/description.html', {'chai': chai})

def add_cart(request,chai_id):
    if not request.user.is_authenticated:
        return redirect('login')
    chai=get_object_or_404(ChaiVarity,id=chai_id)
    cart_item,created=Cart.objects.get_or_create(user=request.user,chai=chai)
    if not created:
        cart_item.quantity+=1
        cart_item.save()
    return redirect('viewcart') #view cart has not been created
def view_cart(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'sakshyam/cart.html', {'cart_items': cart_items})
