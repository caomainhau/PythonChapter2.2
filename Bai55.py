import zipfile

def compress_file(input_file, output_zip):
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        zipf.write(input_file)
    print("Đã nén thành công!")

def extract_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_to)
    print("Đã giải nén thành công!")
