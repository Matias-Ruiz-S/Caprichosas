

def importe_total_carro(request):
    total=0
    if 'carro' in request.session:
        for key, value in request.session["carro"].items():
            total += int(value["acumulado"])
    return {'importe_total_carro':total}


def counter(request):
    cart_count = 0
    
    if 'carro' in request.session:
        for key, value in request.session["carro"].items():
            cart_count +=  int(value["cantidad"]) 

    
    return dict(cart_count=cart_count)
