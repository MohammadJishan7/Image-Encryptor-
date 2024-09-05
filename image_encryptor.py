# Simple Image Encryption Tool

from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path):
    # Load the image
    image = Image.open(input_image_path)
    pixels = np.array(image)
    
    # Convert pixel array to a higher data type to prevent overflow
    pixels = pixels.astype(np.int16)

    # Swap pixel values
    pixels[:, :, 0], pixels[:, :, 1] = pixels[:, :, 1], pixels[:, :, 0]  # Swap Red and Green channels

    # Apply a basic mathematical operation (adding 50 to each pixel value)
    pixels = (pixels + 50) % 256

    # Convert the pixel array back to uint8 before saving
    pixels = pixels.astype(np.uint8)

    # Save the encrypted image
    encrypted_image = Image.fromarray(pixels)
    encrypted_image.save(output_image_path)

# Example usage with your specific paths
encrypt_image('C:\\Users\\jisha\\Desktop\\Image\\Daki.png', 'D:\\Python\\data\\encrypted_Daki.png')
