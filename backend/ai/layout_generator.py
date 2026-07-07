from PIL import Image, ImageDraw

def generate_layout(objects, output_path):
    width = 800
    height = 600

    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Room border
    draw.rectangle((40, 40, 760, 560), outline="black", width=4)

    # Window
    draw.rectangle((300, 40, 500, 60), fill="skyblue")
    draw.text((360, 18), "WINDOW", fill="black")

    # Door
    draw.rectangle((40, 500, 80, 560), fill="brown")
    draw.text((20, 570), "DOOR", fill="black")

    x = 100
    y = 100

    for obj in objects:

        x = 40 + int((obj["x"] / 1600) * 680)
        y = 40 + int((obj["y"] / 900) * 480)

        x = max(60, min(x, 620))
        y = max(80, min(y, 480))

        draw.rectangle(
            (x, y, x + 100, y + 50),
            outline="blue",
            width=3
        )

        draw.text(
            (x + 8, y + 18),
            obj["name"].upper(),
            fill="black"
            )
    y += 90

    if y > 430:
            y = 100
            x += 180

    image.save(output_path)