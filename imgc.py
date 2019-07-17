# __Author__: NOLA
# __Date__: 2019/6/18

from PIL import Image
import os


def img_cuts(rt_dir, dir_name, ):
    save_option = []
    file_list = os.listdir(rt_dir)
    save_option.append(dir_name)

    try:
        os.makedirs(dir_name)
    except FileExistsError:
        pass

    # noinspection PyBroadException
    try:
        for i in range(0, len(file_list)):
            path = os.path.join(rt_dir, file_list[i])
            file_name = path.split("\\")[1]
            if os.path.isfile(path):
                img = Image.open(path)
                # print("size", img.size)
                cropped = img.crop((0, 0, 800, 379))
                cropped.save(save_option[0] + "/" + file_name)
    except Exception as e:
        print(e)
        pass


root_dir = "./src_img"
target_dir = "modified_img"

if __name__ == "__main__":
    img_cuts(root_dir, target_dir)
