from django.shortcuts import render
from .models import Product
from tradexa.common import post_and_product_list
from datetime import datetime
# Create your views here.


def add_list_product(request):
    if not request.user.is_authenticated:
            return redirect('user_dashboard:login')
    
    if request.method == 'POST':
        name = request.POST.get('name')
        weight = request.POST.get('weight')
        price = request.POST.get('price')
        
        if name and weight and price:
            Product.objects.create(
                name = name,
                weight = float(weight),
                price = float(price)
            )
            data = post_and_product_list(request)
            return render(request, 'index.html', data)
        
        data = post_and_product_list(request)
        data['error'] = "All field are required"
        return render(request, 'index.html', data)

    else:
        data = post_and_product_list(request)
        return render(request, 'index.html', data)


def update_product(request):
    if not request.user.is_authenticated:
            return redirect('user_dashboard:login')

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        name = request.POST.get('name')
        weight = request.POST.get('weight')
        price = request.POST.get('price')
        
        try:
            if product_id and name and weight and price:
                product = Product.objects.get(id=product_id)
                product.name = name
                product.weight = weight
                product.price = price
                product.updated_at = datetime.now()
                
                product.save()

                data = post_and_product_list(request)
                return render(request, 'index.html', data)
            
            data = post_and_product_list(request)
            data['update_error'] = "All field are required"
            return render(request, 'index.html', data)

        except Exception as e:
            data = post_and_product_list(request)
            data['update_error'] = str(e)
            return render(request, 'index.html', data)

    data = post_and_product_list(request)
    return render(request, 'index.html', data)
    
    
