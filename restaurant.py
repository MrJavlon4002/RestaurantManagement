class Restaurant():
    # Reservations data
    reservations = {
        "Michel Johnson": {
            'date' : '12.10.2024',
            'time' : '10:00',
            'cust_num' : 4,
            'dishes': [
                {'juice' : {
                    'price': 2,
                    'description': 'That is juice.',
                    'category': 'drink'
                    }
                },
                {
                    'cake': {
                        'price': 7,
                        'description': 'That is cake.',
                        'category': 'desert'
                    }
                },
            ]
        }
    }
    # Data of dishes
    dishes = {
        'soup' : {
            'price': 15,
            'description': 'That is soup.',
            'category': 'main',
        },
        'kebab' : {
            'price': 10,
            'description': 'That is kebab.',
            'category': 'main'
        },
        'juice' : {
            'price': 2,
            'description': 'That is juice.',
            'category': 'drink'
        },
        'cake': {
            'price': 7,
            'description': 'That is cake.',
            'category': 'desert'
        },
        'tea': {
            'price': 1,
            'description': 'That is tea.',
            'category': 'drink'
        }
    }

    # data of dates
    dates = {
        '12.10.2024': ['10:00']
    }
    
    # data of requests
    requests = []

    # data of stuff members
    staff_members = ['John Wick', 'Will Smith']

    #information of Restaurant
    restaurant_info = "The name of our restaurant is PDP restaurant. We have several services for food."
