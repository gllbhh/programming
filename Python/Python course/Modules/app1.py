# if module is stored in a subfolder we can prefix
# it with the folder name to call it

from ecommerce.shopping import sales

# or
# from ecommerce.shopping.sales import calc_shipping, calc_tax
# to import specific functions

import sys
print(sys.path)

sales.calc_tax()
sales.calc_shipping()
