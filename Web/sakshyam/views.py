from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect
from .models import ChaiVarity
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from .forms import store
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
def contact_view(request):
    if request.method == 'POST':
        form = store(request.POST)
        if form.is_valid():
            form.save()  # Saves the form data directly to the database
            return render(request, 'success.html', {'name': form.cleaned_data['name']})
    else:
        form = store()

    return render(request, 'contact.html', {'form': form})

