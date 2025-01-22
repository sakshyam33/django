from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect
from .models import ChaiVarity,Cart
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from .forms import store,Checkout,FeedbackForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def thanks(request):
    return render(request,'thanks.html')
def all(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'sakshyam/all_item.html', {'chais': chais})

# @login_required(login_url='login')  # Ensure the user is logged in before accessing this view
# def buy_chai(request, chai_id):
#     # Retrieve the chai by its ID
#     chai = get_object_or_404(ChaiVarity, id=chai_id)

#     if chai.amount > 0:
#         # Reduce the chai stock by 1
#         chai.reduce_amount(quantity=1)

#         # Add the item to the user's cart
#         cart_item, created = Cart.objects.get_or_create(user=request.user, chai=chai)
#         if not created:
#             # If the item already exists in the cart, increase the quantity
#             cart_item.quantity += 1
#             cart_item.save()

#         return redirect('menu')  # Redirect to the menu page after purchase
#     else:
#         # If out of stock, show an appropriate message or redirect to an error page
#         return HttpResponse("Sorry, this chai is out of stock!")
def contact_view(request):
    if request.method == 'POST':
        form = store(request.POST)
        if form.is_valid():
            form.save()  # Saves the form data directly to the database
            return render(request, 'success.html', {'name': form.cleaned_data['name']})
    else:
        form = store()

    return render(request, 'contact.html', {'form': form})



def view_description(request, chai_id):
    # Fetch the chai item by its primary key
    chai = get_object_or_404(ChaiVarity, id=chai_id)
    return render(request, 'sakshyam/description.html', {'chai': chai})

@login_required(login_url='login')  # Ensure the user is logged in

def add_to_cart(request, chai_id):

    """

    Add an item to the cart.


    Args:

        request: HTTP request object.

        chai_id: ID of the chai item to be added to the cart.

    """

    # Check if the user is authenticated

    if not request.user.is_authenticated:

        return redirect('login')  # Redirect to login if not authenticated


    # Retrieve the chai by its ID

    chai = get_object_or_404(ChaiVarity, id=chai_id)


    if chai.amount <= 0:

        # If the chai is out of stock

        return HttpResponse("Sorry, this chai is out of stock!")


    # Add the chai to the user's cart

    cart_item, created = Cart.objects.get_or_create(user=request.user, chai=chai)

    if not created:

        # If the item already exists in the cart, increase the quantity

        cart_item.quantity += 1

        cart_item.save()


    # Redirect to the cart view

    return redirect('view_cart')  # Replace 'view_cart' with the name of your cart view URL



# def add_cart(request,chai_id):
#     if not request.user.is_authenticated:
#         return redirect('login')
#     chai=get_object_or_404(ChaiVarity,id=chai_id)
#     cart_item,created=Cart.objects.get_or_create(user=request.user,chai=chai)
#     if not created:
#         cart_item.quantity+=1
#         cart_item.save()
#     return redirect('viewcart') #view cart has not been created

@csrf_exempt
def update_cart(request, chai_id):
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'message': 'You must be logged in to update the cart.'})

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            change = data.get('change', 0)
            
            chai = get_object_or_404(ChaiVarity, id=chai_id)
            cart_item = Cart.objects.filter(user=request.user, chai=chai).first()
            
            if not cart_item:
                return JsonResponse({'success': False, 'message': 'Item not found in the cart!'})

            if change > 0:  # Increase quantity
                if chai.amount <= cart_item.quantity:
                    return JsonResponse({'success': False, 'message': 'No available stock.'})
                cart_item.quantity += change
                chai.amount -= change
            elif change < 0:  # Decrease quantity
                if cart_item.quantity + change <= 0:
                    cart_item.delete()
                else:
                    cart_item.quantity += change
                chai.amount -= change
            
            cart_item.save()
            chai.save()

            return JsonResponse({'success': True, 'message': 'Cart updated successfully.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

def view_cart(request):
    if not request.user.is_authenticated:
        return redirect('login')

    # Fetch cart items for the logged-in user
    cart_items = Cart.objects.filter(user=request.user)

    # Prepare data for the template
    cart_data = [
        {
            'title': item.chai.name,  # Assuming 'product' has a 'name' field
            'price': item.chai.price,  # Assuming 'product' has a 'price' field
            'quantity': item.quantity,
            'image': item.chai.image.url if item.chai.image else '',  # Assuming product image exists
        }
        for item in cart_items
    ]

    return render(request, 'sakshyam/cart.html', {'cart_data': cart_data})
def checkout(request):
    if request.method=='POST':
        form=Checkout(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form=Checkout()
    return render(request,'sakshyam/checkout.html',{'form':form})
