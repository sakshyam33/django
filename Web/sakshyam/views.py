from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect
from .models import ChaiVarity
from django.shortcuts import render, redirect, get_object_or_404

def all(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'sakshyam/all_item.html', {'chais': chais})

@login_required(login_url='login')  # Ensure the user is logged in before buying
def buy_chai(request, chai_id):
    # Retrieve the chai by its id
    chai = get_object_or_404(ChaiVarity, id=chai_id)

    if chai.amount > 0:
        # Reduce the chai stock by 1 (or more if you want to allow quantity selection)
        chai.reduce_amount(quantity=1)
        return redirect('menu')  # Redirect to the menu page after purchase
    else:
        # If out of stock, show an appropriate message or redirect to an error page
        return HttpResponse("Sorry, this chai is out of stock!")

