import cv2
import numpy as n


#ubah data
def string_to_bits(pesan):
    biner = ''.join(format(ord(char), '08b') for char in pesan)
    return biner

#ubah data dengan file yang ingin disisipkan
def hide_data(gambar, data):
    uk_data = len(data)

    #ukuran gambar
    t_gambar, l_gambar, _ = gambar.shape
    uk_gambar = t_gambar * l_gambar

    if uk_data > uk_gambar:
        raise ValueError ("File terlalu besar.")

    index = 0

    for baris in range(t_gambar):
        for kolom in range(l_gambar):
            pixel = gambar[baris, kolom]

            for warna in range (3): #citra warna
                if index < uk_data:
                    #bit data
                    bit = int(data[index])

                    #ubah bit LSB dengan bit data
                    pixel[warna] = (pixel[warna] & 254) | bit
                    index += 1
                else:
                    break
    return gambar

#ekstrak data dari gambar
def extract_data(image, uk_data):
    extracted_data = ""
    index = 0

    t_gambar, l_gambar, _ = image.shape

    for baris in range (t_gambar):
        for kolom in range (l_gambar):
            pixel = gambar[baris, kolom]

            for warna in range (3): #citra warna
                #bit-data dari bit LSB
                extracted_data += str(pixel[warna] & 1)
                index += 1

                if index == uk_data:
                    return extracted_data

#implementasi
if __name__ == "__main__":
    #baca gambar
    image_path = "tiger.jpg"
    gambar = cv2.imread(image_path)

    #file yg disembunyikan
    hidedata = "Ilham"

    #ubah data jadi bit
    data_hidden = string_to_bits(hidedata)

    #sisipkan data ke gambar
    gambar_hide = hide_data(gambar.copy(), data_hidden)

    #simpan gambar
    output_gambar = "hasil_tiger.jpg"
    cv2.imwrite(output_gambar, gambar_hide)

    #ekstrak data dari gambar
    extracted_data = extract_data(gambar_hide, len(data_hidden))
    print("File tersembunyi di ekstrak: ", extracted_data)