from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from .form import Userform,Sellerform,Productform
from .models import Usermode,Seller_Model,Customer1
from .models import Product1,Cart1
from home import calc
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def product_show(r):
    form = Product1.objects.all()
    return render(r,'home/product_show.html',{'form':form})


# @login_required()
# def User_view(r,id):
#     form=Userform()
#     if r.method=="POST":
#         form=Userform(r.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/payment')
#     return render(r,'home/userform.html',{'form':form})

def Seller_view(r):
    form=Sellerform()
    if r.method=="POST":
        form=Sellerform(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home')
    return render(r,'home/Sellerform.html',{'form':form})



def Product_view(r):
    form=Productform()
    if r.method=="POST":
        form=Productform(r.POST,r.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productshow')
    return render(r,'home/Productform.html',{'form':form,})


def Selection_View(r):
    return render(r,'home/selection.html')

def Home_view(r):
    totalitem=0
    U=Customer1.objects.all()
    form = Product1.objects.all()
    if r.session.has_key('phone'):
        phone=r.session['phone']
        totalitem=len(Cart1.objects.filter(phone=phone))
        customer=Customer1.objects.filter(phone=phone)
        for c in customer:
            name=c.name
            data={
                'name':name,
                'totalitem':totalitem,
                'form': form
            }

            data['name']=name
            data['totalitem']=totalitem
            return render(r, 'home/cards.html', data)
    else:
        return redirect('/login')
def login(r):
    return render(r,'registration/login.html')

def view(r):
    form = Product1.objects.all()
    return render(r, 'home/product_view.html', {'form': form})


def update(r,id):
    abc= Product1.objects.get(id=id)
    if r.method=="POST":
        form=Productform(r.POST,instance=abc)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productshow')
    return render(r,'home/update.html',{'abc':abc})




def delete(r,id):
    abc = Product1.objects.get(id=id)
    abc.delete()
    return HttpResponseRedirect('/productshow')




def detail(r,id):
    totalitem=0
    form = Product1.objects.get(id=id)
    Item_already_in_cart=False
    if r.session.has_key('phone'):
        phone=r.session['phone']
        totalitem=len(Cart1.objects.filter(phone=phone))
        Item_already_in_cart=Cart1.objects.filter(Q(Product_brand=form.id) & Q(phone=phone)).exists()
        customer=Customer1.objects.filter(phone=phone)
        for c in customer:
            name=c.name
        data={
            'form':form,
            'Item_already_in_cart':Item_already_in_cart,
            'name':name,
            'totalitem':totalitem

        }
        return render(r,'product_detail.html',data)    #{'form':form}




# def payment(r):
#
#     return render(r,'home/payment_method.html')


def User_view(r,id):
    obj=Product1.objects.get(id=id)
    form=Userform()
    global det
    det={'id':obj.id}
    if r.method=="POST":

        det['qunt']=r.POST['quantity1']
        det['cost']=r.POST['product_cost']

        print(qunt,cost,obj.id)
        # form=Userform(r.POST)
        # if form.is_valid():
        #     form.save()
        # return HttpResponseRedirect(f"/payment/{obj.id}/")

    return render(r,'home/userform.html',{'form':obj,'ob':form})




def payment(r,id):
    obj=Product1.objects.get(id=id)
    Total_cost=calc.total(det['qunt'],det['cost'])
    return render(r,'home/payment_method.html',{'obj':obj,'total':Total_cost})




def SignUp1(r):
    obj=Customer1.objects.all()
    if r.method=='GET':
        return render(r,'home/Signup1.html')
    else:
        postdata=r.POST
        name=postdata.get('name')
        phone=postdata.get('phone')

        error_message=None
        value={
            'phone':phone,
            'name':name
        }

        customer=Customer1(name=name,
                          phone=phone)
        if(not name):
            error_message = "name is required"
        elif not phone:
            error_message = "phone No. is required"
        elif len(phone)<10 or len(phone)>10:
            error_message = "phone No. must be 10 digit"
        elif customer.isExists():
            error_message = "Account already Exist"
            value={
            'phone':phone,
            'name':name
        }


        if not error_message:
            messages.success(r,'Congratulation !! Register Successfull')
            customer.register()
            return redirect('/')
        else:
            data={
                'error':error_message,
                'value':value

            }
            return render(r,'home/Signup1.html',data)



def login(r):
    if r.method=='GET':
        return render(r,'home/login.html')
    else:
        phone=r.POST.get('phone')

        error_message=None
        value={
            'phone':phone
        }


        customer=Customer1.objects.filter(phone=r.POST['phone'])
        if customer:
            r.session['phone']=phone
            return redirect('/')
        else:
            error_message= "mobile No is Invalid !!"

            data={
                'error':error_message,
                'value':value

            }


        return render(r,'home/login.html',data)


def logout(r):
    if r.session.has_key('phone'):
        del r.session['phone']
        return redirect('/login')


def Cartview(r):
    phone=r.session['phone']
    product_id=r.GET.get('prod_id')
    product_name=Product1.objects.get(id=product_id)
    product=Product1.objects.filter(id=product_id)
    for p in product:
        product_image=p.product_image
        product_cost= p.product_cost
        Cart1(phone=phone,Product_brand=product_name,product_image=product_image,product_cost=product_cost).save()
        return redirect(f"/detail/{product_id}")


def show_add_to_cart(r):
    form=Cart1.objects.all()
    return render(r,'home/show_cart.html',{'form':form})


def remove_cart(r,id):
    abc = Cart1.objects.get(id=id)
    abc.delete()
    return HttpResponseRedirect('/show_cart')