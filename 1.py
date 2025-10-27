import easyocr
reader = easyocr.Reader(['en'], gpu=False)   # first call downloads models
result = reader.readtext('/home/shubh/Documents/securimage_show _1.png', detail=0)
print(" ".join(result))

# import easyocr

# reader = easyocr.Reader(['en'], gpu=False)  # You're using CPU here
# result = reader.readtext('securimage_show_1.png', detail=0)
# print("Captcha text:", " ".join(result))
