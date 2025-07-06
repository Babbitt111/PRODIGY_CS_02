# 🖼️ Image Encryption Tool – Prodigy InfoTech Internship Task 2

This Python tool encrypts and decrypts images using pixel-level manipulation. Developed as part of my **Cyber Security Internship** with **Prodigy InfoTech**, it demonstrates how simple transformations can obscure and restore image data securely.

---

## 🔐 Features

- Encrypts images by modifying RGB pixel values using a user-defined key
- Decrypts images by reversing the transformation
- Supports `.png`, `.jpg`, and other common formats
- Simple command-line interface
- Lightweight and easy to use

---

## 🚀 How to Use

### 1. Install Dependencies

Make sure you have Python installed. Then install Pillow:

```bash
pip install pillow

---

### 2. Encrypt an Image

Run the script and follow the prompts:

```bash
python image_encryptor.py

- Choose Encrypt
- Enter the path to your image (e.g., images/photo.jpg)
- Enter a numeric key (e.g., 123)
- The encrypted image will be saved as encrypted_photo.png

---

### 3. Decrypt an Image

Run the script again and choose **Decrypt**:

```bash
python image_encryptor.py

- Choose Decrypt
- Enter the path to your image (e.g., images/photo.jpg)
- Enter a numeric key (e.g., 123)
- The decrypted image will be saved as decrypted_photo.png

```markdown
---

## 🧪 Sample Output

🔐 Image Encryptor 🔐
- Encrypt an image
- Decrypt an image
1

Enter image path:
images/photo.jpg

Enter encryption key:
123

✅ Image encrypted and saved as encrypted_photo.png

---

## 🧠 What I Learned

- How to manipulate image pixels using Pillow  
- How to apply reversible transformations for encryption  
- How to build a simple CLI tool in Python  
- The importance of using consistent keys for decryption
