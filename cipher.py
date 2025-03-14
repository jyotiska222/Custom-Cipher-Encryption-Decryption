def generate_matrix(keyword):
    # Define the base sequence
    base_sequence = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    
    # Remove characters from the base sequence that are already in the keyword
    filtered_sequence = ""
    for char in base_sequence:
        if char not in keyword:
            filtered_sequence += char
    
    # Combine the keyword and the filtered sequence
    full_sequence = keyword + filtered_sequence
    
    # Generate the 62-column matrix
    matrix = []
    for i in range(62):
        # Shift the sequence to the left by i characters
        row = full_sequence[i:] + full_sequence[:i]
        matrix.append(row)
    
    return matrix

def encrypt_message(message, key, matrix):
    # Remove spaces from the message
    message = message.replace(" ", "")
    
    # Repeat the key if it's shorter than the message
    repeated_key = (key * (len(message) // len(key))) + key[:len(message) % len(key)]
    
    encrypted_message = ""
    
    # Encrypt each character
    for i in range(len(message)):
        # Get the row index (based on the message character)
        row_index = matrix[0].find(message[i])
        if row_index == -1:
            # If the character is not in the matrix (e.g., a symbol), keep it as is
            encrypted_message += message[i]
            continue
        
        # Get the column index (based on the key character)
        col_index = matrix[0].find(repeated_key[i])
        if col_index == -1:
            # If the key character is not in the matrix (e.g., a symbol), keep the message character as is
            encrypted_message += message[i]
            continue
        
        # Get the encrypted character from the intersection of the row and column
        encrypted_char = matrix[row_index][col_index]
        encrypted_message += encrypted_char
    
    return encrypted_message

def decrypt_message(encrypted_message, key, matrix):
    # Remove spaces from the encrypted message
    encrypted_message = encrypted_message.replace(" ", "")
    
    # Repeat the key if it's shorter than the encrypted message
    repeated_key = (key * (len(encrypted_message) // len(key))) + key[:len(encrypted_message) % len(key)]
    
    decrypted_message = ""
    
    # Decrypt each character
    for i in range(len(encrypted_message)):
        # Get the column index (based on the key character)
        col_index = matrix[0].find(repeated_key[i])
        if col_index == -1:
            # If the key character is not in the matrix (e.g., a symbol), keep the encrypted character as is
            decrypted_message += encrypted_message[i]
            continue
        
        # Find the row index where the encrypted character exists in the column
        row_index = -1
        for row in range(62):
            if matrix[row][col_index] == encrypted_message[i]:
                row_index = row
                break
        
        if row_index == -1:
            # If the encrypted character is not in the matrix (e.g., a symbol), keep it as is
            decrypted_message += encrypted_message[i]
        else:
            # Get the decrypted character from the first row of the matrix
            decrypted_char = matrix[0][row_index]
            decrypted_message += decrypted_char
    
    return decrypted_message

# Main program
def main():
    # Take user inputs
    keyword = input("Enter the Passkey: ")
    choice = input("Choose 'e' for encrypt or 'd' for decrypt: ").strip().lower()
    
    if choice == "e":
        message = input("Enter the MESSAGE: ")
        key = input("Enter the KEY_OF_THAT_MESSAGE: ")
        
        # Generate the matrix
        matrix = generate_matrix(keyword)
        
        # Encrypt the message
        encrypted_message = encrypt_message(message, key, matrix)
        print("Encrypted Message:", encrypted_message)
    
    elif choice == "d":
        encrypted_message = input("Enter the ENCRYPTED MESSAGE: ")
        key = input("Enter the KEY OF THE MESSAGE: ")
        
        # Generate the matrix
        matrix = generate_matrix(keyword)
        
        # Decrypt the message
        decrypted_message = decrypt_message(encrypted_message, key, matrix)
        print("Decrypted Message:", decrypted_message)
    
    else:
        print("Invalid choice. Please choose 'encrypt' or 'decrypt'.")

# Run the program
if __name__ == "__main__":
    main()