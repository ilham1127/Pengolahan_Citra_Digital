import heapq
from collections import defaultdict

def build_frequency_dict(gambar):
    frequency_dict = defaultdict(int)
    for pixel in gambar:
        frequency_dict[pixel] += 1
    return frequency_dict

def build_huffman_tree(frequency_dict):
    heap = [[weight, [pixel, ""]] for pixel, weight in frequency_dict.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        low = heapq.heappop(heap)
        high = heapq.heappop(heap)
        for pair in low[1:]:
            pair[1] = '0' + pair[1]
        for pair in high[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])
    return heap[0]

def build_huffman_codes(tree):
    huffman_codes = {}
    for pair in tree[1:]:
        pixel = pair[0]
        code = pair[1]
        huffman_codes[pixel] = code
    return huffman_codes

gambar = input("Masukkan data gambar yang ingin dikompresi: ")
frequency_dict = build_frequency_dict(gambar)
huffman_tree = build_huffman_tree(frequency_dict)
huffman_codes = build_huffman_codes(huffman_tree)
print("Kode Huffman:")
for pixel, code in huffman_codes.items():
    print(pixel, ":", code)