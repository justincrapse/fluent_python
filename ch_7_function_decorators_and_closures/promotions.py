promos = []


def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


@promotion
def fidelity_promo(order):
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


@promotion
def bulk_item_promo(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .01
    return discount


@promotion
def large_order_promo(order):
    discount_items = {item.product for item in order.cart}
    if len(discount_items) >= 10:
        return order.total() * .07
    return 0


def best_promo(order):
    return max(promo(order) for promo in promos)
