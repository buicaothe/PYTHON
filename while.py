
'''
max = 10
sum, i = 0, 0
while i < max:
    print(i, end = '+' if i<(max-1) else '=')
    sum = sum+i
    i=i+1
else:
    print(sum)
'''
'''
n = float(input('Enter a positive number: '))
while n < 0:
    n = float(input('It is a nagative number! Enter a positive number: '))
else: print(f'Yes, {n} is Positive number!!')
'''
'''
s = 'buicaothe'
# range(bắt đầu, kết thúc, bước nhảy)
for index in range(0, len(s), 2):
    print(s[index], end="  ")
print()
for index in range(1, len(s), 2):
    print('  ',s[index], end='')
'''
'''
word = 'buicaothe'
index = 0
while index < len(word): 
    print(word[index])
    index +=1

for i in word:
    print(i)
'''
'''
a = float(input('Enter the amount of $ to share between 2 to 5 people: '))
for i in range(2,6):
    amount = a/i
    print(f'{i} people: ${amount:.2f} each!!!')
'''
'''
print("in ma trận vuông A:")
max = int(input('Nhập số hàng x cột: '))
for i in range (1,max+1):
    for j in range(1,max+1):
        print(f'A{i}{j}', end = '          ')
    print()
'''
'''
import random
while True:
    r = random.randint(0,100)
    print(r, end=': ')
    while True:
        print(r%3, end = ' ')
        if r%3 == 0:
            print('Stop')
            break
        r=r-1
    if r%5 == 0:
        print(f'{r} - the end')
        break
'''
'''
import random
random.choice((1,3,4))
random.choice([1,3,4])
random.random()
'''

# 1. Nhập và kiểm tra xác suất đầu vào
p_input = input("Nhập xác suất khách vào cửa hàng (0.0 - 1.0): ")
p = float(p_input)

if p < 0.0 or p > 1.0:
    print("Xác suất không hợp lệ. Chương trình kết thúc.")
    exit()  # Thoát chương trình ngay lập tức

# 2. Khởi tạo các biến theo dõi
total_customers = 0
longest_queue = 0
idle_time = 0
queue_length = 0        # Số lượng khách trong hàng đợi
service_time_left = 0   # Thời gian còn lại để phục vụ khách hiện tại

# 3. Chạy vòng lặp mô phỏng 100 lần (100 phút)
for round_num in range(1, 101):

    # --- KIỂM TRA KHÁCH VÀO ---
    # Lấy một số ngẫu nhiên từ 0.0 đến 1.0
    r = random.random()
    if r <= p:
        queue_length = queue_length + 1
        total_customers = total_customers + 1

    # Cập nhật hàng đợi dài nhất nếu cần
    if queue_length > longest_queue:
        longest_queue = queue_length

    # --- XỬ LÝ PHỤC VỤ TẠI QUẦY ---
    if service_time_left == 0:
        # Nếu thu ngân đang rảnh
        if queue_length > 0:
            # Lấy 1 người từ hàng đợi ra để bắt đầu phục vụ
            queue_length = queue_length - 1

            # Chọn ngẫu nhiên loại hàng: A(1p), B(3p), C(4p)
            loai_hang = random.randint(1, 3)
            if loai_hang == 1:
                service_time_left = 1
            elif loai_hang == 2:
                service_time_left = 3
            else:
                service_time_left = 4

            # Vì việc phục vụ bắt đầu ngay phút này, ta trừ đi 1 phút luôn
            service_time_left = service_time_left - 1
        else:
            # Hàng rỗng, cộng thêm thời gian rảnh
            idle_time = idle_time + 1
    else:
        # Nếu đang bận phục vụ, giảm thời gian cần làm xuống
        service_time_left = service_time_left - 1

# this is the new change

# 4. Xuất báo cáo kết quả
print("---------------------------------------")
print("KẾT QUẢ SAU 100 PHÚT MÔ PHỎNG:")
print("Tổng số khách đã ghé thăm:", total_customers)
print("Độ dài hàng đợi lớn nhất:", longest_queue)
print("Tổng thời gian thu ngân rảnh:", idle_time, "phút")
