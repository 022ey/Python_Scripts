from urllib.request import urlopen  # TODO: change this
import re 
import os
import cv2

def download_image(num, directory):

    if num == 404:
        return 
    
    try:
        url = f'https://xkcd.com/{num}'
        regex = r"for hotlinking\/embedding\): (.*)"
        content = urlopen(url)
        if content.status == 200:
            print(num, 'OK')
            html_content = content.read().decode()
            matches = re.finditer(regex, html_content, re.MULTILINE)

            for matchNum, match in enumerate(matches, start=1):
                image_url = match.group(matchNum)
                
                if not '.' in image_url.rsplit('/')[-1]:
                    print('no file at', num)
                    return                
                
                ext = image_url.rsplit('.')[-1]
                image = urlopen(image_url).read()
                open(f'{directory}/{num}.{ext}', 'wb').write(image)
        else:
            print('Error:', num)
    except:
         print('exception at', num)

def get_latest_comic_id():
    regex = r"<meta property=\"og:url\" content=\"https://xkcd.com/(.*)/"
    xkcd  = urlopen('https://xkcd.com').read().decode()
    matches = re.finditer(regex, xkcd, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        return int(match.group(matchNum))

def resize_images(directory, height=1080, width=1920 ):  # top-right feels good
    os.makedirs(directory + '_resized', exist_ok=True)
    for image in os.listdir(directory):
        
        if '.gif' in image:   # magic lib is better
            continue
        
        img = cv2.imread(directory + '/' + image)
        black = [0]*3    
        top, bottom, left, right = map( lambda x : x if x > 0 else 0, (0, height-len(img), width-len(img[0]), 0))
        
        
        
        padded_img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=black)
        cv2.imwrite(directory+'_resized' + '/' + image, padded_img)    
    
if __name__ == '__main__':
    directory = 'xkcd_images'
    os.makedirs(directory, exist_ok=True)

    for num in range(1, get_latest_comic_id() + 1):
         download_image(num, directory)
    resize_images(directory)
