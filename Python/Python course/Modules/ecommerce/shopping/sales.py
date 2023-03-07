# from ..customer import customer
# from ecommerce.customer import customer
print("Sales initialized", __name__)

# absolute import
# relative import
# from ..customer import customer

# customer.contact_customer()


def calc_tax():
    print("Tax Calculated")


def calc_shipping():
    print("Shipping Calculated")


if __name__ == "__main__":
    print("Sales Started")
    calc_shipping()
    calc_tax()
