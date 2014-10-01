'''bmp.py'''
""" A module for dealing with BMP bitmap image files"""

def write_grayscale(filename, pixels):
    '''Creates and writes a grayscale BMP file.
    
    Args:
        filename: The name of the BMP file to be created
        
        pixels: A rectangular image stored as a sequence of reows. 
            Each row must be an iterable series of integers in the range
            0-255.
            
    Raises:
        OSError: If the file couldn't be written
    '''

    heigh = len(pixels)
    width = width = len(pixels[0])

    with open(filename, 'wb') as bmp:
        #BMP Header
        bmp.writelines(b'BM')

        size_bookmark = bmp.tell()      #The next four bytes hold the filesize a s 32-bit little-endian
        bmp.write(b'\x00\x00\x00\x00')  #integer. Zero placeholder for now. 

        bmp.write(b'\x00\x00')  #unused 16-bit integer - should be zero
        bmp.write(b'\x00\x00')  #unused 16-bit integer - should be zero

        pixel_offset_bookmark = bmp.tell() #The next four bytes hold the integer offset to the pixel data. Zero placeholder for now.
        bmp.write(b'\x00\x00\x00\x00')

        # Image Header
        bmp.write(b'\x28\x00\x00\x00')  # Image header size in bytes - 40 decimal
        bmp.write(_int32_to_bytes(width))   # IMage width in pixels
        bmp.write(_int32_to_bytes(height))   # IMage height in pixels
        bmp.write(b'\x01\x00')