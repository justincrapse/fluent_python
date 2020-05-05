from itertools import combinations, combinations_with_replacement, permutations, product

print('combinations', list(combinations('ABC', 2)))
print('comb with replacement', list(combinations_with_replacement('ABC', 2)))
print('permutations', list(permutations('ABC', 2)))
print('product', list(product('ABC', repeat=2)))
