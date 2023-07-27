from PIL import Image, ImageDraw, ImageFont


def watermark(image_name):
    photo = Image.open(image_name)

    drawing = ImageDraw.Draw(photo)

    black = (3, 8, 12)
    font = ImageFont.truetype("arial.ttf", 40)
    drawing.text((0, 0), 'text', fill=black, font=font)
    photo.save(image_name)