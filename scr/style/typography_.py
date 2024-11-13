class Typography:
    def __init__(self):
        self.htmlFontSize = 16

    def px_to_rem(self, px):
        return f"{px / 16}rem"  # Hàm chuyển đổi pixel sang rem

    def get_typography():
        return {
            'fontFamily_Roboto': '"Roboto", "Helvetica", "Arial", sans-serif',
            'fontFamily_Serif': '"Times New Roman", "Georgia", "Palatino", "Baskerville"',
            'fontFamily_Sans-serif': '"Arial", "Arial Black", "Verdana", "Tahoma", "Impact", "Gill Sans"',
            'fontSize': 14,
            'fontWeightLight': 300,
            'fontWeightRegular': 400,
            'fontWeightMedium': 500,
            'fontWeightBold': 700,
            'fontWeightExtra': 900,

            
            'h1': {
                'fontFamily': '"Roboto", "Helvetica", "Arial", sans-serif',
                'fontWeight': 300,
                'fontSize': "6rem",
                'lineHeight': 1.167,
                'letterSpacing': "-0.01562em",
            },
            'h2': {
                'fontFamily': '"Roboto", "Helvetica", "Arial", sans-serif',
                'fontWeight': 300,
                'fontSize': "3.75rem",
                'lineHeight': 1.2,
                'letterSpacing': "-0.00833em",
            },
            'h3': {
                'fontFamily': '"Roboto", "Helvetica", "Arial", sans-serif',
                'fontWeight': 400,
                'fontSize': "3rem",
                'lineHeight': 1.167,
                'letterSpacing': "0em",
            },
            'h4': {
                'fontFamily': '"Roboto", "Helvetica", "Arial", sans-serif',
                'fontWeight': 400,
                'fontSize': "2.125rem",
                'lineHeight': 1.235,
                'letterSpacing': "0.00735em",
            },
            'h5': {
                'fontFamily': '"Roboto", "Helvetica", "Arial", sans-serif',
                'fontWeight': 400,
                'fontSize': "1.5rem",
                'lineHeight': 1.334,
                'letterSpacing': "0em",
            },
            'h6': {
                'fontFamily': '"Roboto", "Helvetica", "Arial", sans-serif',
                'fontWeight': 500,
                'fontSize': "1.25rem",
                'lineHeight': 1.6,
                'letterSpacing': "0.0075em",
            },
            'subtitle1': {
                'fontFamily': '"Roboto", "Helvetica", "Arial", sans-serif',
                'fontWeight': 400,
                'fontSize': "1rem",
                'lineHeight': 1.75,
                'letterSpacing': "0.00938em",
                
            },
            'subtitle2': {
                'fontFamily': '"Roboto", "Helvetica", "Arial", sans-serif',
                'fontWeight': 500,
                'fontSize': "0.875rem",
                'lineHeight': 1.57,
                'letterSpacing': "0.00714em",
            },
            'body1': {
                'fontFamily': '"Roboto", "Helvetica", "Arial", sans-serif',
                'fontWeight': 400,
                'fontSize': "1rem",
                'lineHeight': 1.5,
                'letterSpacing': "0.00938em",
            },
            'body2': {
                'fontFamily': '"Roboto", "Helvetica", "Arial", sans-serif',
                'fontWeight': 400,
                'fontSize': "0.875rem",
                'lineHeight': 1.43,
                'letterSpacing': "0.01071em",
            },
            'button': {
                'fontFamily': '"Roboto", "Helvetica", "Arial", sans-serif',
                'fontWeight': 500,
                'fontSize': "0.875rem",
                'lineHeight': 1.75,
                'letterSpacing': "0.02857em",
                'textTransform': "uppercase",
            },
            'caption': {
                'fontFamily': '"Roboto", "Helvetica", "Arial", sans-serif',
                'fontWeight': 400,
                'fontSize': "0.75rem",
                'lineHeight': 1.66,
                'letterSpacing': "0.03333em",
            },
            'overline': {
                'fontFamily': '"Roboto", "Helvetica", "Arial", sans-serif',
                'fontWeight': 400,
                'fontSize': "0.75rem",
                'lineHeight': 2.66,
                'letterSpacing': "0.08333em",
                'textTransform': "uppercase",
            },
            'inherit': {
                'fontFamily': "inherit",
                'fontWeight': "inherit",
                'fontSize': "inherit",
                'lineHeight': "inherit",
                'letterSpacing': "inherit",
            },
        }
