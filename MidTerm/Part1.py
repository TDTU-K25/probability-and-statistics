from statistics import *  # Import tất cả các hàm trong thư viện statistics


def example_mean():
    # Tính giá trị trung bình cộng của tập dữ liệu

    print(mean([1, 3, 8]))
    # (1 + 3 + 8) / 3 = 12 / 3 = 4

    print(mean([3.2, 4.8, -1.2, 2.9]))
    # (3.2 + 4.8 - 1.2 + 2.9) / 4 = 9.7 / 4 = 2.425

# example_mean()


def example_fmean():
    # Chuyển đổi các giá trị trong tập dữ liệu thành kiểu dữ liệu float
    # Sau đó tính giá trị trung bình cộng của tập dữ liệu

    print(fmean([1, 3, 8]))
    # (1.0 + 3.0 + 8.0) / 3 = 12.0 / 3 = 4.0

    print(fmean([2, 4, 6], [0.2, 0.5, 0.6]))
    # (2.0 * 0.2 + 4.0 * 0.5 + 6.0 * 0.6) /  (0.2 + 0.5 + 0.6) = 6.0 / 1.3

    print(fmean([3.2, 4.8, -1.2, 2.9]))
    # (3.2 + 4.8 - 1.2 + 2.9) / 4 = 9.7 / 4 = 2.425

# example_fmean()


def example_geometric_mean():
    # Tính giá trị trung bình nhân của tập dữ liệu

    print(geometric_mean([32, 16, 40]))
    # Căn bậc 3 của (32 * 16 * 40) = (32 * 16 * 40) ** (1/3)
    # Vì tập dữ liệu có 3 giá trị nên ta lấy căn bậc 3

    print(geometric_mean([24, 15, 9, 92, 103]))
    # Căn bậc 5 của (24 * 15 * 9 * 92 * 103) = (24 * 15 * 9 * 92 * 103) ** (1/5)
    # Vì tập dữ liệu có 5 giá trị nên ta lấy căn bậc 5

    # => Tập dữ liệu có n giá trị ta lấy căn bậc n của tích n giá trị

# example_geometric_mean()


def example_harmonic_mean():
    # Tính giá trị trung bình điều hòa của tập dữ liệu

    print(harmonic_mean([2, 4, 6]))
    # (1 + 1 + 1) / (1/2 + 1/4 + 1/6) = 3 / (1/2 + 1/4 + 1/6) = 3 / (11/12) = 36 / 11

    print(harmonic_mean([2, 4, 6], [2, 3, 9]))
    # (2 + 3 + 9) / (2/2 + 3/4 + 9/6) = 14 / (13/4) = 56 / 13

# example_harmonic_mean()


def example_median():
    # Tìm trung vị của tập dữ liệu

    print(median([1, 11, 13, 5, 7, 10]))
    # Đầu tiên tập dữ liệu sẽ được sắp xếp theo thứ tự tăng dần
    # [1, 5, 7, 10, 11, 13]
    # Số lượng giá trị của tập dữ liệu là 6 (chẵn)
    # => Trung vị = (7 + 10) / 2 = 8.5

    print(median([1, 11, 13, 5, 7]))
    # Đầu tiên tập dữ liệu sẽ được sắp xếp theo thứ tự tăng dần
    # [1, 5, 7, 11, 13]
    # Số lượng giá trị của tập dữ liệu là 5 (lẻ)
    # => Trung vị = 7

# example_median()


def example_median_low():
    # Tìm trung vị nhỏ hơn của tập dữ liệu

    print(median_low([1, 11, 13, 5, 7, 9]))
    # Đầu tiên tập dữ liệu sẽ được sắp xếp theo thứ tự tăng dần
    # [1, 5, 7, 9, 11, 13]
    # Số lượng giá trị của tập dữ liệu là 6 (chẵn)
    # => Trung vị nhỏ hơn = 7

    print(median_low([1, 11, 13, 5, 7]))
    # Đầu tiên tập dữ liệu sẽ được sắp xếp theo thứ tự tăng dần
    # [1, 5, 7, 11, 13]
    # Số lượng giá trị của tập dữ liệu là 5 (lẻ)
    # => Trung vị = 7

# example_median_low()


def example_median_high():
    # Tìm trung vị lớn hơn của tập dữ liệu

    print(median_high([1, 11, 13, 5, 7, 9]))
    # Đầu tiên tập dữ liệu sẽ được sắp xếp theo thứ tự tăng dần
    # [1, 5, 7, 9, 11, 13]
    # Số lượng giá trị của tập dữ liệu là 6 (chẵn)
    # => Trung vị lớn hơn = 9

    print(median_high([1, 11, 13, 5, 7]))
    # Đầu tiên tập dữ liệu sẽ được sắp xếp theo thứ tự tăng dần
    # [1, 5, 7, 11, 13]
    # Số lượng giá trị của tập dữ liệu là 5 (lẻ)
    # => Trung vị = 7

# example_median_high()


def example_median_grouped():
    print(median_grouped([23, 28, 29, 29, 30]))
    print(median_grouped([23, 28, 29, 29, 30], 2))

# example_median_grouped()


def example_mode():
    # Tìm yếu vị của tập dữ liệu

    print(mode([25, 26, 27, 27, 28, 29, 28, 28, 30]))
    # Trong tập dữ liệu, giá trị 28 xuất hiện nhiều nhất với số lần xuất hiện là 3
    # => Yếu vị = 28

    print(mode([25, 26, 27, 27, 27, 28, 29, 28, 28, 30]))
    # Trong tập dữ liệu, giá trị 27 và 28 xuất hiện nhiều nhất với số lần xuất hiện là 3
    # Tuy nhiên chỉ trả về yếu vị đầu tiên trong tập dữ liệu (trong trường hợp này là 27)

    print(mode(["red", "blue", "blue", "red", "green", "red", "red"]))
    # Trong tập dữ liệu, "red" xuất hiện nhiều nhất với số lần xuất hiện là 3
    # Yếu vị là "red"

# example_mode()


def example_multimode():
    # Tìm danh sách các yếu vị của tập dữ liệu

    print(multimode([25, 26, 27, 27, 27, 28, 29, 28, 28, 29, 29, 30]))
    # Trong tập dữ liệu, giá trị 27, 28 và 29 xuất hiện nhiều nhất với số lần xuất hiện là 3
    # Kết quả trả về là 27, 28, 29

    # Tìm yếu vị lớn nhất: 29
    print(max(multimode([25, 26, 27, 27, 27, 28, 29, 28, 28, 29, 29, 30])))

    # Tìm yếu vị nhỏ nhất: 27
    print(min(multimode([25, 26, 27, 27, 27, 28, 29, 28, 28, 29, 29, 30])))

# example_multimode()


def example_quantiles():
    print(quantiles([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], n=4))
    print(quantiles([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], n=10))
    print(quantiles([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], n=20))

# example_quantiles()


def example_pstdev():
    print(pstdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))
    print(pstdev([25, 29, 31, 38, 40]))

# example_pstdev()


def example_pvariance():
    print(pvariance([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))
    print(pvariance([25, 29, 31, 38, 40]))
    print(pvariance([5, 18.6, 4.2, 25.9], mean([5, 18.6, 4.2, 25.9])))

# example_pvariance()


def example_stdev():
    print(stdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))
    print(stdev([25, 29, 31, 38, 40]))

# example_stdev()


def example_variance():
    print(variance([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))
    print(variance([25, 29, 31, 38, 40]))
    print(variance([5, 18.6, 4.2, 25.9], mean([5, 18.6, 4.2, 25.9])))


# example_variance()


def example_covariance():
    x = [1, 3, 5, 9, 8, 7, 6]
    y = [1, 2, 3, 1, 2, 3, 1]
    z = [8, 5, 3, 1, 8, 4, 2]
    print(covariance(x, y))
    print(covariance(x, z))
    print(covariance(y, z))

# example_covariance()


def example_correlation():
    # Ví dụ ta muốn biết hệ số tương quan giữa nhiệt độ trong ngày với doanh thu bán kem
    # nhiệt độ trung bình mỗi ngày trong 3 ngày gần đây, đơn vị độ C
    temp = [35, 30, 25]
    # doanh thu bán kem mỗi ngày trong 3 ngày gần đây, đơn vị $
    revenue = [800, 600, 250]
    print(correlation(temp, revenue))
    # Hệ số tương quan dương có nghĩa là nhiệt độ trung bình trong ngày cao thì lượng người mua kem trong ngày cũng sẽ cao dẫn đến doanh thu bán kem cao vào những ngày này

# example_correlation()


def example_linear_regression():
    # Ví dụ ta muốn dự đoán chiều cao của một người dựa vào số tuổi
    age = [1, 5, 13, 17, 24]
    height = [50, 100, 140, 169, 180]
    slope, intercept = linear_regression(age, height)
    # Ta muốn dự đoán một người 18 tuổi có chiều cao bao nhiêu
    print(round(slope * 18 + intercept))

# example_linear_regression()
