import hashlib


def sha256_checksum(file_path, buf_size=65536):
    sha256 = hashlib.sha256()

    with open(file_path, 'rb') as file:
        while True:
            data = file.read(buf_size)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()
