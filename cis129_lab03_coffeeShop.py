def Take_order():
    coffee_count = input("How many Coffees would you like?")
    muffin_count = input("How many Muffins would you like?")
    bagel_count = input("How many Bagels Would you like?")
    scone_count = input("How many Scones would you like")

    try:
        coffee_count = int(coffee_count)
        muffin_count = int(muffin_count)
        bagel_count = int(bagel_count)
        scone_count = int(scone_count)

    except ValueError:
            print('How many?')
        

    return coffee_count, muffin_count, bagel_count, scone_count

def cash_register(coffee_count, muffin_count, bagel_count, scone_count):

    coffee_cost = (coffee_count * 5.00)
    muffin_cost = (muffin_count * 4.00)
    bagel_cost = (bagel_count * 7.00)
    scone_cost = (scone_count * 6.00)
    tax_total = (coffee_cost * 0.06) + (muffin_cost * 0.06) + (bagel_cost * 0.06) + (scone_cost * 0.06)
    total_cost = (coffee_cost + muffin_cost + bagel_cost + scone_cost + tax_total)

    return coffee_cost, muffin_cost, bagel_cost, scone_cost, tax_total, total_cost

def receipt_printer(coffee_count, muffin_count, bagel_count, scone_count, coffee_cost, muffin_cost, bagel_cost, scone_cost, tax_total, total_cost):

    print(f"""
    *****************************************
    StarBros Coffee & Muffin
    Number of coffees bought?
    {coffee_count}
    Number of muffins bought?
    {muffin_count}
    Number of bagels bought?
    {bagel_count}
    Number of scones bought?
    {scone_count}
    *****************************************


    *****************************************
    StarBros Coffee & Muffin Receipt
    {coffee_count} Coffee at $5 each: ${coffee_cost:.2f}
    {muffin_count} Muffins at $4 each: ${muffin_cost:.2f}
    {bagel_count} Bagels at $7 each: ${bagel_cost:.2f}
    {scone_count} Scones at $6 each: ${scone_cost:.2f}
    6% tax: ${tax_total:.2f}
    --------
    total:${total_cost:.2f}
    *****************************************
    Thank You So Much!!! Please Come Again!!!

    """)

    
    
        

if __name__== '__main__':
    coffee_count, muffin_count, bagel_count, scone_count = Take_order()
    coffee_cost, muffin_cost, bagel_cost, scone_cost, tax_total, total_cost = cash_register(coffee_count, muffin_count, bagel_count, scone_count)
    receipt_printer(coffee_count, muffin_count, bagel_count, scone_count, coffee_cost, muffin_cost, bagel_cost, scone_cost, tax_total, total_cost)
