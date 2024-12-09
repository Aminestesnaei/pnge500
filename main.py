from tkinter import * 
import customtkinter 
import os
from tkinter import filedialog
from PIL import Image
from rembg import remove
import io

# onnxruntime needed

def select_image():
    global image_paths
    # انتخاب کردن عکس
    image_paths = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff *.webp")]  # اگه فرمت دیگه‌ای خواستی اینجا اضافه کن
    )

def resize_remove_bg_and_convert_to_png():
    output_folder = "output_images"  # اسم فولدر خروجی
    os.makedirs(output_folder, exist_ok=True)  # فولدر خروجی که عکس ها داخلش قراره میگیره

    x = int(x_entry.get()) + 1 
    y = int(y_entry.get()) + 1  
    output_size = (x, y)

    # گرفتن فرمت انتخابی
    selected_format = output_format.get()

    for image_path in image_paths:
        try:
            # باز کردن تصویر
            with Image.open(image_path) as img:
                # بررسی وضعیت چک‌باکس برای حذف بک‌گراند
                if remove_bg_var.get():
                    # حذف پس‌زمینه
                    with open(image_path, "rb") as img_file:
                        input_image = img_file.read()  # خواندن تصویر به صورت باینری
                        output_image = remove(input_image)  # حذف پس‌زمینه با استفاده از rembg
                    
                    # تبدیل داده باینری به تصویر PIL
                    img = Image.open(io.BytesIO(output_image))
                
                # تغییر سایز تصویر
                img_resized = img.resize(output_size)
                
                # ذخیره تصویر در فرمت انتخابی
                base_name = os.path.splitext(os.path.basename(image_path))[0]
                output_path = os.path.join(output_folder, f"{base_name}_no_bg.{selected_format}")
                img_resized.save(output_path, format=selected_format)  # ذخیره با فرمت انتخابی
                print(f"Image saved: {output_path}")
        except Exception as e:
            print(f"Error processing {image_path}: {e}")



####### UI CONFIGS #######

def root():
    global x_entry, y_entry, image_paths, remove_bg_var, output_format
    image_paths = []  # متغیر برای ذخیره مسیرهای انتخابی تصاویر

    root = customtkinter.CTk()
    root.title("Pnage500 Developer")
    root.geometry("450x560")
    root.resizable(width=True, height=True)
    customtkinter.deactivate_automatic_dpi_awareness()
    root.config(bg='#272932')

####### Selecting ####### انتخاب عکس

    select_image_label = customtkinter.CTkLabel(root, text="Select Images :", fg_color="#272932", font=("Montserrat", 25)).place(x=20, y=77)
    select_image_button = customtkinter.CTkButton(root, text="SELECT", corner_radius=50, height=30, width=123, fg_color="#E96718", bg_color="#272932", font=("Montserrat", 16), text_color="#000000", command=select_image).place(x=290, y=84)
    supported_files = customtkinter.CTkLabel(root, text="supported format : \n *.jpg *.jpeg *.png *.bmp *.gif *.tiff *.webp", fg_color="#272932", font=("Montserrat", 15), justify=LEFT).place(x=50, y=120)




####### Resize ####### تغییر سایز

    resize_label = customtkinter.CTkLabel(root, text="Resize :", fg_color="#272932", font=("Montserrat", 25)).place(x=20, y=240)
    
    x_entry = customtkinter.CTkEntry(root, bg_color="#272932", font=("Montserrat", 20), height=30, width=60, fg_color="#E96718", text_color="#000000")
    x_entry.place(x=285, y=240)
    
    y_entry = customtkinter.CTkEntry(root, bg_color="#272932", font=("Montserrat", 20), height=30, width=60, fg_color="#E96718", text_color="#000000")
    y_entry.place(x=355, y=240)

####### Removing Checkbox ####### چکباکس حذف بکگراند
    remove_bg_var = BooleanVar(value=False)  # مقدار پیش‌فرض: False
    Remove_Background_label = customtkinter.CTkLabel(root, text="Remove Background :", fg_color="#272932", font=("Montserrat", 25)).place(x=20, y=320)
    remove_bg_checkbox = customtkinter.CTkCheckBox(root, text="", variable=remove_bg_var, bg_color="#272932", text_color="#E96718", fg_color="#E96718", font=("Anaheim", 25), hover=False).place(x=340, y=325)

    save_as_label = customtkinter.CTkLabel(root, text="Save As :", fg_color="#272932", font=("Montserrat", 25)).place(x=20, y=402)

    ####### Format Menu ####### منوی انتخاب فرمت 
    output_format = StringVar(value="png")  # مقدار پیش‌فرض فرمت PNG
    optionmenu = customtkinter.CTkOptionMenu(
        root,
        values=["jpg", "jpeg", "png", "bmp", "gif", "tiff", "webp"],
        height=30,
        width=123,
        fg_color="#E96718",
        text_color="#000000",
        variable=output_format  # متغیر برای ذخیره فرمت انتخاب‌شده
    ).place(x=290, y=402)

    ####### START ####### شروع
    select_image_button = customtkinter.CTkButton(root, text="START", corner_radius=50, height=50, width=153, fg_color="#E96718", bg_color="#272932", font=("Montserrat", 20), text_color="#000000", command=lambda: resize_remove_bg_and_convert_to_png()).place(x=145, y=475)

    root.mainloop()

root()
