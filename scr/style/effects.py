
# shadows | Shape | Spacing | Transitions
class Shadows:
    def __init__(self):
        self.Shadows = {
            "none": "none",
            "z1": "0px 2px 1px -1px rgba(0,0,0,0.2), 0px 1px 1px 0px rgba(0,0,0,0.14), 0px 1px 3px 0px rgba(0,0,0,0.12)",
            "z2": "0px 3px 1px -2px rgba(0,0,0,0.2), 0px 2px 2px 0px rgba(0,0,0,0.14), 0px 1px 5px 0px rgba(0,0,0,0.12)",
            "z3": "0px 3px 3px -2px rgba(0,0,0,0.2), 0px 3px 4px 0px rgba(0,0,0,0.14), 0px 1px 8px 0px rgba(0,0,0,0.12)",
            "z4": "0px 2px 4px -1px rgba(0,0,0,0.2), 0px 4px 5px 0px rgba(0,0,0,0.14), 0px 1px 10px 0px rgba(0,0,0,0.12)",
            "z5": "0px 3px 5px -1px rgba(0,0,0,0.2), 0px 5px 8px 0px rgba(0,0,0,0.14), 0px 1px 14px 0px rgba(0,0,0,0.12)",
            "z6": "0px 3px 5px -1px rgba(0,0,0,0.2), 0px 6px 10px 0px rgba(0,0,0,0.14), 0px 1px 18px 0px rgba(0,0,0,0.12)",
            "z7": "0px 4px 5px -2px rgba(0,0,0,0.2), 0px 7px 10px 1px rgba(0,0,0,0.14), 0px 2px 16px 1px rgba(0,0,0,0.12)",
            "z8": "0px 5px 5px -3px rgba(0,0,0,0.2), 0px 8px 10px 1px rgba(0,0,0,0.14), 0px 3px 14px 2px rgba(0,0,0,0.12)",
            "z9": "0px 5px 6px -3px rgba(0,0,0,0.2), 0px 9px 12px 1px rgba(0,0,0,0.14), 0px 3px 16px 2px rgba(0,0,0,0.12)",
            "z10": "0px 6px 6px -3px rgba(0,0,0,0.2), 0px 10px 14px 1px rgba(0,0,0,0.14), 0px 4px 18px 3px rgba(0,0,0,0.12)",
            "z11": "0px 6px 7px -4px rgba(0,0,0,0.2), 0px 11px 15px 1px rgba(0,0,0,0.14), 0px 4px 20px 3px rgba(0,0,0,0.12)",
            "z12": "0px 7px 8px -4px rgba(0,0,0,0.2), 0px 12px 17px 2px rgba(0,0,0,0.14), 0px 5px 22px 4px rgba(0,0,0,0.12)",
            "z13": "0px 7px 8px -4px rgba(0,0,0,0.2), 0px 13px 19px 2px rgba(0,0,0,0.14), 0px 5px 24px 4px rgba(0,0,0,0.12)",
            "z14": "0px 7px 9px -4px rgba(0,0,0,0.2), 0px 14px 21px 2px rgba(0,0,0,0.14), 0px 5px 26px 4px rgba(0,0,0,0.12)",
            "z15": "0px 8px 9px -5px rgba(0,0,0,0.2), 0px 15px 22px 2px rgba(0,0,0,0.14), 0px 6px 28px 5px rgba(0,0,0,0.12)",
            "z16": "0px 8px 10px -5px rgba(0,0,0,0.2), 0px 16px 24px 2px rgba(0,0,0,0.14), 0px 6px 30px 5px rgba(0,0,0,0.12)",
            "z17": "0px 8px 11px -5px rgba(0,0,0,0.2), 0px 17px 26px 2px rgba(0,0,0,0.14), 0px 6px 32px 5px rgba(0,0,0,0.12)",
            "z18": "0px 9px 11px -5px rgba(0,0,0,0.2), 0px 18px 28px 2px rgba(0,0,0,0.14), 0px 7px 34px 6px rgba(0,0,0,0.12)",
            "z19": "0px 9px 12px -6px rgba(0,0,0,0.2), 0px 19px 29px 2px rgba(0,0,0,0.14), 0px 7px 36px 6px rgba(0,0,0,0.12)",
            "z20": "0px 10px 13px -6px rgba(0,0,0,0.2), 0px 20px 31px 3px rgba(0,0,0,0.14), 0px 8px 38px 7px rgba(0,0,0,0.12)",
            "z21": "0px 10px 13px -6px rgba(0,0,0,0.2), 0px 21px 33px 3px rgba(0,0,0,0.14), 0px 8px 40px 7px rgba(0,0,0,0.12)",
            "z22": "0px 10px 14px -6px rgba(0,0,0,0.2), 0px 22px 35px 3px rgba(0,0,0,0.14), 0px 8px 42px 7px rgba(0,0,0,0.12)",
            "z23": "0px 11px 14px -7px rgba(0,0,0,0.2), 0px 23px 36px 3px rgba(0,0,0,0.14), 0px 9px 44px 8px rgba(0,0,0,0.12)",
            "z24": "0px 11px 15px -7px rgba(0,0,0,0.2), 0px 24px 38px 3px rgba(0,0,0,0.14), 0px 9px 46px 8px rgba(0,0,0,0.12)"
        }
    
    def get_shadow(self, key):
        """Trả về giá trị bóng đổ cho key đã cho."""
        return self.shadows.get(key, "Shadow not found")

    def add_shadow(self, key, value):
        """Thêm bóng đổ mới vào từ điển."""
        self.shadows[key] = value
"""
# Ví dụ truy cập vào các giá trị
shadows = Shadows()
print("Shadow 'none':", shadows.get_shadow("none"))
print("Shadow 'z1':", shadows.get_shadow("z1"))
"""



class Border:
    def __init__(self, border_radius=4):
        self.border = {
            'borderRadius': border_radius
        }
'''
# Sử dụng
Border = Border()
print(Border.border['borderRadius'])  # Kết quả: 4
'''

class Spacing:
    def __init__(self, spacing=8):
        self.spacing = spacing

    def spacing_func(self, n):
        return f"{n * self.spacing}px"

'''
# Sử dụng
Spacing = Spacing()
print(Spacing.spacing_func(2))  # Kết quả: '16px'
print(Spacing.spacing_func(3))  # Kết quả: '24px'
'''

class Transitions:
    def __init__(self):
        self.duration = {
            'shortest': 150,
            'shorter': 200,
            'short': 250,
            'standard': 300,
            'complex': 375,
            'enteringScreen': 225,
            'leavingScreen': 195,
        }
        self.easing = {
            'easeInOut': "cubic-bezier(0.4, 0, 0.2, 1)",
            'easeOut': "cubic-bezier(0.0, 0, 0.2, 1)",
            'easeIn': "cubic-bezier(0.4, 0, 1, 1)",
            'sharp': "cubic-bezier(0.4, 0, 0.6, 1)",
        }

    def get_auto_height_duration(self):
        # Hàm giả lập cho auto height duration, có thể thay đổi tùy ý
        return self.duration['standard']

    def create(self):
        # Hàm giả lập cho việc tạo transition, có thể tùy chỉnh thêm
        return {
            'duration': self.duration,
            'easing': self.easing,
        }

'''
# Ví dụ sử dụng
transitions = Transitions()
print("Auto Height Duration:", transitions.get_auto_height_duration())
print("Transition Duration Standard:", transitions.create()['duration']['standard'])
print("Easing EaseIn:", transitions.create()['easing']['easeIn'])
'''