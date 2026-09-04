# ----------- 01. NUMBER SEQUENCE -----------
# IMPORTING THE PACKAGES
# THIS CELL NEEDS TO BE EXECUTED BEFORE THEY CAN BE USED
import math
import numpy as np
import scipy as sp
import sympy as sy
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import hashlib
import cryptography
# %matplotlib inline


n = sy.symbols('n', integer=True, positive=True)

# Khai báo biểu thức
an = (1 + 1/n)**n

# Tính giới hạn khi n tiến đến vô cùng (sy.oo là ký hiệu vô hạn)
limit_val = sy.limit(an, n, sy.oo)

print("Giới hạn của dãy:", limit_val)  # Kết quả: E

# Dòng 1: Nạp thư viện pandas và đặt bí danh là pd để thao tác với bảng dữ liệu

# Dòng 2: Nạp mô-đun pyplot từ thư viện matplotlib để vẽ biểu đồ

# Dòng 3: Tạo một từ điển (dictionary) chứa dữ liệu thô với 2 cột: 'Ten' và 'Diem'
raw_data = {"Ten": ["An", "Bình", "Cường", "Dung"],
            "Diem": [8.5, 7.0, 9.2, 6.8]}

# Dòng 4: Chuyển đổi từ điển raw_data thành DataFrame (cấu trúc bảng 2 chiều của pandas)
df = pd.DataFrame(raw_data)

# Dòng 5: Lọc các hàng có 'Diem' >= 8.0 và tính điểm trung bình (.mean()) của cột 'Diem' đó
diem_tb_gioi = df[df["Diem"] >= 8.0]["Diem"].mean()

# Dòng 6: In kết quả ra màn hình bằng f-string (định dạng số thực với 2 chữ số thập phân: .2f)
print(f"Điểm trung bình nhóm giỏi: {diem_tb_gioi:.2f}")

# Dòng 7: Khởi tạo một hình vẽ (figure) với kích thước chiều ngang 6 inch, chiều dọc 4 inch
plt.figure(figsize=(6, 4))

# Dòng 8: Vẽ biểu đồ cột với trục X là tên học sinh, trục Y là điểm số
plt.bar(df["Ten"], df["Diem"], color="skyblue")

# Dòng 9: Đặt nhãn tiêu đề cho trục tung (trục Y)
plt.ylabel("Điểm số")

# Dòng 10: Đặt tên tiêu đề chính cho biểu đồ
plt.title("Biểu đồ điểm số học sinh")

# Dòng 11: Yêu cầu Kernel kết xuất và hiển thị đồ thị ra ô kết quả (output cell)
plt.show()
