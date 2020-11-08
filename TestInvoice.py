import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

def test_CanCalculateTotalImpurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 76.46

# The shipping is 5% of the total impure cost (pureTotal * 0.05)
def test_CanCalculateTotalShipping(invoice, products):
    invoice.totalShipping(products)
    assert invoice.totalShipping(products) == 3.75

# The taxes cost which is 4.8 of the total pure cost (impureTotal - discount) * 0.048
def test_CanCaluculateTotalTaxes(invoice, products):
    invoice.totalTaxes(products)
    assert invoice.totalTaxes(products) == 3.33


