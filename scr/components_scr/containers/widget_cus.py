from PySide6.QtWidgets import QWidget

class CustomWidget(QWidget):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent)
        self.setStyleSheet(self.get_stylesheet(**kwargs))

    @staticmethod
    def get_stylesheet(
        bg_color=None,
        border_color=None,
        border_width=None,
        border_radius=None,
        padding=None,
        margin=None,
    ):
        # Gán giá trị mặc định
        bg_color = bg_color or "#transparent"
        border_color = border_color or "#transparent"
        border_width = border_width or 1
        border_radius = border_radius or 10
        padding = padding or "0px"
        margin = margin or "0px"

        return f"""
        QWidget {{
            background-color: {bg_color};
            border: {border_width}px solid {border_color};
            border-radius: {border_radius}px;
            padding: {padding};
            margin: {margin};
        }}
        """