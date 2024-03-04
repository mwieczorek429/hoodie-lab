from django.conf import settings
from products.models import Hoodie

class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID) 
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'size': product.size,
                                     'price': str(product.price)}
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Hoodie.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            product_id = str(product.id)
            if product_id in cart:
                cart[product_id].setdefault('product', product)
        for item in cart.values():
            yield item