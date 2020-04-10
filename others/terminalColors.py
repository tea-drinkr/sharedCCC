class Colortext:
    ENDC = '\033[m'  # reset to the defaults
    # colors below
    RED = '\033[31m'  # Red text
    GREEN = '\033[32m'  # Green Text
    YELLOW = '\033[33m'  # Yellow text
    BLUE = '\033[34m'  # Blue text
    CYAN = '\033[36m'  # bight blue text
    # text styles below
    RED_bold = '\033[1;31m'  # Red bold text
    GREEN_bold = '\033[1;32m'  # Green bold Text
    YELLOW_bold = '\033[1;33m'  # Yellow bold text
    BLUE_bold = '\033[1;34m'  # Blue bold text
    CYAN_bold = '\033[1;36m'  # brright blue bold text
    # flashing text
    FLASH = '\33[5m'
# Format: (color goes here + "your code" + ENDC)