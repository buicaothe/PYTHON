'''
# 1. Khởi tạo Tuple ban đầu
thuc_don = ("Cơm tấm", "Phở", "Bánh mì")

print('Thực đơn ban đầu: ',thuc_don)

# 2. Chuyển Tuple thành List
thuc_don_list = list(thuc_don)

# 3. Bây giờ ta có thể sửa đổi thoải mái trên List này
thuc_don_list[2] = "Bún chả"

# 4. Chuyển List đã sửa ngược lại thành Tuple
thuc_don = tuple(thuc_don_list)

print('Thực đơn sau khi chỉnh sửa: ',thuc_don)
# Kết quả: ('Cơm tấm', 'Bún chả', 'Bánh mì')

my_first_tuple = ()
print('print: ',my_first_tuple)
x = (1)
y = (1,)
print(type(x))
print(type(y))
print(type(my_first_tuple))

s = 'buicaothebuicasothee'
dic = dict.fromkeys(s,1000)
print(dic)

dic = dict(zip(list(s), [i+1 for i in range(100)]))
print(dic)
dic = dict(zip([i+1 for i in range(100)], list(s)))
print(dic)


l = [1,10,1,2,20,3,30,4,40,5,50,6,60]

c= l[0::2]
d = l[-10:-1:2]
t = tuple(l)
e = t[-(len(t)):-1]
print(l)
print(e)

#n = [i+1 for i in range(10)]
t = tuple(i**i for i in range(10))
#print(n)
print(t)

l = []
for i in range(10): 
    l.append(i)

l.append(1000)
l.append(2000)
l.append(3000)
print(l)


fruits = ['apple', 'banana','kiwi','cherry']
for item in fruits:
    print(item)

for i in range(len(fruits)):
    print(f'{i+1}: {fruits[i]}')

s = 'buicaothe'
dic = list(s)

print(dic)
print("Dùng for: ")
for i in range(len(s)):
    print(f'{i+1}: {dic[i]}: làm phép lũy thừa {i**i}')

n = [num*3 for num in range(10)]
print(n)
others = [num for num in n if num%9 ==0]
print(others)

tictactoe_board = []
for i in range(3):
    row = ['_' for j in range(3)]
    tictactoe_board.append(row)
    print()
print(tictactoe_board)

for row in tictactoe_board:
    print(row)

tictactoe_board = [['_' for i in range(3)] for j in range(3)]
for i in range(3):
    print(tictactoe_board[i])

    
tictactoe_board = []
for i in range(3):
    row = [j for j in range(3)]
    tictactoe_board.append(row)
print('In dạng am trận: ')
for i in range(3):
    print(tictactoe_board[i])

print('In dạng từng hàng: ')
for j in range(3):
    print(f'Hàng {j+1}: ','\n', tictactoe_board[j])

print('In từng phần tử Ma trận: ')
for i in range(3):
    for j in range(3):
        print(f'A{i+1}{j+1} = ', tictactoe_board[i][j])

print()
print('Gán từ phần tử vào biến Aij: ')

for i in range(3):
    for j in range(3):
        tictactoe_board[i][j] = input(f'Nhập phần tử A{i+1}{j+1} = ')
print('In dạng ma trận: ')
for i in range(3):
    print(tictactoe_board[i])

dic = {x: f"{x}^2={x**2}" for x in (2, 4, 6)}
print(dic)

l = [1, 10, 1, 2, 20, 3, 30, 4, 40, 5, 50, 6, 60]
s = set(l)
print(s)
# item = s.pop
# print(item)
s.update(set('Helloh'))
print(s)

dic = {x: f"{x}+1 = {x+1}" for x in range(5)}
print(dic)
a = dic[1]
print(a)
dic[2] = dic[2]+['bui', 'cao']
print(dic)

d = {1: ['A', 'a'], 2: ['B', 'b'], 3: ['C', 'c'], 4: ['D', 'd']}
print(d)
print(d[1])
print(d[2])
print(d[3])
print(d[4])
d[2] = ['Ba', 'Be', 'BUI', 'CAO', 'THE']  # OVERWIRITE; REPLACE
d[6] = ['E', 'e']  # add new
print(d)
d.clear()
print('Dictionary content after CLEAR: ', d)

# 1. Khởi tạo một set chứa các loại quả
fruits = {"Apple", "Banana", "Cherry", "Mango"}
print(fruits)
# 2. Sử dụng phương thức pop() để lấy ra một phần tử: NGẪU NHIÊN!
removed_item = fruits.pop() # GÁN phần tử bị mất này cho 1 biến khác

# 3. In phần tử đã bị lấy ra
print("Phần tử bị loại bỏ:", removed_item)

# 4. In tập hợp còn lại sau khi pop
print("Tập hợp còn lại:", fruits)


dic = {'a': 'bui', 'b': 'cao', 'c': 'the', 'd': 'không có gì'}  # key : value
print(dic)
# for key in dic:
#   print(f'Key number = {key} and Value = {dic[key]}')  # keyname

for key in dic:
    print(dic[key])

for item in dic.values():
    print(item)

print('key-value-pairs: ')
for key, value in dic.items():
    print(key, value)


# Khởi tạo dictionary
phone_book = {
    "An": "0912345",
    "Bình": "0988888",
    "Chi": "0901111"
}

# Duyệt và in
for name, phone in phone_book.items():
    print(f"Tên: {name} - SĐT: {phone}")

a = set()
a.add('A')
a.add('B')
a.add('C')
while a:
    print(f'Nếu lấy đi: {a.pop()}')
    if a == set():
        print("---> Hết hàng!")

    else:
        print("Hàng còn lại: ", len(a), ' món là: ', a)
'''
