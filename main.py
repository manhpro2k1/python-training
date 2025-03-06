import heapq
from collections import Counter
import pickle


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoding:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    def make_frequency_dict(self, text):
        """Đếm tần suất xuất hiện của mỗi ký tự"""
        return Counter(text)

    def make_heap(self, frequency):
        """Tạo min-heap từ tần suất xuất hiện"""
        for char, freq in frequency.items():
            node = HuffmanNode(char, freq)
            heapq.heappush(self.heap, node)

    def merge_nodes(self):
        """Gộp các node cho đến khi heap chỉ còn 1 phần tử"""
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = HuffmanNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)

    def make_codes_helper(self, node, current_code):
        """Đệ quy để tạo mã Huffman cho mỗi ký tự"""
        if node is None:
            return

        if node.char is not None:
            self.codes[node.char] = current_code
            self.reverse_mapping[current_code] = node.char

        self.make_codes_helper(node.left, current_code + "0")
        self.make_codes_helper(node.right, current_code + "1")

    def make_codes(self):
        """Tạo mã Huffman cho tất cả các ký tự"""
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)

    def get_encoded_text(self, text):
        """Mã hóa đoạn văn bản ban đầu"""
        encoded_text = ""
        for char in text:
            encoded_text += self.codes[char]
        return encoded_text

    def pad_encoded_text(self, encoded_text):
        """Đệm thêm bits để đủ byte"""
        padding = 8 - (len(encoded_text) % 8)
        for i in range(padding):
            encoded_text += "0"

        # Thêm thông tin về số bit đệm vào đầu
        padded_info = "{0:08b}".format(padding)
        padded_encoded_text = padded_info + encoded_text
        return padded_encoded_text

    def get_byte_array(self, padded_encoded_text):
        """Chuyển đổi chuỗi bits thành mảng bytes"""
        b = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i+8]
            b.append(int(byte, 2))
        return bytes(b)

    def compress(self, text):
        """Nén dữ liệu văn bản"""
        frequency = self.make_frequency_dict(text)
        self.make_heap(frequency)
        self.merge_nodes()
        self.make_codes()

        encoded_text = self.get_encoded_text(text)
        padded_encoded_text = self.pad_encoded_text(encoded_text)
        bytes_array = self.get_byte_array(padded_encoded_text)

        # Lưu bảng tra mã Huffman để giải nén sau này
        with open("huffman_mapping.pkl", "wb") as f:
            pickle.dump(self.reverse_mapping, f)

        return bytes_array

    def remove_padding(self, bit_string):
        """Loại bỏ padding khi giải nén"""
        padded_info = bit_string[:8]
        padding = int(padded_info, 2)

        bit_string = bit_string[8:]
        encoded_text = bit_string[:-padding] if padding > 0 else bit_string

        return encoded_text

    def decode_text(self, encoded_text):
        """Giải mã chuỗi bit thành văn bản gốc"""
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                decoded_text += self.reverse_mapping[current_code]
                current_code = ""

        return decoded_text

    def decompress(self, bytes_array):
        """Giải nén dữ liệu đã nén"""
        # Tải bảng tra mã Huffman
        with open("huffman_mapping.pkl", "rb") as f:
            self.reverse_mapping = pickle.load(f)
            # Tạo ngược lại codes từ reverse_mapping
            self.codes = {v: k for k, v in self.reverse_mapping.items()}

        # Chuyển đổi bytes thành chuỗi bit
        bit_string = ""
        for byte in bytes_array:
            bits = bin(byte)[2:].rjust(8, '0')
            bit_string += bits

        # Loại bỏ padding
        encoded_text = self.remove_padding(bit_string)

        # Giải mã
        decompressed_text = self.decode_text(encoded_text)

        return decompressed_text

# Ví dụ sử dụng


def main():
    huffman = HuffmanCoding()

    # Kiểm tra xem file có tồn tại không, nếu không thì tạo văn bản mẫu
    try:
        with open("input.txt", "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print("File 'input.txt' không tồn tại. Tạo file với dữ liệu mẫu...")
        text = """Đây là một đoạn văn bản mẫu để kiểm tra thuật toán nén Huffman.
Thuật toán nén Huffman là một thuật toán nén không mất dữ liệu phổ biến,
được sử dụng trong nhiều ứng dụng nén dữ liệu như định dạng JPEG, MP3, và nhiều định dạng nén khác.
Thuật toán này hoạt động dựa trên việc phân tích tần suất xuất hiện của các ký tự trong dữ liệu
và xây dựng mã có độ dài biến đổi cho mỗi ký tự dựa trên tần suất xuất hiện của chúng."""

        # Tạo file input.txt với dữ liệu mẫu
        with open("input.txt", "w", encoding="utf-8") as file:
            file.write(text)
        print("Đã tạo file 'input.txt' với dữ liệu mẫu.")

    # Nén dữ liệu
    compressed_data = huffman.compress(text)

    # Lưu dữ liệu đã nén vào file
    with open("compressed.bin", "wb") as file:
        file.write(compressed_data)
    print("Đã lưu dữ liệu nén vào file 'compressed.bin'")

    # Giải nén dữ liệu
    with open("compressed.bin", "rb") as file:
        binary_data = file.read()

    decompressed_text = huffman.decompress(binary_data)

    # Lưu dữ liệu đã giải nén
    with open("decompressed.txt", "w", encoding="utf-8") as file:
        file.write(decompressed_text)
    print("Đã lưu dữ liệu giải nén vào file 'decompressed.txt'")

    # Hiển thị tỷ lệ nén
    original_size = len(text.encode('utf-8'))
    compressed_size = len(compressed_data)
    print(f"Kích thước ban đầu: {original_size} bytes")
    print(f"Kích thước sau khi nén: {compressed_size} bytes")
    print(f"Tỷ lệ nén: {compressed_size/original_size:.2%}")

    # Kiểm tra tính chính xác của thuật toán
    print(f"Nén thành công: {text == decompressed_text}")


if __name__ == "__main__":
    main()
