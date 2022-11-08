# Import các thư viện cần thiết
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

# Mở ảnh
img = Image.open('assets/dark_image.jpg')

# Biến đổi ảnh màu thành ảnh xám
img = img.convert('L')

# Số lượng pixels trong ảnh = chiều rộng ảnh x chiều cao ảnh
numberOfPixels = img.size[0] * img.size[1]

# Biến đổi ảnh thành ma trận 2 chiều với
# số dòng là chiều cao ảnh, số cột là chiều rộng ảnh
matrix_img = np.asarray(img)

# Biến đổi ma trận thành mảng 1 chiều => Thuận tiện cho việc đếm số lần xuất hiện của các giá trị mức xám
pixels = matrix_img.flatten()


# Biểu đồ phân bố tần số của các giá trị mức xám

def getImageHistogram(matrix_img):
    # Tạo mảng với kích thước là 256 để lưu số lần xuất hiện của các giá trị mức xám từ 0 đến 255
    # Giá trị mặc định của mỗi phần tử trong mảng là 0
    histogram = np.zeros(256)

    # Các pixels trong ảnh chỉ có giá trị mức xám từ 0 đến 255
    # => Các giá trị mức xám cũng chính là indexes của mảng

    # Nếu xuất hiện giá trị mức xám nào thì ta sẽ cộng thêm 1 lần xuất hiện cho phần tử lưu số lần xuất hiện của giá trị mức xám tương ứng

    for pixel in matrix_img:
        histogram[pixel] += 1

    return histogram


imgHist = getImageHistogram(pixels)

# Đồ thị phân bố tần số của các giá trị mức xám trong ảnh
plt.plot(imgHist)
plt.title('Trước khi áp dụng thuật toán Histogram Equalization')
plt.xlabel('Mức xám')
plt.ylabel('Số lượng pixel')
plt.show()

# Tính tần suất tích lũy


# f: mảng chứa tần số của các giá trị mức xám
def cumulativeRelativeFrequencyDistributions(f, N):
    # N: Số lượng pixels trong ảnh
    result = [f[0] / N]  # tạo mảng để lưu trữ tần suất tích lũy
    for i in range(1, len(f)):
        result.append(result[-1] + (f[i] / N))
    return np.array(result)


crfd = cumulativeRelativeFrequencyDistributions(imgHist, numberOfPixels)


def equalHist(crfd):
    for i in range(len(crfd)):
        crfd[i] *= 255
        crfd[i] = int(crfd[i])
    return crfd


sk = equalHist(crfd)

# Ánh xạ các mức xám biến đổi được cho số lượng pixel tương ứng

"""
for i in range(len(pixels)):	
    pixels[i] = sk[pixels[i]]

# Tương đương câu lệnh dưới
"""


pixels_new = sk[pixels]

# Biểu đồ phân bố tần số của các giá trị mức xám sau khi áp dụng thuật toán Histogram equalization
plt.hist(pixels_new, bins=256)
plt.title('Sau khi áp dụng thuật toán Histogram Equalization')
plt.xlabel('Mức xám')
plt.ylabel('Số lượng pixel')
plt.show()

# Biến mảng trở lại thành ma trận vì lúc đầu ta biến ma trận thành mảng 1 chiều để thuận tiện đếm số lần xuất hiện của các giá trị xám
matrix_img_new = np.reshape(pixels_new, matrix_img.shape)

# Hiển thị ảnh trước và sau khi áp dụng thuật toán
fig = plt.figure()
fig.set_figheight(15)
fig.set_figwidth(15)

fig.add_subplot(1, 2, 1)
plt.imshow(matrix_img, cmap='gray')

fig.add_subplot(1, 2, 2)
plt.imshow(matrix_img_new, cmap='gray')

plt.show(block=True)
