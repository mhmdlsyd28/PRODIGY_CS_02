import hashlib
from PIL import Image

# Image Encryption & Decryption Project

# Encryption Function
def encrypt_image( image_path ,  enc_key ):
    img = Image.open(image_path)
    width, height = img.size
    # Hashing th key with sha256
    hashed = hashlib.sha256(enc_key.encode()).digest()
    pixels = img.load()
    # Mapping the image positions
    pixel_positions = [(x, y) for y in range(height) for x in range(width)]
    num_positions = len(pixel_positions)
    # Shuffling Pixels
    for i in range(num_positions):
        hash_index = i % len(hashed)
        hash_value = hashed[hash_index]
        new_index = (hash_value + i) % num_positions
        pixel_positions[i], pixel_positions[new_index] = pixel_positions[new_index], pixel_positions[i]

    # Create a new image with shuffled pixels
    encrypted_img = Image.new("RGB", (width, height))

    # Copy pixels to the new image with shuffled positions
    for i, (x, y) in enumerate(pixel_positions):
        encrypted_pixel = pixels[i % width, i // width]
        encrypted_img.putpixel((x, y), encrypted_pixel)

    # Save the encrypted image
    encrypted_img.save("encrypted_img.jpg")
    print("Image encrypted successfully.")
    return encrypted_img


# Decryption Function :
def decrypt_image (encrypted_image_path , dec_key , enc_key ):
    # Check if the user input Key is the same Encryption Key
    if dec_key == enc_key :
        img = Image.open(encrypted_image_path)
        width, height = img.size
        hashed = hashlib.sha256(dec_key.encode()).digest()
        pixels = img.load()

        # Create a shuffled list of pixel positions based on the hash
        pixel_positions = [(x, y) for y in range(height) for x in range(width)]
        num_positions = len(pixel_positions)
        for i in range(num_positions):
            hash_index = i % len(hashed)
            hash_value = hashed[hash_index]
            new_index = (hash_value + i) % num_positions
            pixel_positions[i], pixel_positions[new_index] = pixel_positions[new_index], pixel_positions[i]

        # Create a new image with shuffled pixels
        decrypted_img = Image.new("RGB", (width, height))
        decrypted_pixels = decrypted_img.load()

        # Copy pixels to the new image with shuffled positions
        for i, (x, y) in enumerate(pixel_positions):
            decrypted_pixels[i % width, i // width] = pixels[x, y]
            decrypted_img.putpixel((x, y), decrypted_pixels[i % width, i // width])

        decrypted_img.save("Decrypted_img.png")
        print("Image decrypted successfully.")
        return decrypted_img
    else:
        print("Wrong Key !!!! ")
        return (encrypted_image)  # Return the Encrypted Image in the case of wrong Key


# Image Encryption
image_path = 'D:\Pycharm.Projects\img.jpg'               # Enter the path of the image
enc_key = input("Enter the Encryption key : ")           # Encryption Key
encrypted_image = encrypt_image(image_path, enc_key)     # Calling the Encryption Function
encrypted_image.show()

# Image Decryption
# Check whether the user wants to decrypt the image or not
x=input("Do you want to Decrypt the Image  [y/n]   ?  : ")
if x == 'y':
    encrypted_image_path = "D:\Pycharm.Projects\encrypted_img.jpg"     # Enter the path of the Encrypted Image
    dec_key = input("Enter the Decryption key : ")                     # Enter the Key
    decrypted_image = decrypt_image(encrypted_image_path, dec_key,enc_key)  # Decrypting the Encrypted Image
    decrypted_image.show()
else: print("Thank you")

