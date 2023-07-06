def compress_rle(teks):
    compress = ""
    count = 1
    for a in range (1, len(tekt)):
        if teks[a] == teks[a - 1]:
            count += 1
        else:
            compress += teks[a - 1] + str(count)
            count = 1
    compress += teks[-1] + str(count)
    return compress
teks = input("Silahkan masukkan teks yang mau anda kompres: ")
compress = compress_rle(teks)
print("Teks yang sudah dikompres: ", compress)
