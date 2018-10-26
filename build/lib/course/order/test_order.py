from order.order import Order


def test_create_order():
    o = Order()
    assert hasattr(o, "created_at")
    assert o._created_at == o.created_at
    assert hasattr(o, "id")
    assert len(o.id) == 20


def test_compare_orders():
    o1 = Order()
    o2 = Order()
    assert o1 > o2