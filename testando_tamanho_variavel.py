#!/usr/bin/env python3

# metaprogramação
# r - read
# w - write
# a

fp = open('novoarquivo.txt', 'w')

template = '{0} = 1\nprint({0})\n{1}'
print(template.format('x'*9, 'arg 2nd position'), file=fp)

fp.close()
