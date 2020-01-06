from PIL import Image, ImageDraw, ImageFont

if __name__ == '__main__':
    # 配置字体
    font = ImageFont.truetype('font/SourceHanSansCN-Bold.otf', 20) # 参数：字体名，字体大小
    # 打开图片
    # img = Image.open('img.png').convert('RGBA')
    # 创建图片
    img = Image.new('RGBA', (500, 500), '#cdcdcd')
    # 绘制文字
    ImageDraw.Draw(img).text((10, 10), '测试文字测试文字测试文字\n测试文字测试文字', font=font, fill='#666666') # 参数：文字位置，文字内容， 字体样式， 填充颜色
    img.show()

