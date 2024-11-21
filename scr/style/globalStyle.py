
from scr.style.palette_ import palette
# from effects import Shadows, Transitions, Border, Spacing
from scr.style.typography_ import Typography
from scr.style.Breakpoints_ import Breakpoints
from PySide6.QtGui import QColor

class Palette():
    class Primary:
        @staticmethod
        def main():
            return "#4A4A4A"  # Màu chính của Primary

        @staticmethod
        def indigo():
            return palette.PRIMARY["indigo"] # Màu sáng của Primary
        
        @staticmethod
        def grey():
            return palette.PRIMARY["grey"] # Màu sáng của Primary
        
        @staticmethod
        def red():
            return palette.PRIMARY["red"] # Màu sáng của Primary
        
        @staticmethod
        def purple():
            return palette.PRIMARY["purple"] # Màu sáng của Primary
        
        @staticmethod
        def teal():
            return palette.PRIMARY["teal"] # Màu sáng của Primary
        
        @staticmethod
        def contrastText():
            return palette.PRIMARY["contrastText"] # Màu sáng của Primary


    class Secondary:
        @staticmethod
        def main():
            return "#4A4A4A"  # Màu chính của Primary

        @staticmethod
        def indigo():
            return palette.SECONDARY["indigo"] # Màu sáng của Primary
        
        @staticmethod
        def grey():
            return palette.SECONDARY["grey"] # Màu sáng của Primary
        
        @staticmethod
        def red():
            return palette.SECONDARY["red"] # Màu sáng của Primary
        
        @staticmethod
        def purple():
            return palette.SECONDARY["purple"] # Màu sáng của Primary
        
        @staticmethod
        def teal():
            return palette.SECONDARY["teal"] # Màu sáng của Primary
        
        @staticmethod
        def contrastText():
            return palette.SECONDARY["contrastText"] # Màu sáng của Primary
        
    class Third:
        @staticmethod
        def main():
            return "#a8a8a8"  # Màu chính của Primary
        
        @staticmethod
        def indigo():
            return palette.THIRD["indigo"] # Màu sáng của Primary
        
        @staticmethod
        def grey():
            return palette.THIRD["grey"] # Màu sáng của Primary
        
        @staticmethod
        def red():
            return palette.THIRD["red"] # Màu sáng của Primary
        
        @staticmethod
        def purple():
            return palette.THIRD["purple"] # Màu sáng của Primary
        
        @staticmethod
        def teal():
            return palette.THIRD["teal"] # Màu sáng của Primary
        
        @staticmethod
        def contrastText():
            return palette.THIRD["contrastText"] # Màu sáng của Primary
        
    class Four:
        @staticmethod
        def main():
            return "#a8a8a8"  # Màu chính của Primary
        
        @staticmethod
        def indigo():
            return palette.FOUR["indigo"] # Màu sáng của Primary
        
        @staticmethod
        def grey():
            return palette.FOUR["grey"] # Màu sáng của Primary
        
        @staticmethod
        def red():
            return palette.FOUR["red"] # Màu sáng của Primary
        
        @staticmethod
        def purple():
            return palette.FOUR["purple"] # Màu sáng của Primary
        
        @staticmethod
        def teal():
            return palette.FOUR["teal"] # Màu sáng của Primary
        

    class Info:
        @staticmethod
        def main():
            return "#00BCD4"  # Màu chính của Info

        @staticmethod
        def light():
            return "#4DB6AC"  # Màu sáng của Info

        @staticmethod
        def dark():
            return "#00838F"  # Màu tối của Info

        @staticmethod
        def contrast_text():
            return "#FFFFFF"  # Màu văn bản nổi bật trên Info

    class Success:
        @staticmethod
        def main():
            return "#4CAF50"  # Màu chính của Success

        @staticmethod
        def light():
            return "#80E27E"  # Màu sáng của Success

        @staticmethod
        def dark():
            return "#388E3C"  # Màu tối của Success

        @staticmethod
        def contrast_text():
            return "#FFFFFF"  # Màu văn bản nổi bật trên Success

    class Warning:
        @staticmethod
        def main():
            return "#FF9800"  # Màu chính của Warning

        @staticmethod
        def light():
            return "#FFB74D"  # Màu sáng của Warning

        @staticmethod
        def dark():
            return "#F57C00"  # Màu tối của Warning

        @staticmethod
        def contrast_text():
            return "#FFFFFF"  # Màu văn bản nổi bật trên Warning

    class Error:
        @staticmethod
        def main():
            return "#F44336"  # Màu chính của Error

        @staticmethod
        def light():
            return "#E57373"  # Màu sáng của Error

        @staticmethod
        def dark():
            return "#D32F2F"  # Màu tối của Error

        @staticmethod
        def contrast_text():
            return "#FFFFFF"  # Màu văn bản nổi bật trên Error

    class Text:
        @staticmethod
        def fontFamily_roboto():
            return Typography.get_typography()["fontFamily_Roboto"]  # font
        
        @staticmethod
        def fontFamily_serif():
            return Typography.get_typography()["fontFamily_Serif"]  
        
        @staticmethod
        def fontFamily_sans_serif():
            return Typography.get_typography()["fontFamily_Sans-serif"]  

        @staticmethod
        def fontSize():
            return Typography.get_typography()["fontSize"]  # Màu văn bản phụ

        @staticmethod
        def fontWeightLight():
            return Typography.get_typography()["fontWeightLight"]  # Màu văn bản phụ

        @staticmethod
        def fontWeightRegular():
            return Typography.get_typography()["fontWeightRegular"]  # Màu gợi ý văn bản

        @staticmethod
        def fontWeightMedium():
            return Typography.get_typography()["fontWeightMedium"]  # Màu gợi ý văn bản

        @staticmethod
        def fontWeightBold():
            return Typography.get_typography()["fontWeightBold"]  # Màu gợi ý văn bản

        @staticmethod
        def fontWeightExtra():
            return Typography.get_typography()["fontWeightExtra"]  # Màu gợi ý văn bản

    class Background:
        @staticmethod
        def default():
            return "#FFFFFF"  # Màu nền mặc định

        @staticmethod
        def paper():
            return "#FAFAFA"  # Màu nền cho các phần tử giấy

    class Action:
        @staticmethod
        def active():
            return "#1976D2"  # Màu chính khi hoạt động

        @staticmethod
        def disabled():
            return palette.ACTION()["disabled"]  # Màu khi vô hiệu hóa

        @staticmethod
        def disabledBackground():
            return palette.ACTION()["disabledBackground"]  # Màu khi vô hiệu hóa

        @staticmethod
        def hover(primary_color):
            color = QColor(primary_color)  # Tạo đối tượng QColor từ mã màu chính
            hover_color = color.lighter(140).name()  # Làm sáng 30% cho màu hover

            return hover_color

        @staticmethod
        def press(primary_color):
            color = QColor(primary_color)  # Tạo đối tượng QColor từ mã màu chính
            pressed_color = color.darker(110).name()  # Làm tối 20% cho màu pressed

            return pressed_color
