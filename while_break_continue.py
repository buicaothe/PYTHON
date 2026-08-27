
'''
_____________CLOCK PROGRAMME_____________
'''
'''
import time
t = time.time()
t10 = t + 10
stop = time.ctime(t10)
print(f'Stop when {stop} is reached!')
while True:
    print(f'\r{(current := time.ctime(time.time()))}', end ='', flush = True)
    if current == stop:
        print()
        print(f'{stop} was reached')
        break
    time.sleep(1)
'''
'''
while True:
    ten = input("Nhập tên bạn (gõ 'thoat' để dừng): ")
    if ten == 'thoat':
        break  # Dừng vòng lặp ngay tại đây
    print(f"Chào {ten}!")
print('Tạm biệt!')
'''
'''
max = int(input('Enter max number: '))
a=int(input('Enter the break condition: '))
sum = 0
i = 0
while i < max:
    if i == a:
        print ('Kết quả dở dang STOP!')
        break
    print(i, end='+' if i < (max-1) else '')
    sum = sum+i
    i = i+1
print('=')
print(sum)
'''
'''
import random
numberofloop = 0
while True:
    numberofloop +=1
    r = random.randint(0,100)
    if r >=90:
        continue
    print(r)
    if r <= 10:
        break
print('Nuber of loops were ',numberofloop)
'''
'''
for i in range(2,11):
    print(i)

i = 1
while i < 10:
    i=i+1
    print(i)
'''
'''
# Double a number 3 times:
a = int(input('Enter a number to doube 3 times: '))
for i in range(3):
    a = a*2
    print(a)
'''
'''
cap = float(input('Enter the Capital $: '))
year = int(input('Enter the number of year: '))
rate = float(input('Enter the interest rate per year %: '))
for i in range(1,year+1):
    cap = (rate/100+1)*cap
    print(f'Year {i}: ${cap:.2f}')
'''
s, e = int(input('Nhập khoảng\nBắt đầu: ')), int(input('Kết thúc: '))

# Hoán đổi nếu s > e
if s > e:
    s, e = e, s

print(f'Tổng các số chẵn từ {s} đến {e} là: ', end='')

total_sum = 0
# Đảm bảo s bắt đầu là số chẵn
s_start = s if s % 2 == 0 else s + 1

for num in range(s_start, e + 1, 2):
    total_sum += num
else:
    # Khối else này sẽ chạy sau khi vòng lặp for kết thúc bình thường
    print(total_sum)
