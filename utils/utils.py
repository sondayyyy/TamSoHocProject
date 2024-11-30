import unicodedata

def get_tamsohoc_result(name, day, month, year, hour): #hàm kích hoạt kết quả
    result = calculate_main_number(day, month, year)  # kết quả từ hàm tính toán số chủ đạo
    tong_bandau = result['tong_bandau']
    so_chu_dao = result['so_chu_dao']
    tong2_so_chu_dao = result['tong_2_so_chu_dao']
    tong2_so_chu_dao_cu = result['tong_2_so_chu_dao_cu']

    dob_string = str(day) + str(month) + str(year)  # Chuyển đổi tất cả thành chuỗi trước khi nối

    y1 = int(str(year)[0])
    y2 = int(str(year)[1])
    y3 = int(str(year)[2])
    y4 = int(str(year)[3])

    la_trong = 0
    la_ngoai = 0

    if tong_bandau < 10:
        la_trong = 0
        la_ngoai = so_chu_dao
    elif so_chu_dao < 11:
        la_trong = tong2_so_chu_dao_cu // 10
        la_ngoai = tong2_so_chu_dao_cu % 10
    else:
        la_trong = so_chu_dao // 10
        la_ngoai = so_chu_dao % 10

    la_trong_result = generate_main_number_table(la_trong, dob_string)
    la_ngoai_result = generate_main_number_table(la_ngoai, dob_string)

    la_so_an = calculate_latest_number(
        la_trong_result['center_number'] + la_ngoai_result['center_number']
        if la_trong_result and la_ngoai_result else 0
    )

    la_so_uc_che = calculate_latest_number(
        la_ngoai_result['center_number'] - la_trong_result['center_number']
        if la_trong_result and la_ngoai_result else 0
    )

    la_tuoi_tho = calculate_latest_number(y1 + y2 + y3 + y4)
    la_thanh_thieu_nien = calculate_latest_number(y1 + y2 + y3 + y4 + int(month))
    la_truong_thanh = calculate_latest_number(y1 + y2 + y3 + y4 + int(month) + int(day))
    la_hau_van = calculate_latest_number(
        y1 + y2 + y3 + y4 + int(month) + int(day) + int(hour or 0))

    tuoi_chuyen_hau_van = 36 - tong2_so_chu_dao

    ngu_hanh = calculate_latest_number(so_chu_dao)

    cung_ngu_hanh = get_cung_ngu_hanh(ngu_hanh)

    sinh_ra = get_sinh_ra(tong2_so_chu_dao)
    sinh_ra_phu = get_cung_ngu_hanh(sinh_ra)

    duoc_sinh = get_duoc_sinh(tong2_so_chu_dao)
    duoc_sinh_phu = get_cung_ngu_hanh(duoc_sinh)

    bi_khac = get_bi_khac(tong2_so_chu_dao) or 0
    bi_khac_phu = get_cung_ngu_hanh(bi_khac)

    khac = get_khac(tong2_so_chu_dao) or 0
    khac_phu = get_cung_ngu_hanh(khac)

    ban_so_theo_ten = get_name_number(name)

    return {
        'tong_bandau': tong_bandau,
        'so_chu_dao': so_chu_dao,
        'tong2_so_chu_dao': tong2_so_chu_dao,
        'tong2_so_chu_dao_cu': tong2_so_chu_dao_cu,
        'la_trong': la_trong,
        'la_ngoai': la_ngoai,
        'la_so_an': la_so_an,
        'la_so_uc_che': la_so_uc_che,
        'la_tuoi_tho': la_tuoi_tho,
        'la_thanh_thieu_nien': la_thanh_thieu_nien,
        'la_truong_thanh': la_truong_thanh,
        'la_hau_van': la_hau_van,
        'tuoi_chuyen_hau_van': tuoi_chuyen_hau_van,
        'ngu_hanh': ngu_hanh,
        'cung_ngu_hanh': cung_ngu_hanh,
        'sinh_ra': sinh_ra,
        'sinh_ra_phu': sinh_ra_phu,
        'duoc_sinh': duoc_sinh,
        'duoc_sinh_phu': duoc_sinh_phu,
        'bi_khac': bi_khac,
        'bi_khac_phu': bi_khac_phu,
        'khac': khac,
        'khac_phu': khac_phu,
        'ban_so_theo_ten': ban_so_theo_ten
    }


def calculate_main_number(day: str, month: str, year: str):  # logic tính toán số chủ đạo
    tong_bandau = (
        int(day)
        + int(month)
        + int(str(year)[0])
        + int(str(year)[1])
        + int(str(year)[2])
        + int(str(year)[3])
    )  # Tổng ban đầu, ví dụ 09+12+2+0+0+2 = 25

    so_chu_dao = tong_bandau  # Gọi số chủ đạo = tổng ban đầu

    tong_2_so_chu_dao_cu = tong_bandau  # Gọi tổng 2 số chủ đạo cũ = tổng ban đầu

    # Nếu số chủ đạo lớn hơn 9 và các chữ số không giống nhau, cộng lại
    if so_chu_dao > 9 and str(so_chu_dao)[0] != str(so_chu_dao)[1] and so_chu_dao % 10 != 0:
        so_chu_dao = sum_number_itself(so_chu_dao)
        tong_2_so_chu_dao_cu = sum_number_itself(tong_bandau)

    if so_chu_dao > 9:
        so_chu_dao = sum_number_itself(so_chu_dao)

    tong_2_so_chu_dao = sum_number_itself(so_chu_dao) if so_chu_dao > 9 else so_chu_dao

    return {
        "tong_bandau": tong_bandau,
        "so_chu_dao": so_chu_dao,
        "tong_2_so_chu_dao_cu": tong_2_so_chu_dao_cu,
        "tong_2_so_chu_dao": tong_2_so_chu_dao,
    }


def calculate_latest_number(number): #có vẻ các giá trị này cần thay đổi
    result = number
    if number <= 9:
        return result
    if str(number)[0] == str(number)[1]:
        return result
    if number % 10 == 0:
        return result

    return sum_number_itself(sum_number_itself(number))


def sum_number_itself(n): #Hàm tính tổng từng giá trị số 
    return sum(int(digit) for digit in str(n))


def get_row_values(center_number): #Hàm tính toán vị trí giá trị 1 hàng dọc
    left_range_numbers = [1, 4, 7]
    right_range_numbers = [3, 6, 9]

    return [
        center_number + 2 if center_number in left_range_numbers else center_number - 1,
        center_number,
        center_number - 2 if center_number in right_range_numbers else center_number + 1,
    ]


def generate_main_number_table(center_number_init, dob_string): 
    result = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    first_number = abs(center_number_init) // 10 #số đầu chia 10 bỏ dư
    second_number = abs(center_number_init) % 10 #số 2 chia 10 lấy dư

    center_number_to_cal = first_number + second_number #số cần tính là tổng 2 số
    center_number_to_display = int(center_number_init) #số hiển thị lấy giá trị đầu tiên

    if center_number_init < 0: 
        center_number_to_cal = abs(center_number_to_cal) 
    elif center_number_init == 0 or center_number_to_display % 10 == 0:
        center_number_to_cal = int(str(center_number_to_display)[0])

    result[0] = get_row_values(
        center_number_to_cal - 3 if center_number_to_cal -
        3 >= 1 else center_number_to_cal + 6
    ) 
    result[1] = get_row_values(center_number_to_cal)
    result[2] = get_row_values(
        center_number_to_cal + 3 if center_number_to_cal +
        3 <= 9 else center_number_to_cal - 6
    )
    #giá trị được truyền vào từ hàm get_row_values để tính toán vị trí 3 hàng ngang

    result = [
        [duplicate_number(col, dob_string) for col in row]
        for row in result
    ]#chưa hiểu cách kết quả hoạt động

    main_number_duplicate = duplicate_number(
        center_number_to_cal if center_number_init != 0 else 0,
        dob_string
    ) #hàm đếm lần lặp

    center_number_display = str(center_number_to_display)
    if main_number_duplicate:
        center_number_display += f", {main_number_duplicate}"

    result[1][1] = center_number_display

    return {"result": result, "center_number": sum_number_itself(center_number_display.replace(', ', ''))}


def duplicate_number(value, parent_str, default_number=None):
    count = parent_str.count(str(value))

    if count < 1 and value == default_number:
        return default_number
    if count < 1:
        return None
    if value == 0:
        print({"count": count})

    return str(value) * count


def get_sinh_ra(number):
    if number == 7:
        return 5
    return number - 7 if number > 7 else number + 3


def get_duoc_sinh(number):
    if number == 3:
        return 5
    return number + 7 if number < 3 else number - 3


def get_bi_khac(number):
    if number == -4:
        return 3
    if number == 9:
        return -8
    if number == -2:
        return 1
    if number == 7:
        return -6
    if number == 5:
        return -4
    if number == 0:
        return 9
    if number == 3:
        return -2
    if number == -8:
        return 7
    if number == 1:
        return 0
    if number == -6:
        return 5


def get_khac(number):
    if number == -4:
        return 5
    if number == 9:
        return 0
    if number == -2:
        return 3
    if number == 7:
        return -8
    if number == 5:
        return -6
    if number == 0:
        return 1
    if number == 3:
        return -4
    if number == -8:
        return 9
    if number == 1:
        return -2
    if number == -6:
        return 7


def get_cung_ngu_hanh(number):
    return number - 5 if number >= 5 else number + 5


def get_am_duong_ngu_hanh(ngu_hanh):
    return '-' if abs(int(ngu_hanh)) % 2 == 0 else '+'


def get_ten_ngu_hanh(ngu_hanh):
    ngu_hanh_str = str(ngu_hanh)
    if '4' in ngu_hanh_str or '9' in ngu_hanh_str:
        return 'Kim'
    if '2' in ngu_hanh_str or '7' in ngu_hanh_str:
        return 'Thuỷ'
    if '3' in ngu_hanh_str or '8' in ngu_hanh_str:
        return 'Hoả'
    if '1' in ngu_hanh_str or '6' in ngu_hanh_str:
        return 'Thổ'
    return 'Mộc'


def generate_ngu_hanh_am_duong(ngu_hanh, parent_str):
    duplicate_ngu_hanh = duplicate_number(ngu_hanh, parent_str)

    if not duplicate_ngu_hanh:
        return ''

    return f"{duplicate_ngu_hanh} {get_am_duong_ngu_hanh(ngu_hanh)}({get_ten_ngu_hanh(ngu_hanh)})"


def get_name_number(name):
    name = remove_accents(name).replace(' ', '').lower()
    return sum(ban_so_theo_ten_mapping.get(letter, 0) for letter in name)


def get_name_number_string(name):
    name = remove_accents(name).replace(' ', '').lower()
    result = ''
    for letter in name:
        result += str(ban_so_theo_ten_mapping.get(letter, ''))
    return result


def remove_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


ban_so_theo_ten_mapping = {
    'a': 1, 'h': 1, 'q': 1, 'x': 1,
    'b': 2, 'i': 2, 'r': 2, 'y': 2,
    'c': 3, 'j': 3, 's': 3, 'z': 3,
    'd': 4, 'k': 4,
    'e': 5, 'l': 5, 't': 5,
    'f': 6, 'm': 6, 'u': 6,
    'g': 7, 'n': 7, 'v': 7,
    'o': 8, 'w': 8,
    'p': 9
}
