from PIL import Image
import numpy as np

def encrypt_image(input_image_path: str, output_image_path: str, key: int) -> None:
    """
    Encrypts an image by adding a key to each pixel value.

    Args:
    input_image_path (str): Path to the input image.
    output_image_path (str): Path where the encrypted image will be saved.
    key (int): The encryption key to be added to pixel values.
    """
    try:
        # Open the image
        image = Image.open(input_image_path)
        image_array = np.array(image, dtype=np.uint8)

        # Check if key is within valid range
        if not (0 <= key < 256):
            raise ValueError("Key must be in the range [0, 255].")

        # Encrypt the image by adding the key to each pixel
        encrypted_array = (image_array.astype(np.uint16) + key) % 256
        encrypted_array = encrypted_array.astype(np.uint8)

        # Create an encrypted image from the array
        encrypted_image = Image.fromarray(encrypted_array)
        encrypted_image.save(output_image_path)
        print(f"Image encrypted and saved as {output_image_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def decrypt_image(input_image_path: str, output_image_path: str, key: int) -> None:
    """
    Decrypts an image by subtracting the key from each pixel value.

    Args:
    input_image_path (str): Path to the encrypted image.
    output_image_path (str): Path where the decrypted image will be saved.
    key (int): The decryption key to be subtracted from pixel values.
    """
    try:
        # Open the encrypted image
        image = Image.open(input_image_path)
        image_array = np.array(image, dtype=np.uint8)

        # Check if key is within valid range
        if not (0 <= key < 256):
            raise ValueError("Key must be in the range [0, 255].")

        # Decrypt the image by subtracting the key from each pixel
        decrypted_array = (image_array.astype(np.uint16) - key) % 256
        decrypted_array = decrypted_array.astype(np.uint8)

        # Create a decrypted image from the array
        decrypted_image = Image.fromarray(decrypted_array)
        decrypted_image.save(output_image_path)
        print(f"Image decrypted and saved as {output_image_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Encrypt the image
        encrypt_image('input.png', 'encrypted_image.png', key=50)
        # Decrypt the image
        decrypt_image('encrypted_image.png', 'decrypted_image.png', key=50)
    except Exception as e:
        print(f"An error occurred during processing: {e}")
