from ecommerce.models import Cart
def cart_count_context(request):
    if request.user.is_authenticated:
        count=Cart.objects.filter(user_id=request.user).exclude(status='Order-placed').count()
        return {'count':count}
    else:
        return {'count':0}