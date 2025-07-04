from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
    img.save(output_path)
    print("✅ Image encrypted and saved as", output_path)

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
    img.save(output_path)
    print("✅ Image decrypted and saved as", output_path)

# --- User Interface ---
mode = input("Type 'encrypt' or 'decrypt': ").strip().lower()
input_file = input("Enter input image filename (e.g., image.png): ")
output_file = input("Enter output image filename: ")
key = int(input("Enter encryption key (0–255): "))

if mode == 'encrypt':
    encrypt_image(input_file, output_file, key)
elif mode == 'decrypt':
    decrypt_image(input_file, output_file, key)
else:
    print("❌ Invalid mode. Please type 'encrypt' or 'decrypt'.")