# def print_collection(coll, current, s):
#     if current == len(coll):
#         return s
#     else:
#         s += coll[current]
#         return print_collection(coll,
#                                 current+1,
#                                 s)


# a = print_collection(['xin '], 0, 'buicaothe')

# print(a)
# print(len(a))


# import time
# from tkinter import Tk, Frame, Button, Label, Entry, messagebox
# from random import choice

# # --- Decorator đo thời gian ---

# import time
# def timeit(f):
#     def wrap(*args, **kwargs):
#         t1 = time.time()  # before
#         res = f(*args, **kwargs)
#         t2 = time.time()  # after
#         print(f'{f.__name__} used {t2-t1:.4f} sec')
#         return res
#     return wrap


# # --- Các hàm xử lý sự kiện (Callbacks) ---


# def show():
#     messagebox.showinfo("Thông báo", "Bạn vừa nhấn nút Info!")


# def show_info(event):
#     # event là đối số mặc định khi dùng .bind()
#     content = event.widget.get()
#     messagebox.showinfo("Entry", f"Bạn đã nhập: {content}")


# def kl(selection, label_widget):
#     # Hàm này mô phỏng việc tung đồng xu
#     result = choice(['Heads', 'Tails'])
#     if selection == result:
#         text = f"Đúng rồi! Kết quả là {result}"
#     else:
#         text = f"Sai rồi! Kết quả là {result}"
#     label_widget.config(text=text)

# # --- Hàm chính dựng giao diện ---


# def main():
#     root = Tk()
#     root.title('Events')
#     root.geometry('300x200')

#     # 1. Nút bấm đơn giản (Callback không tham số)
#     Button(root, text='Info', command=show).pack(pady=5)

#     # 2. Ô nhập liệu (Binding với phím Enter)
#     label_hint = Label(root, text="Nhập gì đó rồi ấn Enter:")
#     label_hint.pack()
#     entry = Entry(root)
#     entry.bind('<Return>', show_info)
#     entry.pack(pady=5)

#     # 3. Frame chứa các nút bấm dùng Lambda
#     # Lưu ý: Tách riêng .pack() để biến 'frame' không bị nhận giá trị None
#     frame = Frame(root)
#     frame.pack(pady=10)

#     k, l = 'Heads', 'Tails'

#     label_result = Label(root, text="Chọn mặt đồng xu!", width=100)
#     label_result.pack()

#     # Nút bên trái (Sử dụng Lambda để truyền tham số)
#     Button(frame, text=k,
#            command=lambda val=k: kl(val, label_result)).pack(side='left', padx=10)

#     # Nút bên phải (Sử dụng Lambda để truyền tham số)
#     Button(frame, text=l,
#            command=lambda val=l: kl(val, label_result)).pack(side='right', padx=10)

#     root.mainloop()


# if __name__ == '__main__':
#     main()


# sum_2 = 0
# counter = 0
# collection = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# while counter < len(collection):
#     sum_2 += collection[counter]
#     counter += 1

# print(sum_2, "while")


# import time
# from tkinter import Tk, Frame, Button, Label, Entry, messagebox
# from random import choice

# # --- Biến toàn cục ---
# previous = 'cyan'

# # --- Decorator đo thời gian (từ ảnh trước của bạn) ---


# def timeit(f):
#     def wrap(*args, **kwargs):
#         t1 = time.time()
#         res = f(*args, **kwargs)
#         t2 = time.time()
#         print(f'{f.__name__} used {t2-t1:.4f} sec')
#         return res
#     return wrap

# # --- Các hàm xử lý (Hàm Callback) ---


# def show():
#     """Hiển thị hộp thoại thông báo đơn giản"""
#     messagebox.showinfo("Hello", "This is a messagebox.")


# def show_info(event):
#     """Lấy dữ liệu từ Entry khi nhấn Enter và xóa nội dung cũ"""
#     d = event.__dict__
#     # d['widget'] tương đương với biến 'entry'
#     messagebox.showinfo("Hello", d['widget'].get())
#     d['widget'].delete(0, 'end')


# @timeit
# def kl(player, label):
#     """Xử lý logic thắng thua và đổi màu nền ngẫu nhiên"""
#     global previous
#     # Vòng lặp đảm bảo màu mới không trùng với màu vừa xuất hiện
#     while True:
#         background = choice(['yellow', 'green', 'blue', 'red', 'cyan'])
#         if previous != background:
#             previous = background
#             break

#     machine = choice(['Heads', 'Tails'])
#     result_text = f"{machine}, {'You won!' if player == machine else 'Sorry - you lost!'}"

#     # Cập nhật nội dung và màu nền cho Label
#     label.config(text=result_text, bg=background)

# # --- Hàm dựng giao diện chính ---


# def main():
#     root = Tk()
#     root.title('Events')
#     root.geometry('350x200')  # Tăng kích thước một chút để dễ nhìn

#     # 1. Nút Info
#     Button(root, text='Info', command=show).pack(pady=5)

#     # 2. Ô nhập liệu (Nhấn Enter để hiện thông báo)
#     entry = Entry(root)
#     entry.bind('<Return>', show_info)
#     entry.pack(pady=5)

#     # 3. Frame chứa 2 nút chọn (Lưu ý: Tách biệt .pack() để tránh lỗi NoneType)
#     my_frame = Frame(root)
#     my_frame.pack(pady=10)

#     k, l = 'Heads', 'Tails'

#     # 4. Label hiển thị kết quả
#     result_label = Label(root, text='Make a guess!', width=40)
#     result_label.pack(pady=10)

#     # Nút bấm SAI (Sẽ tự chạy ngay khi mở App)
#     # Button(my_frame, text=k, command=kl(k, result_label)).pack(side='left', padx=30)

#     # Nút bấm ĐÚNG (Dùng lambda để bọc lại)
#     # Nút Heads
#     Button(my_frame, text=k,
#            command=lambda val=k: kl(val, result_label)).pack(side='left', padx=30)

#     # Nút Tails
#     Button(my_frame, text=l,
#            command=lambda val=l: kl(val, result_label)).pack(side='right', padx=30)

#     root.mainloop()


# if __name__ == '__main__':
#     main()


# def x(i=i): return i*str(i)


# y = [int(x(k)) for k in range(1, 10, 3)]

# import time


# def showprogress(start, stop, step=10, txt='%'):
#     for i in range(start, stop, step):
#         print('\r\r', i, txt, end='', flush=True)
#         time.sleep(0.3)


# showprogress(0, 105, step=10, txt='%')

# def is_valid_business_id(business_id):
#     unique_part = business_id[:7]
#     check_part = business_id[8]
#     coefficients = [7, 9, 10, 5, 8, 4, 2]
#     checksum = sum(int(num) * coeff for num,
#                    coeff in zip(unique_part, coefficients))
#     c = checksum % 11
#     comp_part = '0' if c == 0 else str(11 - c)
#     if comp_part != 1 and comp_part == check_part:
#         return 'valid business id'


from tkinter import Tk, Frame, Button, Label
from random import choice

previous = 'cyan'


def kl(player, label):
    global previous
    while True:
        background = choice(['yellow', 'green', 'blue', 'red', 'cyan'])
        if previous != background:
            previous = background
            break
    machine = choice(['Heads', 'Tails'])
    label.config(text=f"{machine}, {'You won!' if player == machine else 'Sorry - you lost!'}",
                 bg=background)


def main():
    root = Tk()
    root.title('Heads or Tails')
    root.geometry('250x100')
    label = Label(root, text='', width=100)
    label.pack()
    frame = Frame(root).pack()
    Button(frame, text='Heads', command=lambda k='Heads': kl(
        k, label)).pack(side='left', padx=30)
    Button(frame, text='Tails', command=lambda k='Tails': kl(
        k, label)).pack(side='right', padx=30)
    root.mainloop()


if __name__ == '__main__':
    main()
