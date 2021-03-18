from orders.VO.coffee import Coffee
from orders.customers import Customer
from orders.menus import Menu
from orders.sellers import Seller

if __name__ == '__main__':
    # initialize menu
    americano = Coffee(name="Americano", price=3000)
    espresso = Coffee(name="Espresso", price=2000)
    latte = Coffee(name="Latte", price=4000)
    menu = Menu(products={
        americano.name: americano,
        espresso.name: espresso,
        latte.name: latte
    })

    # initialize customer & seller
    customer = Customer(name="John", menu=menu)
    seller = Seller(name="Ami")

    # create order
    order = customer.create_order(coffee_name=latte.name, amount=2)
    receipt = seller.create_receipt(order=order)

    # print receipt
    from pprint import pprint
    pprint(receipt)

