# LIGHTTHEME.PY
from scr import Palette, palette


class LightTheme:

    class ColorBase:
        @staticmethod
        def hover(color):
            hover = Palette.Action.hover(color)
            return hover
        def press(color):
            press = Palette.Action.press(color)
            return press
        
    class Primary:
        @staticmethod
        def main():
            return Palette.Primary.main()
        
        @staticmethod
        def main_hover():
            return LightTheme.ColorBase.hover(Palette.Primary.main())  # Gọi hover từ ColorBase

        @staticmethod
        def main_press():
            return LightTheme.ColorBase.press(Palette.Primary.main())  # Gọi press từ ColorBase        
        

        @staticmethod
        def indigo():
            return Palette.Primary.indigo()
        
        @staticmethod
        def indigo_hover():
            return LightTheme.ColorBase.hover(Palette.Primary.indigo())  # Gọi hover từ ColorBase

        @staticmethod
        def indigo_press():
            return LightTheme.ColorBase.press(Palette.Primary.indigo())  # Gọi press từ ColorBase
                

        @staticmethod
        def grey():
            return Palette.Primary.grey()
        
        @staticmethod
        def grey_hover():
            return LightTheme.ColorBase.hover(Palette.Primary.grey())  # Gọi hover từ ColorBase

        @staticmethod
        def grey_press():
            return LightTheme.ColorBase.press(Palette.Primary.grey())
        

        @staticmethod
        def red():
            return Palette.Primary.red()
        
        @staticmethod
        def red_hover():
            return LightTheme.ColorBase.hover(Palette.Primary.red())  # Gọi hover từ ColorBase

        @staticmethod
        def red_press():
            return LightTheme.ColorBase.press(Palette.Primary.red())
                

        @staticmethod
        def purple():
            return Palette.Primary.purple()
        
        @staticmethod
        def purple_hover():
            return LightTheme.ColorBase.hover(Palette.Primary.purple())  # Gọi hover từ ColorBase

        @staticmethod
        def purple_press():
            return LightTheme.ColorBase.press(Palette.Primary.purple())
                
        @staticmethod
        def teal():
            return Palette.Primary.teal()
        
        @staticmethod
        def teal_hover():
            return LightTheme.ColorBase.hover(Palette.Primary.teal())  # Gọi hover từ ColorBase

        @staticmethod
        def teal_press():
            return LightTheme.ColorBase.press(Palette.Primary.teal())
        
    class Secondary:
        @staticmethod
        def main():
            return Palette.Secondary.main()
        
        @staticmethod
        def main_hover():
            return LightTheme.ColorBase.hover(Palette.Secondary.main())  # Gọi hover từ ColorBase

        @staticmethod
        def main_press():
            return LightTheme.ColorBase.press(Palette.Secondary.main())  # Gọi press từ ColorBase        
        

        @staticmethod
        def indigo():
            return Palette.Secondary.indigo()
        
        @staticmethod
        def indigo_hover():
            return LightTheme.ColorBase.hover(Palette.Secondary.indigo())  # Gọi hover từ ColorBase

        @staticmethod
        def indigo_press():
            return LightTheme.ColorBase.press(Palette.Secondary.indigo())  # Gọi press từ ColorBase
                

        @staticmethod
        def grey():
            return Palette.Secondary.grey()
        
        @staticmethod
        def grey_hover():
            return LightTheme.ColorBase.hover(Palette.Secondary.grey())  # Gọi hover từ ColorBase

        @staticmethod
        def grey_press():
            return LightTheme.ColorBase.press(Palette.Secondary.grey())
        

        @staticmethod
        def red():
            return Palette.Secondary.red()
        
        @staticmethod
        def red_hover():
            return LightTheme.ColorBase.hover(Palette.Secondary.red())  # Gọi hover từ ColorBase

        @staticmethod
        def red_press():
            return LightTheme.ColorBase.press(Palette.Secondary.red())
                

        @staticmethod
        def purple():
            return Palette.Secondary.purple()
        
        @staticmethod
        def purple_hover():
            return LightTheme.ColorBase.hover(Palette.Secondary.purple())  # Gọi hover từ ColorBase

        @staticmethod
        def purple_press():
            return LightTheme.ColorBase.press(Palette.Secondary.purple())
                

        @staticmethod
        def teal():
            return Palette.Secondary.teal()
        
        @staticmethod
        def teal_hover():
            return LightTheme.ColorBase.hover(Palette.Secondary.teal())  # Gọi hover từ ColorBase

        @staticmethod
        def teal_press():
            return LightTheme.ColorBase.press(Palette.Secondary.teal())
        
    class Third:
        @staticmethod
        def main():
            return Palette.Third.main()
        
        @staticmethod
        def main_hover():
            return LightTheme.ColorBase.hover(Palette.Third.main())  # Gọi hover từ ColorBase

        @staticmethod
        def main_press():
            return LightTheme.ColorBase.press(Palette.Third.main())  # Gọi press từ ColorBase        
        

        @staticmethod
        def indigo():
            return Palette.Third.indigo()
        
        @staticmethod
        def indigo_hover():
            return LightTheme.ColorBase.hover(Palette.Third.indigo())  # Gọi hover từ ColorBase

        @staticmethod
        def indigo_press():
            return LightTheme.ColorBase.press(Palette.Third.indigo())  # Gọi press từ ColorBase
                

        @staticmethod
        def grey():
            return Palette.Third.grey()
        
        @staticmethod
        def grey_hover():
            return LightTheme.ColorBase.hover(Palette.Third.grey())  # Gọi hover từ ColorBase

        @staticmethod
        def grey_press():
            return LightTheme.ColorBase.press(Palette.Third.grey())
        

        @staticmethod
        def red():
            return Palette.Third.red()
        
        @staticmethod
        def red_hover():
            return LightTheme.ColorBase.hover(Palette.Third.red())  # Gọi hover từ ColorBase

        @staticmethod
        def red_press():
            return LightTheme.ColorBase.press(Palette.Third.red())
                
        @staticmethod
        def purple():
            return Palette.Third.purple()
        
        @staticmethod
        def purple_hover():
            return LightTheme.ColorBase.hover(Palette.Third.purple())  # Gọi hover từ ColorBase

        @staticmethod
        def purple_press():
            return LightTheme.ColorBase.press(Palette.Third.purple())
                
        @staticmethod
        def teal():
            return Palette.Third.teal()
        
        @staticmethod
        def teal_hover():
            return LightTheme.ColorBase.hover(Palette.Third.teal())  # Gọi hover từ ColorBase

        @staticmethod
        def teal_press():
            return LightTheme.ColorBase.press(Palette.Third.teal())
         
        
    class Background:
        @staticmethod
        def light():    
            color = "#ffffff"
            return color
        
    class Text:
        @staticmethod
        def white():    
            color = "#ffffff"
            return color



    @staticmethod
    def get_stylesheet():
        return f"""
        QWidget {{
            background-color: {LightTheme.Background.light()};
            color: {LightTheme.Primary.main()};
        }}

        QPushButton {{
            background-color: {LightTheme.Primary.main()};
            color: {LightTheme.Text.white()};
            border: 1px solid {LightTheme.Primary.main()};
            font-style: normal;
            font-weight: {Palette.Text.fontWeightRegular()};
            font-size: {Palette.Text.fontSize()};
            font-family: {Palette.Text.fontFamily_sans_serif()};
            padding: 8px 16px;
            border-radius: 8px;
            text-align: center;
        }}

        QPushButton:hover {{
            background-color: {LightTheme.Primary.main_hover()};
            border-color: {LightTheme.Primary.main()};
            color: {LightTheme.Text.white()};
        }}

        QPushButton:pressed {{
            background-color: {LightTheme.Primary.main_press()};
            border-color: {LightTheme.Primary.main()};
            color: {LightTheme.Text.white()};
        }}
        """