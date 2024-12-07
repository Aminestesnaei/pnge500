import os
from tkinter import Tk, filedialog
from PIL import Image

# سلام اگه میخوای کد رو بخونی اول از کامنت شماره یک شروع کن به خوندن #


## (2) ##
def resize_and_convert_to_png(image_paths, output_size=(500, 500)):
    output_folder = "output_images" # اسم فولدر خروجی
    os.makedirs(output_folder, exist_ok=True)  #فولدر خروجی که عکسا داخلش قراره میگیره
    
    for image_path in image_paths:
        try:
            with Image.open(image_path) as img:
                img_resized = img.resize(output_size) # تغییر سایز
                base_name = os.path.splitext(os.path.basename(image_path))[0] 
                output_path = os.path.join(output_folder, f"{base_name}.png")
                img_resized.save(output_path, format="PNG")  # ذخیره عکس در فولدر خروجی که بالاتر ساخته شده
                print(f"Image saved: {output_path}")
        except Exception as e:
            print(f"Error processing {image_path}: {e}")



## (1) ##
def main():
    
    # انتخاب کردن عکس
    image_paths = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff *.webp")] ## اگه فرمت دیگه‌ای خواستی اینجا اضافه کن 
    )
    
    if not image_paths:
        print("No images selected.")
        return
    
    resize_and_convert_to_png(image_paths)


if __name__ == "__main__":
    main()
