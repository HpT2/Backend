from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connection
from .models import Customer, Cart, Contain
from product.models import Product, Category
# Create your views here.


def homepage(request):
    try:
        username = request.session['username']
    except:
        username = None
    return render(request, 'service/homepage.html', {'username': username})



def shop_page(request):
    product_list = Product.objects.all()
    category_list = Category.objects.all()
    try:
        username = request.session['username']
    except:
        username = None
    return render(request, 'service/shop-grid.html', {'username': username, 'product_list': product_list,
                                                      'category_list': category_list, })


def cart_page(request):
    keys = []
    values = []
    if(request.method == 'POST'):
        for key,value in request.POST.items():
            if key == 'Update_cart':
                break
            keys.append(key)
            values.append(value)
    category_list = Category.objects.all()
    try:
        username = request.session['username']
        user = Customer.objects.get(username=username)
        cart = Cart.objects.get(customer_id=user.customer_id)
        if (len(keys) > 1):
            product_ids = []
            x = 1
            while x < len(keys):
                if(keys[x]=='Add_to_cart'):
                    x+=1
                    continue
                product_ids.append(int(keys[x].split('product_')[1]))
                x += 1
        if 'Add_to_cart' in request.POST:
            for i in range(len(product_ids)):
                query = 'exec service.add_to_cart @cart_id = {0}, @product_id={1}'.format(cart.cart_id,product_ids[i])
                try:
                    cursor = connection.cursor()
                    cursor.execute(query)
                    cursor.close()
                except Exception as e:
                    cursor.close()
                    pass
        if 'Update_cart' in request.POST:
            x = 0
            while x < len(product_ids):
                query = 'update service.contain\n' \
                        'set amount={0}\n' \
                        'where product_id={1} and cart_id={2}'.format(values[x+1], product_ids[x], cart.cart_id)
                cursor = connection.cursor()
                try:
                    cursor.execute(query)
                    cursor.close()
                except Exception as e:
                    cursor.close()
                    pass
                x += 1
        query = 'exec service.get_cart @cart_id ="{0}"'.format(cart.cart_id)
        cursor = connection.cursor()
        product_object_list = []
        contain_list = []
        total_list = []
        try:
            cursor.execute(query)
            product_list_id = cursor.fetchall()
            for id in product_list_id:
                id = str(id)
                id = id.split(",")[0]
                id = id.split("(")[1]
                product = Product.objects.get(product_id=id)
                contain = Contain.objects.get(product_id=id, cart_id=cart.cart_id)
                product_object_list.append(product)
                contain_list.append(contain)
                total_list.append(product.price * contain.amount)
            object_list = zip(product_object_list,contain_list,total_list)
            sum = 0
            for i in range(len(total_list)):
                sum += total_list[i]
            cursor.execute('update service.cart\n'
                           'set total_price={0}\n'
                           'where cart_id={1}'.format(sum,cart.cart_id))
            cursor.close
        except Exception as e:
            product_list = None
            cursor.close()
    except Exception as e:
        print(e)
        username = None
        return  render(request,'service/shoping-cart.html', {'username': username})
    return render(request, 'service/shoping-cart.html', {'username': username, 'category_list':category_list,
                                                         'object_list': object_list, 'cart':cart,
                                                         'sum':sum})



def register(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        Fname = request.POST['Fname']
        Lname = request.POST['Lname']
        Email = request.POST['Email']
        Phone = '09714799331'
        Address = 'sdsadasdad'
        query = 'exec service.register @Fname="{0}", @Lname="{1}", @username="{2}", @password="{3}", ' \
                '@Email="{4}", @Phone="{5}", @Address="{6}"'.format(Fname,Lname,username,password,Email,Phone,Address)
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            cursor.close()
            request.session['username'] = username
            return homepage(request)
        except Exception as e:
            print(e)
            cursor.close()
            return HttpResponse(e)


def profile(request):
    username = request.session['username']
    user = Customer.objects.get(username=username)
    if(request.method == 'POST'):
        address = request.POST['address']
        Fname = request.POST['Fname']
        Lname = request.POST['Lname']
        Email = request.POST['email']
        Birthdate = request.POST['Birthdate']
        query = 'exec service.update_info @username={0}, @address="{1}", @Fname={2}, @Lname={3}, ' \
               '@Email="{4}", @Birthdate="{5}"'.format(username,address,Fname,Lname,Email,Birthdate)
        cursor = connection.cursor()
        try:
            print(query)
            cursor.execute(query)
            cursor.close()
            username = request.session['username']
        except:
            error = 'cannot save'
            return render(request,'service/profile.html', {'user':user,'error':error})
    return render(request,'service/profile.html', {'user':user})


def logout(request):
    del request.session['username']
    return homepage(request)