import hashlib

def hash_data(data, algorithm="sha256"):
    """
    Hàm băm dữ liệu với thuật toán SHA-256 hoặc SHA-512.

    Args:
        data (str): Dữ liệu đầu vào để băm.
        algorithm (str): Thuật toán băm ('sha256' hoặc 'sha512').

    Returns:
        str: Giá trị băm của dữ liệu.
    """
    if algorithm == "sha256":
        hashed = hashlib.sha256(data.encode('utf-8')).hexdigest()
    elif algorithm == "sha512":
        hashed = hashlib.sha512(data.encode('utf-8')).hexdigest()
    else:
        raise ValueError("Thuật toán không được hỗ trợ!")
    return hashed

# Dữ liệu ban đầu
original_data = "hello world"

# 1. Băm dữ liệu không sửa đổi
hash_sha256_no_change = hash_data(original_data, "sha256")
hash_sha512_no_change = hash_data(original_data, "sha512")

# 2. Băm dữ liệu sau khi sửa đổi (ví dụ: thêm một chuỗi vào cuối)
modified_data = original_data + " modified"
hash_sha256_modified = hash_data(modified_data, "sha256")
hash_sha512_modified = hash_data(modified_data, "sha512")

# Xuất kết quả
print("Dữ liệu gốc:", original_data)
print("SHA-256 (không sửa):", hash_sha256_no_change)
print("SHA-512 (không sửa):", hash_sha512_no_change)
print("Dữ liệu sửa đổi:", modified_data)
print("SHA-256 (sửa):", hash_sha256_modified)
print("SHA-512 (sửa):", hash_sha512_modified)