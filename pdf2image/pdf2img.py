import os,sys,fitz

if len(sys.argv) != 2:
    pdf_path = input("Please enter pdf name(with extention) : ")
else:
    pdf_path = sys.argv[1]
    # for command line usage : python pdf2img.py main.pdf

# pdf_path = 'main.pdf'

# CHECK IF Path exist 
if not os.path.exists(pdf_path): 
    print("path does not exist, pdf must be in the same folder")
    sys.exit(1)

# create folder recursively XD 
os.makedirs('Converted_img',exist_ok=True)
# os.mkdir('Converted_img',0o666)

base_name = os.path.basename(pdf_path).split('.')[0]
images = []
# 
pdf_file = fitz.open(pdf_path)

for i in range(len(pdf_file)):
    page = pdf_file.loadPage(i)
    page_pixel = page.getPixmap()
    images.append(page_pixel.tobytes('pgm'))
    page_pixel.writePNG(f"Converted_img/{base_name}{i}.png")




#  to compress png and convert into JPEG
''' 
from PIL import Image
def png2jpg():
    directory = r'Converted_img'
    for f in os.listdir(directory):
        if f.endswith(".png"):
            im = Image.open(os.path.join(directory, f))
            name= os.path.splitext(os.path.join(directory, f))[0] +'.jpg'
            rgb_im = im.convert('RGB')
            rgb_im.save(name)
            # print(os.path.join(directory, f))
png2jpg()

'''