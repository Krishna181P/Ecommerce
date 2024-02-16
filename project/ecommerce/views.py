from django.shortcuts import render,redirect
from django.views import View
from ecommerce.forms import RegisterForm,LoginForm,CartForm,OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from ecommerce.models import Products,Category,Cart,OrderPlaced
from django.core.mail import send_mail,settings




# Create your views here.

class Home(View):
    def get(self,request,*args,**kwargs):
        data=Products.objects.all()
        return render(request,'index.html',{'products':data})
    
class RegisterView(View):
    def get(self,request,*args,**kwargs):
        form=RegisterForm()
        return render(request,'register.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,'Registration Successfully')
            return redirect('log_view')
        else:
            messages.error(request,'Invalid')
            return redirect('reg_view')

        
class UserLogin(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,'login.html',{'form':form})
    def post(self,request,*args,**kwargs):
        uname=request.POST['username']
        psw=request.POST['password']
        user=authenticate(username=uname,password=psw)
        if user:
            login(request,user)
            messages.success(request,'Loggin Successfully')
            return redirect('home_view')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('log_view')
# class Userhome(View):
#     def get(self,request,*args,**kwargs):
#         return render(request,'userhome.html')
class UserLogout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        messages.success(request,'Logout Successfully')
        return redirect('home_view')

class ProductDetailView(View):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get('id')
        product=Products.objects.get(id=pid)
        return render(request,'productdetails.html',{'product':product})
    

class AddtoCart(View):
    def get(self,request,*args,**kwargs):
        form=CartForm()
        pid=kwargs.get('id')
        product=Products.objects.get(id=pid)
        return render(request,'addtocart.html',{'form':form,'product':product})
    def post(self,request,*args,**kwargs):
        u=request.user
        pid=kwargs.get('id')
        q=request.POST.get('quantity')
        p=Products.objects.get(id=pid)
        Cart.objects.create(user=u,quantity=q,product=p)
        return redirect('home_view')
    
class CartUserList(View):
    def get(self,request,*args,**kwargs):
        data=Cart.objects.filter(user=request.user).exclude(status='order-placed')
        return render(request,'Cartlistview.html',{'carts':data})
    
class PlaceOrderView(View):
    def get(self,request,*args,**kwargs):
        form=OrderForm()
        return render(request,'placeorder.html',{'form':form})
    def post(self,request,*args,**kwargs):
        cart_id=kwargs.get('cart_id')
        cart=Cart.objects.get(id=cart_id)
        user=request.user
        address=request.POST['address']
        email=request.POST['email']
        OrderPlaced.objects.create(user=user,cart=cart,address=address,email=email)
        send_mail('confirmation','order-placrd Successfully',settings.EMAIL_HOST_USER,[email])
        cart.status='Order-placed'
        cart.save()
        return redirect('home_view')
class CartDelete(View):
    def get(self,request,*args,**kwargs):
        cart_id=kwargs.get('id')
        data=Cart.objects.get(id=cart_id)
        data.delete()
        return redirect('cart_list')



