items = [
    {
        'code':1,
        'name':'Frappoccino☕',
        'stock':6,
        'price':5
    },
    {
        'code':2,
        'name':'Hot Chocolate☕',
        'stock':6,
        'price':10
    },
    {
        'code':3,
        'name':'Latte☕',
        'stock':6,
        'price':2
    },{
        'code':4,
        'name':'Americano☕',
        'stock':6,
        'price':2
    },{
        'code':5,
        'name':'Oleato🍹',
        'stock':6,
        'price':2
    },{
        'code':6,
        'name':'Ice Tea🍹',
        'stock':6,
        'price':2
    },{
        'code':7,
        'name':'Iced Latte🍹',
        'stock':6,
        'price':2
    },{
        'code':8,
        'name':'Cold Chocolate Cream brew🍹',
        'stock':6,
        'price':2
    },{
        'code':9,
        'name':'Madeleines🍰',
        'stock':6,
        'price':2
    },{
        'code':10,
        'name':'Vanilla Biscotti🍰',
        'stock':6,
        'price':2
    },{
        'code':11,
        'name':'Shortbread Cookies🍰',
        'stock':6,
        'price':2
    },{
        'code':12,
        'name':'Rip van Wafels🍰',
        'stock':6,
        'price':2
    },
]

is_quit = False
item = ''

total= 0

while is_quit == False:
    print("================================================================================================")
    print("""█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   ▄▀█ █░░ █▀▀ ▀▄▀ ▄▀█ ▀ █▀   █░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   █▀█ █▄▄ ██▄ █░█ █▀█ ░ ▄█   ▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█

█▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀
█░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄""")
    print("================================================================================================")
    print("""𝓜 𝓮𝓷𝓾""")
    print("================================================================================================")
    for i in items:
        print(f"{i['name']:27s} - Stock: {i['stock']} - Price: {i['price']:.2f} - code: {i['code']}")
        print('-' * 25)
    

    a = int(input("Enter the code number of the item you want to get: "))
    for i in items:
        if a == i['code']:
            item = i
    if item == '':
        print('INVALID CODE')
    else:
        print(f"Great, {item['name']} will cost you {item['price']} dollars")

        price = int(input(f"Enter {item['price']} dollars to purchase, if you wish to puchase another item enter another code: "))
        if price == item['price']:
            print(f"Thank you for buying here is your {item['name']}")
        else:
            print(f"Please enter only {item['price']} dollars")
    a = input   ("To quit the machine enter q and to continue buying enter c to continue: ")
    if a == 'q':
        is_quit = True
    else:
        is_quit = False
    print('')
