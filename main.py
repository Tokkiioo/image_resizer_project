from PIL import Image
with open("C:/Users/casal/Documents/Freecodecamp/19-image_resizer/JUEGOSDLC-LOGO-2.png", "rb") as fp:
    im = Image.open(fp, mode='r')

def resize_image(size1, size2):

    image = Image.open("C:/Users/casal/Documents/Freecodecamp/19-image_resizer/JUEGOSDLC-LOGO-2.png")

    print(f"Current size: {image.size}")

    resized_image = image.resize((size1, size2))

    resized_image.save(f"C:/Users/casal/Documents/Freecodecamp/19-image_resizer/JUEGOSDLC-LOGO-3-{size1}.png")

size1 = int(input("Enter width: "))
size2 = int(input("Enter length: "))
resize_image(size1,size2)