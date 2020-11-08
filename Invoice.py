class Invoice:

    def __init__(self):
        self.items = {}

    def addProduct(self, qnt, price, discount):
        self.items['qnt'] = qnt
        self.items['unit_price'] = price
        self.items['discount'] = discount
        return self.items

    def totalImpurePrice(self, products):
        total_impure_price = 0
        for k, v in products.items():
            total_impure_price += float(v['unit_price']) * int(v['qnt'])
        total_impure_price = round(total_impure_price, 2)
        return total_impure_price

    def totalDiscount(self, products):
        total_discount = 0
        for k, v in products.items():
            total_discount += (int(v['qnt']) * float(v['unit_price'])) * float(v['discount']) / 100
        total_discount = round(total_discount, 2)
        self.total_discount = total_discount
        return total_discount

    # Get Shipping cost (5% of order)
    def totalShipping(self, products):
        total_cost = 0

        for k, v in products.items():
            total_cost += (int(v['qnt']) * float(v['unit_price']))

        total_shipping = round(total_cost * 0.05, 2)
        self.total_shipping = total_shipping
        return total_shipping

    # Get Taxes Cost (4.8% taxes in NC)
    def totalTaxes(self, products):
        total_cost = 0

        for k, v in products.items():
            total_cost += (int(v['qnt']) * float(v['unit_price']))

        total_discount = self.totalDiscount(products)
        total_cost = (total_cost - total_discount)
        total_taxes = round(total_cost * 0.048, 2)
        self.total_taxes = total_taxes
        return total_taxes


    def totalPurePrice(self, products):
        total_pure_price = self.totalImpurePrice(products) - self.totalDiscount(products) + self.totalTaxes(products) + self.totalShipping(products)
        return total_pure_price

    def inputAnswer(self, input_value):
        while True:
            userInput = input(input_value)
            if userInput in ['y', 'n']:
                return userInput
            print("y or n! Try again.")

    def inputNumber(self, input_value):
        while True:
            try:
                userInput = float(input(input_value))
            except ValueError:
                print("Not a number! Try again.")
                continue
            else:
                return userInput