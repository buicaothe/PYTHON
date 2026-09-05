'''
board = [None]*4
board[0] = list('ABC')

#board[1:] = [['-' for _ in range (3)] for _ in range(3)]

print(board)
print(board[1:])
print(board[0])
print(board[1])
print(board[2])
print(board[3])

matrice = [[f'A{j+1}{i+1}' for i in range(3)] for j in range(5)]

for i in range(5): print(matrice[i])

import random

# 1. Khởi tạo bàn cờ và các biến
board = [['_', '_', '_'], 
         ['_', '_', '_'], 
         ['_', '_', '_']]

player = 'X'  # Người chơi là X
bot = 'O'     # Máy là O
turns = 0
win = False

# 2. Vòng lặp chính
while turns < 9 and not win:
    # In bàn cờ
    print("\n  0 1 2")
    row_idx = 0
    for row in board:
        print(row_idx, row[0], row[1], row[2])
        row_idx += 1

    if turns % 2 == 0:
        # LƯỢT CỦA NGƯỜI
        print("\n--- Lượt của bạn (X) ---")
        r_in = input("Nhập hàng (0-2): ")
        c_in = input("Nhập cột (0-2): ")
        
        # Kiểm tra nhập liệu
        if r_in not in ['0', '1', '2'] or c_in not in ['0', '1', '2']:
            print("!! Chỉ nhập 0, 1 hoặc 2 !!")
            continue
        
        r, c = int(r_in), int(c_in)
        if board[r][c] != '_':
            print("!! Ô này đã có người đánh !!")
            continue
            
        board[r][c] = player
        current_check = player
    else:
        # LƯỢT CỦA MÁY
        print("\n--- Máy (O) đang suy nghĩ... ---")
        # Vòng lặp để máy tìm ô trống
        while True:
            bot_r = random.randint(0, 2)
            bot_c = random.randint(0, 2)
            if board[bot_r][bot_c] == '_':
                board[bot_r][bot_c] = bot
                break
        current_check = bot

    turns += 1

    # 3. Kiểm tra thắng cuộc
    # Kiểm tra hàng & cột
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '_': win = True
        if board[0][i] == board[1][i] == board[2][i] != '_': win = True
    # Kiểm tra đường chéo
    if board[0][0] == board[1][1] == board[2][2] != '_': win = True
    if board[0][2] == board[1][1] == board[2][0] != '_': win = True

    if win:
        # In kết quả cuối cùng
        print("\n  0 1 2")
        row_idx = 0
        for row in board:
            print(row_idx, row[0], row[1], row[2])
            row_idx += 1
        
        if current_check == player:
            print("\nCHÚC MỪNG! Bạn đã thắng Máy! 🎉")
        else:
            print("\nMáy thắng rồi! Chúc bạn may mắn lần sau. 🤖")
    elif turns == 9:
        print("\nHÒA RỒI!")


import random

def solve_sliding_puzzle():
    # 1. GIAI ĐOẠN CHUẨN BỊ (PREPARATION)
    # Khởi tạo bộ dữ liệu gốc (Immutable - Tuple)
    ORIGINAL = tuple("UNCOPYRIGHTABLE") # 15 chữ cái duy nhất
    n = len(ORIGINAL)
    
    # Vòng lặp tìm cấu hình có thể giải được (Solvable)
    while True:
        indexes = list(range(n))
        random.shuffle(indexes)
        
        # Kiểm tra tính khả thi (Solvability check)
        # Một puzzle 15 ô (lưới 4x4) giải được khi số nghịch thế là CHẴN 
        # (Vì ô trống mặc định nằm ở dòng cuối cùng - dòng 4)
        inversions = 0
        for i in range(n):
            for j in range(i + 1, n):
                if indexes[i] > indexes[j]:
                    inversions += 1
        
        if inversions % 2 == 0:
            break
            
    # 2. THIẾT LẬP BÀN CỜ (BOARD SETUP)
    # Tạo board từ indexes và thêm ô trống (Blank slot)
    board = [ORIGINAL[i] for i in indexes]
    board.append("_") # Ô trống ở cuối danh sách 16 phần tử
    
    # 3. VÒNG LẶP GIẢI ĐỐ (SOLVING LOOP)
    while True:
        print("\n--- SLIDING PUZZLE 4x4 ---")
        # In bàn cờ dưới dạng 4 hàng x 4 cột
        for i in range(0, 16, 4):
            print("  ".join(board[i:i+4]))
        
        # Kiểm tra điều kiện thắng
        # Board hiện tại (bỏ ô cuối) phải giống ORIGINAL và ô cuối phải là "_"
        if tuple(board[:-1]) == ORIGINAL and board[-1] == "_":
            print("\nCHÚC MỪNG! Bạn đã giải xong câu đố!")
            break
            
        # Nhập ô muốn di chuyển
        move = input("\nNhập chữ cái muốn di chuyển (hoặc 'q' để thoát): ").upper()
        if move == 'Q': break
        
        if move not in board or move == "_":
            print("Lỗi: Ký tự không hợp lệ!")
            continue
            
        # Tìm vị trí index của ô chọn và ô trống
        idx_move = board.index(move)
        idx_empty = board.index("_")
        
        # Tính toán vị trí hàng/cột (0-3) từ index một chiều
        row_m, col_m = divmod(idx_move, 4)
        row_e, col_e = divmod(idx_empty, 4)
        
        # Kiểm tra tính kề cạnh (Adjacent): 
        # Cùng hàng và cách nhau 1 cột HOẶC Cùng cột và cách nhau 1 hàng
        is_adjacent = (row_m == row_e and abs(col_m - col_e) == 1) or \
                      (col_m == col_e and abs(row_m - row_e) == 1)
        
        if is_adjacent:
            # Hoán đổi (Swap)
            board[idx_empty], board[idx_move] = board[idx_move], board[idx_empty]
        else:
            print("Lỗi: Chỉ có thể di chuyển ô cạnh ô trống!")

if __name__ == "__main__":
    solve_sliding_puzzle()
'''
import random

# 1. GIAI ĐOẠN CHUẨN BỊ (PREPARATION)
# Khởi tạo bộ dữ liệu gốc (Immutable Tuple - Một chiều)
ORIGINAL = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

# Vòng lặp tìm cấu hình có thể giải được (Solvable)
solvable = False
while not solvable:
    # Khởi tạo danh sách chỉ số (Mutable List)
    indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    
    # Xáo trộn danh sách chỉ số
    random.shuffle(indexes)
    
    # Kiểm tra tính khả thi bằng cách đếm số nghịch thế (Inversions)
    inversions = 0
    for i in range(15):
        for j in range(i + 1, 15):
            # Cặp (a, b) tạo thành nghịch thế nếu a xuất hiện trước b nhưng a > b
            if indexes[i] > indexes[j]:
                inversions += 1
    
    # Nếu số nghịch thế là số chẵn, cấu hình này có thể giải được
    if inversions % 2 == 0:
        solvable = True

# 2. THIẾT LẬP BÀN CỜ (BOARD SETUP)
board = []
for i in range(15):
    # Đưa các phần tử từ ORIGINAL vào board dựa trên indexes đã xáo trộn
    board.append(ORIGINAL[indexes[i]])

# Thêm ô trống vào cuối bàn cờ
board.append(" ") 

# 3. VÒNG LẶP GIẢI ĐỐ (SOLVING LOOP)
while True:
    print("\n--- SLIDING PUZZLE 4x4 ---")
    
    # In nội dung bàn cờ dưới dạng 4 hàng và 4 cột
    for i in range(0, 16, 4):
        print(board[i], "\t", board[i+1], "\t", board[i+2], "\t", board[i+3])
    
    # Kiểm tra xem board hiện tại có giống ORIGINAL không (so sánh 15 ô đầu)
    is_solved = True
    for i in range(15):
        if board[i] != ORIGINAL[i]:
            is_solved = False
    
    # Nếu giống và ô trống nằm ở cuối cùng, người dùng đã thắng
    if is_solved and board[15] == " ":
        print("\nCHÚC MỪNG! Bạn đã hoàn thành trò chơi.")
        break
    
    # Yêu cầu người dùng nhập slot muốn di chuyển
    # Lưu ý: Chương trình sẽ crash nếu nhập ký tự không phải số hoặc số không có trong board
    move = int(input("\nNhập số ô muốn di chuyển: "))
    
    # Tìm vị trí (index) của ô chọn và ô trống trên mảng một chiều
    idx_move = -1
    idx_empty = -1
    for i in range(16):
        if board[i] == move:
            idx_move = i
        if board[i] == " ":
            idx_empty = i
            
    # Tính hàng (row) và cột (col) từ index một chiều
    row_m = idx_move // 4
    col_m = idx_move % 4
    row_e = idx_empty // 4
    col_e = idx_empty % 4
    
    # Tính khoảng cách hàng và cột (tương đương abs())
    diff_row = row_m - row_e
    if diff_row < 0: diff_row = -diff_row
    
    diff_col = col_m - col_e
    if diff_col < 0: diff_col = -diff_col
    
    # Kiểm tra tính kề cạnh: được phép tráo đổi nếu nằm cùng hàng/cột và cạnh nhau
    if (row_m == row_e and diff_col == 1) or (col_m == col_e and diff_row == 1):
        # Tráo đổi ô chọn với ô trống
        board[idx_empty], board[idx_move] = board[idx_move], board[idx_empty]
    else:
        print("Lỗi: Ô được chọn không nằm cạnh ô trống!")