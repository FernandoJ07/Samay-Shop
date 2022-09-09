def totalCart(request):
    total = 0 
    if request.session.get('cart'):
        for key, value in request.session['cart'].items():
            total += value["precio"] * value['cantidad']
    return {"total": total}

