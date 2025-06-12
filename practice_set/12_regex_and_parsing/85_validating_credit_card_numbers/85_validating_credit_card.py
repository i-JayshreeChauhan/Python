import re

pattern = r"^(?:[456][0-9]{15}|[456][0-9]{3}(?:-[0-9]{4}){3})$"


def is_valid_card(card):

    # 1. Match structure (either 16 digits or grouped with hyphens)
    pattern = r"^(?:[456]\d{15}|[456]\d{3}(?:-\d{4}){3})$"
    if not re.fullmatch(pattern, card):
        return False   
    
    # 2. Remove hyphens (if any) for further checks
    clean_card = card.replace('-', '')

    # 3. Check for 4 or more repeated digits in a row
    if re.search(r"(\d)\1{3,}", clean_card):
        return False
    
    return True




for _ in range(int(input())):
    card = input()
    if is_valid_card(card):
        print("Valid")
    else:
        print("Invalid")

    
