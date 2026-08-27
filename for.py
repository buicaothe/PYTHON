# def check_item(target, items):
#     print(f"Đang tìm '{target}'...")
#     for item in items:
#         if item == target:
#             print("=> Đã tìm thấy!")
#             break
#     else:
#         print("=> Không tìm thấy món này.")
#     print("-" * 20)


# my_list = ["laptop", "mouse", "keyboard"]

# check_item("mouse", my_list)     # Trường hợp gặp break
# check_item("headphone", my_list)  # Trường hợp chạy hết vòng lặp (vào else)
# check_item("ihm=en", my_list)
# check_item("laptop", my_list)

a = int(input('KIẾM TRA CÁC SỐ TỪ 2 ĐẾN SỐ: '))

for i in range(2, a+1):
    for j in range(2, i):
        if i % j == 0:
            print(f'{i} không phải là nguyen to')
            break
    else:
        print(f'{i} LÀ SỐ NGUYÊN TỐ!')
