'''
try:
    # Khối lệnh có nguy cơ xảy ra lỗi
    so_chia = 10 / int(input("Nhập số chia: "))
except ZeroDivisionError:
    # Xử lý khi xảy ra lỗi chia cho 0
    print("Lỗi: Không thể chia cho số 0!")
except ValueError:
    # Xử lý khi người dùng nhập chữ thay vì số
    print("Lỗi: Bạn phải nhập một con số!")
else:
    # Chạy KHI VÀ CHỈ KHI khối try không có lỗi nào
    print("Phép chia thành công, kết quả là:", so_chia)
finally:
    # Luôn luôn chạy, dù có lỗi hay không
    print("Kết thúc quá trình xử lý.")


try:
    # Đoạn code có thể gây nhiều lỗi
    so = int(input("Nhập một số bất ký: "))
    ket_qua = 100 / so

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file dữ liệu.")

except ValueError:
    print("Lỗi: Dữ liệu trong file không phải là số.")

except ZeroDivisionError:
    print("Lỗi: Số trong file bằng 0, không chia được.")

except Exception as e:
    # Đây là "lưới cuối cùng" bắt mọi lỗi còn lại
    print(f"Lỗi phát sinh ngoài dự kiến: {e}")

else:
    print(f'Bạn đã nhập đúng đầu vào là con số, cụ thể là số {so}')

finally:
    print('Kết thúc chương trình')
'''
f = None
try:
    f = open('testFoo.txt')
    result = f.read()
    print(result)
    print('The file is', 'closed!' if f.closed else 'open!')
except:
    print('The file could not be OPen!')
finally:
    if f and not f.closed:
        f.close()
        print('the file is', 'closed' if f.closed else 'open!')
