import os
import argparse
from PIL import Image


def mirror_images_in_folder(folder_path, horizontal_flip=False, vertical_flip=False):
    # 检查文件夹路径是否存在
    if not os.path.isdir(folder_path):
        print("指定的文件夹路径不存在或不合理。")
        return

    # 获取文件夹内所有文件
    files = os.listdir(folder_path)

    # 检查文件夹内是否存在图片文件
    image_files_exist = False
    for file in files:
        # 检查文件是否为图片（这里简单地通过文件后缀进行判断）
        if file.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            image_files_exist = True
            break

    # 如果文件夹内不存在图片文件，则输出提示消息
    if not image_files_exist:
        print("指定路径中不存在图像文件。")
        return

    # 遍历文件夹内的每个文件
    for file in files:
        # 检查文件是否为图片（这里简单地通过文件后缀进行判断）
        if file.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            # 拼接文件的完整路径
            file_path = os.path.join(folder_path, file)

            try:
                # 打开图片文件
                image = Image.open(file_path)

                # 根据选项进行翻转
                if horizontal_flip:
                    image = image.transpose(Image.FLIP_LEFT_RIGHT)
                if vertical_flip:
                    image = image.transpose(Image.FLIP_TOP_BOTTOM)

                # 保存翻转后的图片，覆盖原始图片
                image.save(file_path)

                print(f"{file} 已成功翻转")
            except Exception as e:
                print(f"处理文件 {file} 时出错：{e}")


def main():
    # 创建解析器
    parser = argparse.ArgumentParser(description="Mirror flip images in the specified folder.")

    # 添加命令行选项
    parser.add_argument("-d", "--directory", help="Specify the directory containing images.", default=os.getcwd())
    parser.add_argument("-H", "--horizontal", action="store_true", help="Flip images horizontally.")
    parser.add_argument("-V", "--vertical", action="store_true", help="Flip images vertically.")

    # 解析命令行参数
    args = parser.parse_args()

    # 调用函数对指定文件夹内的图片进行翻转
    mirror_images_in_folder(args.directory, args.horizontal, args.vertical)


if __name__ == "__main__":
    main()
