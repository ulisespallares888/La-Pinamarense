def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session["shoppingcart"].items():
            total = total + (float(value["precio"]) * value["cantidad"])
           
    return {'total_key': total}

