from .cart import Cart

# Context Processor

def cart(request):
    return {'cart': Cart(request)}
