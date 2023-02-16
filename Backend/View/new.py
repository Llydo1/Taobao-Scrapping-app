import requests

image_url = "https://gw.alicdn.com/imgextra/i3/2734055462/O1CN01VdFlQD1qDe1mU393H_!!2734055462.jpg_Q75.jpg_.webp"
FOLDER_PATH= "C:\\Users\\beani\\OneDrive\\Desktop\\samsidu\\"

img_data = requests.get(image_url).content
with open(FOLDER_PATH + 'image_name.jpg', 'wb') as handler:
    handler.write(img_data)

print(FOLDER_PATH)