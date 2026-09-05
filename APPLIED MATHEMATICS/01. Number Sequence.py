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
# ===============================================================
# ********************* NUMBER SEQUENCE *************************
# Dòng 1: Nạp NumPy để làm việc với mảng số học và các hàm lượng giác véc-tơ hóa
import numpy as np

# Dòng 2: Nạp hàm minimize từ thư viện con optimize của SciPy để tìm điểm cực tiểu
from scipy.optimize import minimize

# Dòng 3: Nạp mô-đun pyplot từ Matplotlib để trực quan hóa đồ thị hàm số
import matplotlib.pyplot as plt

# Dòng 4: Khai báo hàm mục tiêu cần tối ưu f(x) = x^2 + 10*sin(x)


def ham_muc_tieu(x):
    # Dòng 5: Trả về giá trị của hàm số tại điểm x
    return x**2 + 10 * np.sin(x)


# Dòng 6: Thiết lập điểm đoán ban đầu (initial guess) cho thuật toán là x = 2.0
diem_khoi_tao = -500.0

# Dòng 7: Gọi thuật toán SciPy để tìm tọa độ x làm hàm mục tiêu đạt giá trị nhỏ nhất
ket_qua = minimize(ham_muc_tieu, diem_khoi_tao)

# Dòng 8: Lấy nghiệm x tối ưu tìm được từ kết quả trả về của SciPy (kết quả lưu ở trường .x)
x_min = ket_qua.x[0]

# Dòng 9: In tọa độ nghiệm cực tiểu ra màn hình với 4 chữ số thập phân
print(
    f"Điểm cực tiểu tại x = {x_min:.4f}, giá trị f(x) = {ham_muc_tieu(x_min):.4f}")

# Dòng 10: Tạo mảng 500 điểm liên tục từ -10 đến 10 để vẽ đường cong đồ thị mượt mà
x_ve = np.linspace(-10, 10, 10)

# Dòng 11: Khởi tạo khung vẽ đồ thị có kích thước 7x4 inch
plt.figure(figsize=(7, 4))

# Dòng 12: Vẽ đường cong của hàm số theo tọa độ (x_ve, ham_muc_tieu(x_ve))
plt.plot(x_ve, ham_muc_tieu(x_ve), label='f(x) = x^2 + 10*sin(x)', color='blue')

# Dòng 13: Đánh dấu điểm cực tiểu vừa tìm được bằng một dấu chấm tròn đỏ nổi bật
plt.scatter(x_min, ham_muc_tieu(x_min), color='red',
            s=60, zorder=5, label='Điểm cực tiểu (SciPy)')

# Dòng 14: Hiển thị hộp chú thích (legend) để phân biệt các thành phần trên hình
plt.legend()

# Dòng 15: Xuất hình vẽ ra màn hình
plt.show()
