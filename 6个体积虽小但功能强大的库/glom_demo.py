from glom import glom, T, Iter

data = {
    'orders': [
        {
            'id': 101,
            'customer': {
                'name': 'Alice',
                'address': {'city': 'Beijing', 'district': 'Chaoyang'}
            },
            'items': [
                {'name': 'Burger', 'qty': 2},
                {'name': 'Coke', 'qty': 1}
            ],
            'status': 'completed'
        },
        {
            'id': 102,
            'customer': {
                'name': 'Bob',
                'address': {'city': 'Shanghai', 'district': 'Pudong'}
            },
            'items': [
                {'name': 'Pizza', 'qty': 1},
                {'name': 'Tea', 'qty': 2}
            ],
            'status': 'pending'
        }
    ]
}

spec = (
    'orders',
    [
        {
            'order_id': 'id',
            'customer_name': 'customer.name',
            'city': 'customer.address.city',
            'num_items': (T['items'], len),
            'status': 'status'
        }
    ]
)

result = glom(data, spec)
for item in result:
    print(item)