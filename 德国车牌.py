
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

# 定义车牌尺寸和颜色
width, height = 520, 110
background_color = (255, 255, 255)  # 白色
blue_color = (0, 51, 153)  # 纯蓝色
border_radius = 10  # 收小圆角半径

# 创建图像和绘制对象
image = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(image)

# 画黑色边框的圆角矩形
draw.rounded_rectangle([(0, 0), (width, height)], radius=border_radius, fill=background_color, outline=(0, 0, 0), width=2)
draw.rounded_rectangle([(3, 3), (width-3, height-3)], radius=border_radius, fill=background_color, outline=(0, 0, 0), width=4)


# 在矩形内绘制色条，确保不遮盖外部矩形
draw.rounded_rectangle([(6, 6), (50, height-7)], radius=border_radius, fill=(0, 51, 153), outline=(0, 51, 153), width=888)

# 加载欧盟图标（JPEG 格式）
eu_icon_path = r"欧盟.jpg"
eu_icon = Image.open(eu_icon_path)

draw.rectangle([(30, 6), (50, 103)], fill=(0, 51, 153))

# 调整图标大小
eu_icon = eu_icon.resize((37, 37))
image.paste(eu_icon, (10, 10))  # 不使用掩模，直接粘贴


# 绘制字母 D，减小字体大小并调整位置
font_size_d = 50  # 字母 D 的新字体大小
font_d = ImageFont.truetype(r'vue01\src\assets\fonts\FE-FONT.TTF', font_size_d)

# 计算 D 的位置
d_x = 13
d_y = 45  # 调整位置使其在欧盟图标正下方

draw.text((d_x, d_y), "D", fill="white", font=font_d)

content = input("输入您的车牌号")  # 示例内容
font_size_content = 90  # 内容的字体大小
font_content = ImageFont.truetype(r'vue01\src\assets\fonts\FE-FONT.TTF', font_size_content)

# 计算内容位置
text_x = 50  # 左侧内容的起始位置
text_y = 11   # 垂直居中的位置

# 添加内容
draw.text((text_x, text_y), content, fill="black", font=font_content)

# 显示车牌
plt.imshow(image)
plt.axis('off')  # 关闭坐标轴
plt.show()

# 保存图像
image.save(r'D:\license_plate.PNG')
