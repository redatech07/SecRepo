def read_file(file_path, max_size = 5 * 1024 * 1024):

    try:
        with open(file_path, "rb") as file:
            content = file.read(max_size + 1)

    except OSError:
        return None

    if len(content) > max_size:
        return None

    try:
        return content.decode("utf-8-sig")

    except UnicodeDecodeError:
        try:
            return content.decode("utf-16")

        except UnicodeDecodeError:
            return None