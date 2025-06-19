from PIL import Image
import stepic

# Đường dẫn tới ảnh gốc (ảnh HUTECH 30 năm)
original_image = 'hutech30.png'  # ví dụ ảnh gốc tên là hutech30.png
encoded_image_path = 'static/TEST/encoded.png'

# Mở ảnh
img = Image.open(original_image)

# Thông điệp cần giấu
message = "ilovehutech"

# Mã hóa thông điệp vào ảnh
encoded_img = stepic.encode(img, message.encode())

# Lưu ảnh đã mã hóa
encoded_img.save(encoded_image_path)

print(f"Đã giấu thông điệp vào ảnh: {encoded_image_path}")
