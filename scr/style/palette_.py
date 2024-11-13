GREY = {
    "50": "#fafafa",
    "100": "#f5f5f5",
    "200": "#eeeeee",
    "300": "#e0e0e0",
    "400": "#bdbdbd",
    "500": "#9e9e9e",
    "600": "#757575",
    "700": "#616161",
    "800": "#424242",
    "900": "#212121",
    "A100": "#f5f5f5",
    "A200": "#eeeeee",
    "A400": "#bdbdbd",
    "A700": "#616161"
}

RED = {
    "50": "#FFEBEE",
    "100": "#FFCDD2",
    "200": "#EF9A9A",
    "300": "#E57373",
    "400": "#EF5350",
    "500": "#F44336",
    "600": "#E53935",
    "700": "#D32F2F",
    "800": "#C62828",
    "900": "#B71C1C",
    "A100": "#FF8A80",
    "A200": "#FF5252",
    "A400": "#FF1744",
    "A700": "#D50000"
}

PURPLE = {
    "50": "#EDE7F6",
    "100": "#D1C4E9",
    "200": "#B39DDB",
    "300": "#9575CD",
    "400": "#7E57C2",
    "500": "#673AB7",
    "600": "#5E35B1",
    "700": "#512DA8",
    "800": "#4527A0",
    "900": "#311B92",
    "A100": "#B388FF",
    "A200": "#7C4DFF",
    "A400": "#651FFF",
    "A700": "#6200EA"
}

TEAL = {
    "50": "#E0F2F1",
    "100": "#B2DFDB",
    "200": "#80CBC4",
    "300": "#4DB6AC",
    "400": "#26A69A",
    "500": "#009688",
    "600": "#00897B",
    "700": "#00796B",
    "800": "#00695C",
    "900": "#004D40",
    "A100": "#A7FFEB",
    "A200": "#64FFDA",
    "A400": "#1DE9B6",
    "A700": "#00BFA5"
}

INDIGO = {
    "50": "#E8EAF6",
    "100": "#C5CAE9",
    "200": "#9FA8DA",
    "300": "#7986CB",
    "400": "#5C6BC0",
    "500": "#3F51B5",
    "600": "#3949AB",
    "700": "#303F9F",
    "800": "#283593",
    "900": "#1A237E",
    "A100": "#8C9EFF",
    "A200": "#536DFE",
    "A400": "#3D5AFE",
    "A700": "#304FFE"
}

class palette():
        PRIMARY = {
            "Main": "#4A4A4A",
            "indigo": INDIGO["900"],
            "grey": GREY["900"],
            "red": RED["900"],
            "purple": PURPLE["900"],
            "teal": TEAL["900"],  
            "contrastText": "#FFFFFF",  # Văn bản nổi bật
        }

        SECONDARY = {
            "Main": "#9e9e9e",
            "indigo": INDIGO["500"],
            "grey": GREY["500"],
            "red": RED["500"],
            "purple": PURPLE["500"],
            "teal": TEAL["500"],  
            "contrastText": "#FFFFFF"
        }

        THIRD = {
            "Main": "#ffffff",
            "indigo": INDIGO["200"],
            "grey": GREY["200"],
            "red": RED["200"],
            "purple": PURPLE["200"],
            "teal": TEAL["200"],  
            "contrastText": "#FFFFFF"
        }

        INFO = {
            "main": "#0288d1",
            "light": "#03a9f4",
            "dark": "#01579b",
            "contrastText": "#ffffff"
        }

        SUCCESS = {
            "main": "#2e7d32",
            "light": "#4caf50",
            "dark": "#1b5e20",
            "contrastText": "#ffffff"
        }

        WARNING = {
            "main": "#ed6c02",
            "light": "#ff9800",
            "dark": "#e65100",
            "contrastText": "#ffffff"
        }

        ERROR = {
            "main": "#d32f2f",
            "light": "#ef5350",
            "dark": "#c62828",
            "contrastText": "#ffffff"
        }

        TEXT = {
            "primary": "rgba(0, 0, 0, 0.87)",
            "secondary": "rgba(0, 0, 0, 0.6)",
            "disabled": "rgba(0, 0, 0, 0.38)",
            "divider": "rgba(0, 0, 0, 0.12)"
        }

        BACKGROUND = {
            "paper": "#ffffff",
            "default": "#ffffff"
        }

        ACTION = {
            "active": "rgba(0, 0, 0, 0.54)",
            "hover": "rgba(0, 0, 0, 0.04)",
            "hoverOpacity": 0.04,
            "selected": "rgba(0, 0, 0, 0.08)",
            "selectedOpacity": 0.08,
            "disabled": "rgba(0, 0, 0, 0.26)",
            "disabledBackground": "#00000003",
            "disabledOpacity": 0.38,
            "focus": "rgba(0, 0, 0, 0.12)",
            "focusOpacity": 0.12,
            "activatedOpacity": 0.12
        }
