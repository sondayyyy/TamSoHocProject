# breakpoints.py

class Breakpoints:
    def __init__(self):
        self.keys = ["xs", "sm", "md", "lg", "xl"]
        self.values = {
            "xs": 0,
            "sm": 600,
            "md": 900,
            "lg": 1200,
            "xl": 1536,
        }
        self.unit = "px"
        self.direction = "ltr"

    def up(self, key):
        return f"(min-width: {self.values[key]}{self.unit})"

    def down(self, key):
        return f"(max-width: {self.values[key]}{self.unit})"

    def between(self, start, end):
        return f"(min-width: {self.values[start]}{self.unit}) and (max-width: {self.values[end]}{self.unit})"

    def only(self, key):
        keys = self.keys
        idx = keys.index(key)
        if idx == len(keys) - 1:
            return f"(min-width: {self.values[key]}{self.unit})"
        return f"(min-width: {self.values[key]}{self.unit}) and (max-width: {self.values[keys[idx + 1]]}{self.unit})"

    def not_(self, key):
        return f"(not all and (max-width: {self.values[key]}{self.unit}))"

    def container_queries(self, size):
        # Logic for container queries can be implemented here
        return f"Container queries for size: {size}"

    def apply_styles(self, element, styles):
        # Simulate applying styles to an element
        for property, value in styles.items():
            setattr(element, property, value)

"""
# Sử dụng
breakpoints = Breakpoints()
print(breakpoints.up("sm"))  # Kết quả: "(min-width: 600px)"
print(breakpoints.between("sm", "lg"))  # Kết quả: "(min-width: 600px) and (max-width: 1200px)"


# Giả lập một đối tượng element
class Element:
    pass

element = Element()
styles = {'background_color': 'blue', 'font_size': '14px'}
breakpoints.apply_styles(element, styles)
print(element.__dict__)  # Kết quả: {'background_color': 'blue', 'font_size': '14px'}
"""