import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Tạo một bảng dữ liệu mẫu bằng Pandas
df = pd.DataFrame(
    {"KinhNghiem": [1, 3, 5, 7, 10], "Luong": [10, 20, 35, 50, 80]}
)

# Thiết lập giao diện trực quan của seaborn
sns.set_theme(style="whitegrid")

# Vẽ biểu đồ phân tán kết hợp đường hồi quy tuyến tính
sns.regplot(x="KinhNghiem", y="Luong", data=df, color="blue")

plt.title("Mối quan hệ giữa kinh nghiệm và mức lương")
plt.show()
