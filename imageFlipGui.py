import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image


def mirror_images_in_folder(folder_path, horizontal_flip=False, vertical_flip=False):
    files = os.listdir(folder_path)
    image_files_exist = False
    for file in files:
        if file.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            image_files_exist = True
            break

    if not image_files_exist:
        messagebox.showwarning("警告", "指定路径中不存在图像文件。")
        return

    for file in files:
        if file.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            file_path = os.path.join(folder_path, file)
            try:
                image = Image.open(file_path)
                if horizontal_flip:
                    image = image.transpose(Image.FLIP_LEFT_RIGHT)
                if vertical_flip:
                    image = image.transpose(Image.FLIP_TOP_BOTTOM)
                image.save(file_path)
            except Exception as e:
                messagebox.showerror("错误", f"处理文件 {file} 时出错：{e}")

    messagebox.showinfo("完成", "图像翻转完成。")


def browse_folder():
    folder_path = filedialog.askdirectory()
    entry_path.delete(0, tk.END)
    entry_path.insert(0, folder_path)


def start_flip():
    folder_path = entry_path.get()
    horizontal_flip = var_horizontal.get()
    vertical_flip = var_vertical.get()
    mirror_images_in_folder(folder_path, horizontal_flip, vertical_flip)


# 创建主窗口
root = tk.Tk()
root.title("图像翻转工具")

# 创建文件夹路径输入框和浏览按钮
frame_path = tk.Frame(root)
frame_path.pack(pady=10)
label_path = tk.Label(frame_path, text="选择文件夹路径:")
label_path.pack(side=tk.LEFT)
entry_path = tk.Entry(frame_path, width=50)
entry_path.pack(side=tk.LEFT)
button_browse = tk.Button(frame_path, text="浏览", command=browse_folder)
button_browse.pack(side=tk.LEFT)

# 创建水平和垂直翻转选项
frame_options = tk.Frame(root)
frame_options.pack(pady=5)
var_horizontal = tk.BooleanVar()
check_horizontal = tk.Checkbutton(frame_options, text="水平翻转", variable=var_horizontal)
check_horizontal.pack(side=tk.LEFT)
var_vertical = tk.BooleanVar()
check_vertical = tk.Checkbutton(frame_options, text="垂直翻转", variable=var_vertical)
check_vertical.pack(side=tk.LEFT)

# 创建开始按钮
button_start = tk.Button(root, text="开始", width=20, command=start_flip)
button_start.pack(pady=10)

root.mainloop()
