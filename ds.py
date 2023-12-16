import cv2
import numpy as np
 
 
def restore_image(image, original_size):
 
    # 获取图像的原始宽度和高度
    height, width = original_size
 
    # 计算缩放比例
    scale = min(image.shape[1]/width, image.shape[0]/height)
 
    # 计算缩放后的宽度和高度
    new_width = int(width * scale)
    new_height = int(height * scale)
 
    # 计算填充位置
    x_offset = (image.shape[1] - new_width) // 2
    y_offset = (image.shape[0] - new_height) // 2
 
    # 将调整后的图像放置在原始图像中心
    restored_image = image[y_offset:y_offset + new_height, x_offset:x_offset + new_width]
 
 
    # 调整图像大小
    # restored_image = cv2.resize(restored_image, None,None,1/scale,1/scale,interpolation=cv2.INTER_LANCZOS4)
 
    
    restored_image = cv2.resize(restored_image,(width,height),interpolation=cv2.INTER_LANCZOS4)
 
    return restored_image
 
 
 
def resize_image(image, target_size, fill_value):
    # 获取图像的原始宽度和高度
    height, width = image.shape[:2]
 
    # 计算缩放比例
    scale = min(target_size[0] / width, target_size[1] / height)
 
    # 计算缩放后的宽度和高度
    new_width = int(width * scale)
    new_height = int(height * scale)
    # print(" new_width = {}, new_height = {} ".format(new_width, new_height))
    # 调整图像大小
    resized_image = cv2.resize(image, (new_width, new_height),interpolation=cv2.INTER_LANCZOS4)
 
    # 创建目标大小的空白图像，并填充特定值
    padded_image = np.full((target_size[1], target_size[0], image.shape[2]), fill_value, dtype=np.uint8)
 
    # 计算填充位置
    x_offset = (target_size[0] - new_width) // 2
    y_offset = (target_size[1] - new_height) // 2
 
    # print(" x_offset = {}, y_offset = {} ".format(x_offset, y_offset))
    # 将调整后的图像放置在填充图像中心
    padded_image[y_offset:y_offset + new_height, x_offset:x_offset + new_width] = resized_image
 
    return padded_image
 
 
# 读取图像
image = cv2.imread('1.jpg')
 
# 设置目标大小（这里设置为300x300）
target_size = (512, 512)
 
# 设置填充值
fill_value = 114
 
# 进行图像缩放和填充
resized_image = resize_image(image, target_size, fill_value)
 
 
# 将缩放后的图像恢复到原始大小
restored_image = restore_image(resized_image, (image.shape[0],image.shape[1]))
 
 
cv2.imwrite("1_reszie.jpg",resized_image )
save_params = [cv2.IMWRITE_JPEG_QUALITY, 100]
cv2.imwrite("1_restored.jpg",restored_image,save_params)
# # 显示原始图像和缩放后的图像
# cv2.imshow('Original Image', image)
# cv2.imshow('Resized Image', resized_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
