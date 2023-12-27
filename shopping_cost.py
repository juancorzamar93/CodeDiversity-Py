import csv


def shopping_cost(filename):
    
    # Compute the total of shopping details stored in a csv file
    # with id, account, purchased_quantity, item_name, item_quantity
    # item_unit, item_price, category

    account = None
    total = 0.0
    total_items = 0

    with open(filename) as f:
        rows = csv.reader(f)
        header = next(f)
        for i, row in enumerate(rows):
            row[2] = int(row[2])
            row[6] = float(row[6])
        
        if account is None:
            account = row[1]
        
        total_items += row[2]
        total += row[2] * row[6]

    return account, total, total_items
    
def add_number(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result

def func(**Kwargs):
    print(Kwargs)

def func2(*args,**kwargs):
    print(args)
    print(kwargs)