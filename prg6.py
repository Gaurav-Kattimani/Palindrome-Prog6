import sys
if len(sys.argv) == 1:
    text = "121"   
else:
    text = sys.argv[1]
    
text_lower = text.lower()
reversed_text = text_lower[::-1]

if text_lower == reversed_text:
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")
