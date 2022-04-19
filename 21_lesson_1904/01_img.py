from PIL import Image

orig_image = 'spiral1.eps'  # сохраняю путь к изображению
img = Image.open(orig_image)  # открываю его
figure = img.convert('RGBA')  # конвертирую цвета в RGB
img.save('spiral1.png', lossless=True)