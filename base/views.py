from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        cartproducts_count = CartModel.objects.filter(host=request.user).count()
    else:
        cartproducts_count = False
    print(request.method)#GET
    print(request.GET)#<QueryDict: {}> #<QueryDict: {'search': ['dell']}>
    #search operation
    no_match = False
    trending = False
    offer = False
    if 'search' in request.GET:
        q = request.GET['search']
        print(q)#dell
        all_products = Product.objects.filter(Q(pname__icontains=q) | Q(pdesc__icontains=q))
        print(len(all_products))#<QuerySet []>
        if len(all_products)==0:
            no_match = True
    elif 'cat' in request.GET:
        cat = request.GET['cat']
        all_products = Product.objects.filter(pcategory=cat)
    elif 'trending' in request.GET:
        all_products = Product.objects.filter(trending = True)
        trending = True
    elif 'offer' in request.GET:
        all_products = Product.objects.filter(offer = True)
        offer = True
    else:
        all_products = Product.objects.all()

    category = []
    a = Product.objects.all()
    for i in a:
        print(i.pcategory)
        if i.pcategory not in category:#parcticular category not present in the list collection
            category+=[i.pcategory]
    print(category)#['laptop', 'Phone', 'Sports', 'Clothes', 'Perfume', 'Skin care']

    return render(request,'home.html',{'all_products':all_products,'no_match':no_match,'category':category,'nav_bar':True,'cartproducts_count':cartproducts_count,'trending':trending,'offer':offer})

def cart(request):
    cartproducts_count = CartModel.objects.filter(host = request.user).count()
    print(cartproducts_count)
    cartproducts = CartModel.objects.filter(host=request.user)
    TA = 0
    for i in cartproducts:
        print(i.totalprice)
        TA+=i.totalprice
    print(TA)
    return render(request,'cart.html',{'cartproducts':cartproducts,'TA':TA,'cartproducts_count':cartproducts_count})

@login_required(login_url='login_')
def addtocart(request,id):
    product = Product.objects.get(id=id)
    try:
        cp = CartModel.objects.get(pname = product.pname,host=request.user)#object instance #Doesn't exists
        cp.quantity+=1
        cp.totalprice+=product.price
        cp.save()
        return redirect('cart')
    except:
        CartModel.objects.create(
            pname = product.pname,
            price = product.price,
            pcategory = product.pcategory,
            quantity = 1,
            totalprice = product.price,
            host = request.user
        )
        return redirect('cart')
    
def remove(request,id):
    product = CartModel.objects.get(id=id)
    product.delete()
    return redirect('cart')

def increment(request,id):
    product = CartModel.objects.get(id=id)
    product.quantity+=1
    product.totalprice+=product.price
    product.save()
    return redirect('cart')

def decrement(request,id):
    product = CartModel.objects.get(id=id)
    if product.quantity>1:
        product.quantity-=1
        product.totalprice-=product.price
        product.save()
    else:
        product.delete()
    return redirect('cart')


def support(request):
    cartproducts_count = CartModel.objects.filter(host=request.user).count() if request.user.is_authenticated else False
    return render(request, 'support.html', {'cartproducts_count': cartproducts_count})

def about(request):
    cartproducts_count = CartModel.objects.filter(host=request.user).count() if request.user.is_authenticated else False
    return render(request, 'about.html', {'cartproducts_count': cartproducts_count})