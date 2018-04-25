
def sha256_checksum(file_path, buf_size=65536):
    import hashlib
    sha256 = hashlib.sha256()

    with open(file_path, 'rb') as file:
        while True:
            data = file.read(buf_size)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()


def ensure_dir_exists(dir_path):
    import os
    import errno

    try:
        os.makedirs(dir_path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
