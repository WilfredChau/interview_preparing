"""
深拷贝和浅拷贝的实现方式和区别
浅拷贝没有拷贝子对象，所以原始数据改变，子对象改变
深拷贝包含对象里的子对象的拷贝，所以原始对象改变不会造成深拷贝里的任何子元素改变
"""

import copy

a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象
b = a  # 赋值
c = copy.copy(a)  # c进行浅拷贝，拷贝对象a
d = copy.deepcopy(a)  # d进行深拷贝，拷贝对象a
a.append(5)  # 修改对象a
a[4].append('c')
print(a)
print(b)
print(c)
print(d)
