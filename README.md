# Custom Cipher Encryption & Decryption

## Description

This Python program encrypts and decrypts messages using a dynamic 62-column matrix. A passkey generates a shifted character sequence, while a key encodes messages securely.

## Features

- Uses a matrix generated from a passkey.
- Encrypts and decrypts messages.
- Supports A-Z, a-z, 0-9 characters.
- Handles missing characters.

## How It Works

### Step 1: Generate the Matrix

1. Remove passkey characters from the base sequence.
2. Create a shifted 6×6 matrix.

| Row | Shift | Sequence  |
|----|------|---------|
| 0  | 0    | ba1AB2  |
| 1  | 1    | a1AB2b  |
| 2  | 2    | 1AB2ba  |

### Step 2: Encrypting

1. Match key length to message.
2. Locate characters in matrix rows.
3. Find intersection for encryption.

| Message | Key | Encrypted |
|---------|-----|-----------|
| A       | B   | 1         |
| 1       | 2   | A         |
| b       | B   | a         |

Encrypted Message: `1Aa`

### Step 3: Decrypting

| Encrypted | Key | Decrypted |
|-----------|-----|-----------|
| 1         | B   | A         |
| A         | 2   | 1         |
| a         | B   | b         |

Decrypted Message: `A1b`

## Running the Program

1. Clone repository:
   ```sh
   git clone git remote add origin https://github.com/jyotiska222/Custom-Cipher-Encryption-Decryption.git
   cd Custom-Cipher-Encryption-Decryption
   ```
2. Run the script:
   ```sh
   python cipher.py
   ```
3. Input required values.

### Example

#### Encryption
```
Enter the Passkey: pas
Choose 'e' for encrypt or 'd' for decrypt: e
Enter the MESSAGE: SecretMsg
Enter the KEY OF THAT MESSAGE: key
Encrypted Message: 7sPRsf1gT
```
#### Decryption
```
Enter the Passkey: pas
Choose 'e' for encrypt or 'd' for decrypt: d
Enter the ENCRYPTED MESSAGE: 7sPRsf1gT
Enter the KEY OF THE MESSAGE: key
Decrypted Message: SecretMsg
```

## Security Strength

- A 4-character passkey has **62⁴ = 14.7 million** combinations.
- A matching key also has **62⁴** combinations.
- Total brute-force attempts: **218 trillion**.

## Notes

- Passkey and key must match for decryption.
- Case-sensitive.
- Non-alphanumeric characters remain unchanged.

*For any Suggestions
j.biswas0022@gmail.com* 

**MY INSTAGRAM PASSWORD: PLgf6B@# (Encrypted)**
*If you get it, You have it*

