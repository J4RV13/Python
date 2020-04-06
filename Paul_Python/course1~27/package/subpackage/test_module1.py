def sum_bm1(a, b):
  return a + b + 1

def multiply_bm2(a, b):
  return a * b * 2

from . import sum_module
print(sum_module.sum_bm(2, 3))

from ..subpackage import sum_module
sum_module.sum_bm(2, 3)
sum_module.multiply_bm(2, 3)

import sum_module
sum_module.sum_bm(3, 5)
