from django.shortcuts import render , redirect
from .models import Product , Members ,Teamoffer ,LatestA ,LatestB,Order,Orderitem,Email,Contact,Leave_message
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        'prod' : Product.objects.all(),
        'Mem':Members.objects.all(),
        'MemC':Teamoffer.objects.all(),
        'aboutW':LatestA.objects.all(),
        'AboutX':LatestB.objects.all(),
    }


    if request.method=="POST":
        email = request.POST.get("email123")


        email_1=Email(
            Email = email
        )
        email_1.save()
    
    return render(request,"web/index.html",context)

def about(request):
    context={
    'Mem':Members.objects.all()
    }

    if request.method=="POST":
        email = request.POST.get("email123")


        email_1=Email(
            Email = email
        )
        email_1.save()
    return render(request,"web/detail/about.html",context)
def blog(request):

    if request.method=="POST":
        email = request.POST.get("email123")


        email_1=Email(
            Email = email
        )
        email_1.save()
    return render(request,"web/detail/blog.html")
def contact1(request):

    if request.method == 'POST':
        if request.POST.get("form_type") == 'formOne':
            NameC=request.POST.get("Name_C")
            EmailC=request.POST.get("Email_C")
            SubjectC=request.POST.get("Subject_C")
            MessageC=request.POST.get("Message_C")
       
            contact_1=Contact(
                Name=NameC,
                Email1=EmailC,
                Subject=SubjectC,
                Message=MessageC
            )
            contact_1.save()

            
        elif request.POST.get("form_type") == 'formTwo':
            email = request.POST.get("email123")

            email_1=Email(
                Email = email)
            email_1.save()
            






    return render(request,"web/detail/contact.html")
def detail(request):
    if request.method=="POST":
        if request.POST.get("form_type")=='formthree':
            Name=request.POST.get("Name_L")
            EmailL=request.POST.get("Email_L")
            Website=request.POST.get("Web_L")
            Comment=request.POST.get("Com_L")

            leave_1=Leave_message(
                Name=Name,
                Email1=EmailL,
                Website=Website,
                Comment=Comment

            )
            leave_1.save()

        elif request.POST.get("form_type")=='formTwo':
            email = request.POST.get("email123")

            email_1=Email (
                Email = email
                )
            email_1.save()






        


       
    return render(request,"web/detail/detail.html")
def price(request):
    if request.method=="POST":
        email = request.POST.get("email123")


        email_1=Email(
            Email = email
        )
        email_1.save()
    return render(request,"web/detail/price.html")
def product(request):
    context={
        'prod' : Product.objects.all(),
        }
    if request.method=="POST":
        email = request.POST.get("email123")


        email_1=Email(
            Email = email
        )
        email_1.save()
    return render(request,"web/detail/product.html",context)
def service(request):
    context={
        'MemC':Teamoffer.objects.all(),
        }

    if request.method=="POST":
        email = request.POST.get("email123")


        email_1=Email(
            Email = email
        )
        email_1.save()
    return render(request,"web/detail/service.html",context)
def team(request):
    context={
        'Mem':Members.objects.all()
        }
    
    if request.method=="POST":
        email = request.POST.get("email123")


        email_1=Email(
            Email = email
        )
        email_1.save()
    return render(request,"web/detail/team.html",context)
def testimonial(request):
    context={
        'MemC':Teamoffer.objects.all(),
        }
    
    if request.method=="POST":
        email = request.POST.get("email123")


        email_1=Email(
            Email = email
        )
        email_1.save()
    return render(request,"web/detail/testimonial.html",context)

def Login1(request):
    if request.method=="POST":
        username=request.POST.get('Username_1')
        password=request.POST.get('PasswordL')
        
        User=authenticate(request,username=username,password=password)
        if User is not None:
            login(request,User)
            return redirect('index')
        else:
            messages.warning(request,'Invalid detail')
            return redirect('login')

    return render(request,"web/account/login.html")
def register(request):
    if request.method=="POST":
        Username=request.POST.get('Username_1')
        First_Name=request.POST.get('First-name')
        Last_Name=request.POST.get("Last-name")
        Email=request.POST.get('Email')
        password=request.POST.get('Password')
        Confirm_password=request.POST.get('Confirm-password')

        if password==Confirm_password:
            customer=User.objects.create_user(Username,Email,password)
            customer.first_name=First_Name
            customer.last_name=Last_Name
            customer.save()
            return redirect('login')

    return render(request,"web/account/sign-up.html")

def logout1(request):
    logout(request)
    return render(request,"web/account/login.html")

# ---------------cart---------------

@login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")

@login_required(login_url="login")
def cart_detail(request):
    return render(request, 'web/cart/cart.html')


# -------cart end-----------



@login_required(login_url="login")
def checkout(request):
    return render(request, 'web/cart/checkout.html')


@login_required(login_url="login")
def placeorder(request):
    if request.method=="POST":
        uid=request.session.get('_auth_user_id')
        user=User.objects.get(id=uid)
        cart=request.session.get('cart')

        First_Name=request.POST.get('Fname')
        Last_Name=request.POST.get('Lname')
        Country=request.POST.get('Country')
        Address=request.POST.get('Address')
        City=request.POST.get('City')
        State=request.POST.get('State')
        Pincode=request.POST.get('Pin')
        Phone=request.POST.get('Phone')
        Email=request.POST.get('Email')

        order_1=Order(
            user=user,
            First_Name=First_Name,
            Last_Name=Last_Name,
            Country= Country,
            Address=Address,
            City= City,
            State= State,
            Pincode=Pincode,
            Phone=Phone,
            Email= Email


        )
        order_1.save()

        for i in cart:
            a=float(cart[i]['price'])
            b=int(cart[i]['quantity'])
            total=a*b

            order_2=Orderitem(
                Order=order_1,
                Product=cart[i]['name'],
                image=cart[i]['image'],
                price=cart[i]['price'],
                qunatity=cart[i]['quantity'],
                total=total
            )

            order_2.save()

    return render(request, 'web/cart/placeorder.html')


@login_required(login_url="login")
def confirm(request):
    return render(request, 'web/cart/confirm.html')


