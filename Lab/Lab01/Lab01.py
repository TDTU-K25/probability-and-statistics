import itertools

"""Exercise 1"""

digits = list(range(0, 10))
k = 4

num_code = list(itertools.permutations(digits, k))

for i in num_code[::-1]:  # Duyệt list từ cuối lên đầu
    if (i[0] == 0):
        num_code.remove(i)

code_length = len(num_code)

"""Exercise 2"""

A = list(range(1, 6))
k = 3
n = len(A)

num_3_digit = list(itertools.permutations(A, k))
num_length = len(num_3_digit)

# print("%i-permutations of %s: " %(k, A))
# for i in num_3_digit:
#   print(i)
# print("Size =", "%i!/(%i-%i)! = " %(n, n, k), num_length)

"""Exercise 3"""


def cross(A, B):
    return {a + b for a in A for b in B}


urn = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789')
k = 3

# (a) Find a list of all possible 3 balls and assign to variable U3. Assign number of set U3 to variable len_U3
# Không gian mẫu
U3 = list(itertools.combinations(urn, k))
len_U3 = len(U3)

# (b) Enumerate all possible cases of three balls of different colors
# for s in U3:
#   if s[0][0] != s[1][0] and s[1][0] != s[2][0] and s[0][0] != s[2][0]:
#     print(s)

# (c) Enumerate all possible cases of the first ball being white and the second ball red
# for s in U3:
#   if s[0][0] == 'W' and s[1][0] == 'R':
#     print(s)

"""Exercise 4"""
# Các cuốn sách đôi 1 khác nhau

# Gom 4 quyển sách Toán lại thành 1 bộ
# Số cách xếp 4 quyển sách toán trong bộ là 4!
permute_4_math = list(itertools.permutations(cross('M', '1234'), 4))

# Gom 3 quyển sách Lý lại thành 1 bộ
# Số cách xếp 3 quyển sách Lý trong bộ là 3!
permute_3_physics = list(itertools.permutations(cross('P', '123'), 3))

# Gom 2 quyển sách Hóa lại thành 1 bộ
# Số cách xếp 2 quyển sách Hóa trong bộ là 2!
permute_2_chemistry = list(itertools.permutations(cross('C', '12'), 2))

# Gom 1 quyển sách Ngôn Ngữ lại thành 1 bộ
# Số cách xếp 1 quyển sách Ngôn Ngữ trong bộ là 1!
permute_1_language = list(itertools.permutations(cross('L', '1'), 1))

# Số cách xếp 4 bộ Toán, Lý, Hóa, Ngôn Ngữ vào kệ sách là 4!

# Cách xếp thứ 1: bộ Toán, bộ Lý, bộ Hóa, bộ Anh = 4! * 3! * 2! * 1! = 288 cách
first_arrangement_4_set_book = list(itertools.product(
    permute_4_math, permute_3_physics, permute_2_chemistry, permute_1_language))

# Với mỗi cách xếp bộ Toán, bộ Lý, bộ Hóa, bộ Ngôn Ngữ vào kệ sách
# ta sẽ hoán vị các bộ sách trong cách sắp xếp đó

# Ví dụ: 1 trong 288 cách xếp bộ Toán, bộ Lý, bộ Hóa, bộ Ngôn Ngữ vào kệ sách là
# (('M2', 'M1', 'M4', 'M3'), ('P3', 'P1', 'P2'), ('C2', 'C1'), ('L1',))

# Ta có 24 cách sắp xếp các bộ sách trong cách này
# (('M2', 'M1', 'M4', 'M3'), ('P3', 'P1', 'P2'), ('C2', 'C1'), ('L1',)) Toán-Lý-Hóa-NgônNgữ
# (('M2', 'M1', 'M4', 'M3'), ('P3', 'P1', 'P2'), ('L1',), ('C2', 'C1')) Toán-Lý-NgônNgữ-Hóa
# (('M2', 'M1', 'M4', 'M3'), ('C2', 'C1'), ('P3', 'P1', 'P2'), ('L1',)) Toán-Hóa-Lý-NgônNgữ
# (('M2', 'M1', 'M4', 'M3'), ('C2', 'C1'), ('L1',), ('P3', 'P1', 'P2')) ...
# (('M2', 'M1', 'M4', 'M3'), ('L1',), ('P3', 'P1', 'P2'), ('C2', 'C1'))
# (('M2', 'M1', 'M4', 'M3'), ('L1',), ('C2', 'C1'), ('P3', 'P1', 'P2'))
# (('P3', 'P1', 'P2'), ('M2', 'M1', 'M4', 'M3'), ('C2', 'C1'), ('L1',))
# ...

permute_4_set_book = []
# Lặp qua các cách sắp xếp trong 288 cách xếp bộ Toán, bộ Lý, bộ Hóa, bộ Ngôn Ngữ vào kệ sách
for arrangement in first_arrangement_4_set_book:
    # Với mỗi cách sắp xếp, hoán vị các bộ sách trong cách sắp xếp đó
    permute_4_set_book.append(list(itertools.permutations(arrangement)))

# Format lại kết quả
res = []
for l in permute_4_set_book:
    for arrangement in l:
        res.append(arrangement)

# for arrangement in res:
#     print(arrangement)
# print(len(res))

"""Exercise 5"""
# Số cách chọn 3 nam: 6!/(3!(6-3)!) = 20
choose_3_men = list(itertools.combinations(cross('M', '123456'), 3))

# Số cách chọn 2 nữ: 9!/(2!(9-2)!) = 36
choose_2_women = list(itertools.combinations(cross('W', '123456789'), 2))

# Số cách chọn 5 người trong đó có 3 nam, 2 nữ = 20 * 36 = 720
committee_5 = list(itertools.product(choose_3_men, choose_2_women))

# for s in committee_5:
#     print(s)

"""Exercise 6"""
deck_card = cross('S', '1234567889JQK') | cross('C', '1234567889JQK') | cross(
    'D', '1234567889JQK') | cross('H', '1234567889JQK')
