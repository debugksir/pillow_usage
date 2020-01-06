from PIL import Image

if __name__ == '__main__':
    # 创建一个RGBA模式下的长256px，宽128px透明图片
    img = Image.new('RGBA', (256, 128), (255,255,255,0)) # 参数：图片模式，图片大小，颜色
    # 图片显示
    img.show()
    # 图片储存
    img.save('img.png') # RGBA模式带透明度对应PNG格式，RGB模式对应JPEG格式
    # 图片转化
    Image.open('img.png').convert('RGB').save('img.jpg')
    # 图片压缩
    img.open('img.jpg').save('img01.jpg', quality=80) # quality对应图片质量，quality值越低图片质量越低占用内存也越低，可视情况而定
    # 图片合成
    img01 = Image.open('img.jpg').convert('RGBA')
    img02 = Image.open('img.png').convert('RGBA')
    Image.alpha_composite(img01, img02).show()


    