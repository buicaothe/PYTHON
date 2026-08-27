'''
f = open("vi-du.txt", "w", encoding="utf-8")  # Mở để ghi
f.write("Chào bạn, tôi là BUI CAO THE!")
f.close()  # Quan trọng: Phải đóng file để giải phóng bộ nhớ

# Ghi file
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Dòng 1\n")
    f.write("Dòng 2")

# Đọc file
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

file = open("testfile.txt", "r", encoding="utf-8")
content = file.read()
print(content)
file.close()


f = None
try:
    f = open('test.txt')
    result = f.read()
    print(result)
    print('the file is ', 'closed' if f.closed else 'open')
except:
    print('the file could not be open')
finally:
    if f and not f.closed:
        f.close()
        print('the file is ', 'closed' if f.closed else 'open')



f = None
try:
    # Mở tệp tin
    f = open('testing.pdf', 'r')
    result = f.read()
    print(result)

except IOError as e:
    print(f"Lỗi IO: {e}")

except ValueError as ve:
    print(f"Lỗi giá trị: {ve}")

except EOFError as eofe:
    print(f"Lỗi kết thúc tệp: {eofe}")

except Exception as e:
    # Thay vì 'except:', dùng 'Exception as e' để bắt lỗi cụ thể hơn
    print(f"Lỗi không xác định: {e}")

finally:
    # Đảm bảo tệp luôn được đóng
    if f and not f.closed:
        f.close()

    # Kiểm tra trạng thái cuối cùng
    status = 'closed' if f is None or f.closed else 'open'
    print(f'The file is {status}')
'''

# f = open('names.txt')
# print(f.read())
# print(f.read(4))
# print(f.readline())
# print(f.readline())
# for line in f:
#     print(line)

# f.close
# try:
#     f = open('names.txt')
#     print(f.read())

# except:
#     print('The file you want to read doesnt exist')
# finally:
#     f.close()

# f = open('names.txt', 'a')
# f.write('Neils')
# f.close()

# f = open('names.txt')
# a = f.read()
# print(a)
# f.close()

# open to write and then close:

# f = open('test.txt', 'w')
# f.write('Please chek the conten again!')
# f.close()

# # must OPen first: before reading
# f = open('test.txt')
# a = f.read()
# print(a)
# f.close()

# 2 wys to create new files:
# opens a file for wirting, creats the file of ot dose not exist:
# f = open('name_list.txt', 'w')
# f.close()

# c=Creat a file, but the file returns an erro if the fiel exist:
# import os
# if os.path.exists("test.txt"):
#     os.remove('test.txt')
# else:
#     print('The file you wnat tot delete does not exist')


# with open('names.txt') as f:
#     content = f.read()

# with open('name_list.txt', 'w') as f:
#     f.write(content)

# with open('name_list.txt') as f:
#     print(f.read())

# items = '01 02 03 04 05 06 07 new content to be added'
# items = items.split(' ')
# print('Nội dung của item đã biến thành list = ', items)

# with open('name_list.txt', 'a') as f:
#     for i in items:
#         f.write('\n'+i)

# with open('name_list.txt') as f:
#     print(f.read())

# try:
#     f = open('test.txt', 'x')
# except:
#     print("File đã có sẵn không cần tạo mới!!!")
#     f = open('test.txt')
#     x = f.read()
#     print('Nội dung trước đó của file test.txt: ',
#           'f=FILE TRỐNG' if x == '' else x)
# finally:
#     f.close()

# list = "DAY LA NIO DUGN DUOC THEM VAO"
# list = list.split()
# with open('test.txt', 'a') as file:
#     for item in list:
#         file.write('\n'+item)
# with open('test.txt') as file:
#     print('Nội dung file test.txt cập nhật mới nhất: ', file.read())

# f = None
# try:
#     f = open('test.txt')
#     result = f.read()
#     print('In lần nữa: ', result)
#     print('the file is ', 'closed' if f.closed else 'open')
# except:
#     print('the file could not be open')
# finally:
#     if f and not f.closed:
#         f.close()
#         print('the file is ', 'closed' if f.closed else 'open')


# f = None
# try:
#     # Mở file để đọc
#     f = open('testing.pdf', 'r')
#     result = f.read()
#     print(result)

# except IOError as e:
#     print(f"Lỗi I/O Lỗi liên quan đến đầu vào/đầu ra (ví dụ: không tìm thấy file): {e}")

# except ValueError as ve:
#     print(f"Lỗi giá trị Lỗi giá trị không hợp lệ: {ve}")

# except EOFError as eofe:
#     print(f"Lỗi kết thúc file - Lỗi khi đọc đến cuối file một cách bất ngờ: {eofe}")

# except Exception as e:
#     # Bắt các lỗi không mong đợi khác. Bắt tất cả các loại lỗi còn lại chưa được liệt kê ở trên
#     print(f"Lỗi không xác định: {e}")

# finally:
#     # Đảm bảo file luôn được đóng cho dù có lỗi hay không
#     if f and not f.closed:
#         f.close()

#     # Kiểm tra trạng thái file cuối cùng
#     status = 'closed' if f is None or f.closed else 'open'
#     print(f'Trạng thái file hiện tại là: {status}')

# f = None
# try:
#     # Mở file test.txt (mặc định là chế độ đọc 'r')
#     f = open('test.txt')
#     result = f.read()
#     print(result)

# except (IOError, ValueError, EOFError) as ive:
#     # Xử lý chung cho cả 3 loại lỗi
#     print('error: ', ive)

# except Exception as e:
#     # Bắt các lỗi không mong đợi khác
#     print('unexpected error:', e)

# finally:
#     # Kiểm tra và đóng file nếu file đang mở
#     if f and not f.closed:
#         f.close()

#     # In trạng thái đóng/mở của file bằng cấu trúc rút gọn (Ternary Operator)
#     status = 'closed' if f is None or f.closed else 'open'
#     print(f'the file is {status}')

# try:
#     with open('test.txt') as fi, open('copy_test.txt', 'w') as fo:
#         result = fi.read()
#         print(f'copied from {fi.name} to {fo.name}:')
#         fo.write(result)
# except:
#     print('Lỗi xảy ra - errr!!')
# print("--------------------------")
# with open('copy_test.txt') as fo:
#     print(fo.read())

# filename = 'test.txt'
# text = 'This is my favourite'
# with open(filename, 'w') as f:
#     num = f.write(text)
# print(f'{num} characters were written into {filename}')

# with open() as f:
#     print(f.read())


from sys import argv
from pathlib import Path

nro, chars = 0, 0
# argv is the name of a file given as a parameter to the program
if len(argv) == 2 and Path(argv[1]).is_file():
    try:
        for line in open(argv[1], 'r'):
            print(f'{nro}: {line}')
            nro += 1
            chars += len(line)
        else:
            print(f"Total of {nro} lines and {chars} characters read.")
    except (IOError, EOFError, ValueError) as e:
        print(e)
    except Exception as ee:
        print("Something went wrong", ee)
else:
    print("File does not exist")
