def Write_Code(content, file_name, mode="w"):
    with open(file_name, mode) as f:
        f.write(content)