def Take_order():
    coffee_count = input("How many Coffees would you like?")
    muffin_count = input("How many Muffins would you like?")

    try:
        coffee_count = int(coffee_count)
        muffin_count = int(muffin_count)

    except ValueError:
            print('How many?')
        

    return coffee_count, muffin_count

def cash_register(coffee_count, muffin_count):

    coffee_cost = (coffee_count * 5.00)
    muffin_cost = (muffin_count * 4.00)
    tax_total = (coffee_cost * 0.06) +(muffin_cost * 0.06)
    total_cost = (coffee_cost + muffin_cost + tax_total)

    return coffee_cost, muffin_cost, tax_total, total_cost

def receipt_printer(coffee_count, muffin_count, coffee_cost, muffin_cost, tax_total, total_cost):

    print(f"""
    *****************************************
    StarBros Coffee & Muffin
    Number of coffees bought?
    {coffee_count}
    Number of muffins bought?
    {muffin_count}
    *****************************************


    *****************************************
    StarBros Coffee & Muffin Receipt
    {coffee_count} Coffee at $5 each: ${coffee_cost:.2f}
    {muffin_count} Muffins at $4 each: ${muffin_cost:.2f}
    6% tax: ${tax_total:.2f}
    --------
    total:${total_cost:.2f}
    *****************************************

    """)

    
    
        

if __name__== '__main__':
    coffee_count, muffin_count = Take_order()
    coffee_cost, muffin_cost, tax_total, total_cost = cash_register(coffee_count, muffin_count)
    receipt_printer(coffee_count, muffin_count, coffee_cost, muffin_cost, tax_total, total_cost)
