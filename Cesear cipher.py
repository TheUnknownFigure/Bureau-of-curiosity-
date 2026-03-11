# Caesar Cipher Encryption Program

def caesar_encrypt(text, shift, preserve_caps):
    encrypted = ""
    for ch in text:
        if 'A' <= ch <= 'Z':
            if preserve_caps:
                encrypted += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            else:
                # Convert to lowercase before shifting
                lower = ch.lower()
                encrypted += chr((ord(lower) - ord('a') + shift) % 26 + ord('a'))
        elif 'a' <= ch <= 'z':
            encrypted += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            # Leave punctuation, spaces, and numbers unchanged
            encrypted += ch
    return encrypted


# --- User Input Section ---
shift = int(input("How much to shift (e.g., 2, 3, 8...): "))
preserve_caps = int(input("Preserve capitalization? (1 = Yes, 0 = No): "))
text = input("Enter the text to be encrypted:\n")

# --- Encryption ---
result = caesar_encrypt(text, shift, preserve_caps)

# --- Output ---
print("\nEncrypted text:")
print(result)