from order.order2 import Order


def test_compare_orders():
    o1 = Order()
    o2 = Order()
    assert o1 > o2
    assert not o1 < o2
    assert not o1 == o2


