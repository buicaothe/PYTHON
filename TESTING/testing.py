import numpy as np

# 1. Tạo mảng 1 chiều (1D) từ một list
arr_1d = np.array([1, 2, 3, 4, 5])
print("Mảng 1D:", arr_1d)

# 2. Tạo mảng 2 chiều (2D - Ma trận) từ list lồng nhau
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\nMảng 2D:\n", arr_2d)

# 3. Tạo mảng gồm toàn số 0 (hữu ích để khởi tạo bộ nhớ trước)
zeros_arr = np.zeros((3, 3)) # Ma trận 3x3
print("\nMảng toàn số 0:\n", zeros_arr)

# 4. Tạo mảng với dãy số liên tiếp (tương tự hàm range() của Python)
# np.arange(start, stop, step)
range_arr = np.arange(0, 10, 2) 
print("\nMảng dãy số bước 2:", range_arr) # Kết quả: [0 2 4 6 8]

import numpy as np

matrix = np.array([[1.5, 2.0, 3.1], [4.2, 5.5, 6.9]])

print("\nMảng :\n", matrix)

print("Số chiều (ndim):", matrix.ndim)       # Kết quả: 2
print("Kích thước (shape):", matrix.shape)     # Kết quả: (2, 3) - 2 hàng, 3 cột
print("Tổng số phần tử (size):", matrix.size)  # Kết quả: 6
print("Kiểu dữ liệu (dtype):", matrix.dtype)   # Kết quả: float64

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

# Các phép toán cơ bản áp dụng cho từng phần tử (element-wise)
print("Cộng:", a + b)       # [11, 22, 33, 44]
print("Trừ:", a - b)        # [9, 18, 27, 36]
print("Nhân:", a * b)       # [10, 40, 90, 160]
print("Bình phương a:", a**2) # [100, 400, 900, 1600]

# Các hàm toán học tích hợp (Universal Functions)
print("\nCăn bậc 2 của b:", np.sqrt(b))
print("Tổng tất cả phần tử trong a:", np.sum(a))
print("Giá trị trung bình của a:", np.mean(a))
print("Giá trị lớn nhất trong a:", np.max(a))