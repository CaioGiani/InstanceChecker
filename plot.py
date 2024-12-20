import os
from PIL import Image, ImageDraw, ImageFont
import shutil
import tqdm

colorIndex = ('#FF3838', '#FF9D97', '#FF701F', '#FFB21D', '#CFD231', '#48F90A', '#92CC17', '#3DDB86', '#1A9334', '#00D4BB',
              '#2C99A8', '#00C2FF', '#344593', '#6473FF', '#0018EC', '#8438FF', '#520085', '#CB38FF', '#FF95C8', '#FF37C7')
categoryIndex = ('Smoke Detector','Alarm Button','Fire Extinguisher', 'Ceiling Light',
                 'FM Power Point (Plug)', 'Command Point (Switch)','Security Cameras')
Image.MAX_IMAGE_PIXELS = None

def readText(path):
    AnnotationDict = {}
    with open(path, 'r') as f:
        lines = f.read()
    for i,line in enumerate(lines.split('\n')):
        if line:
            line = line.split(' ')
            if len(line) == 5:                          #for rectangle, category:str, x:float, y, w, h of the annotation
                category = int(line[0])
                x = float(line[1])
                y = float(line[2])
                w = float(line[3])
                h = float(line[4])
                AnnotationDict[i] = [category, x, y, w, h]
            elif len(line) == 6:                         #for oriented box and ellipse, category:str, x:float, y, w, h, theta:int of the annotation
                category = int(line[0])
                x = float(line[1])
                y = float(line[2])
                w = float(line[3])
                h = float(line[4])
                theta = int(line[5])
                AnnotationDict[i] = [category, x, y, w, h, theta]
            elif len(line) >= 9 and len(line) % 2 == 1:                 #for multi-side polygon, category:str, x1:float, y1, x2, y2, x3, y3, ... of the annotation
                category = int(line[0])
                AnnotationDict[i] = [category]
                AnnotationDict[i].extend([float(x) for x in line[1:]])
    # print(f'processing {path}, got {len(AnnotationDict)} annotations')
    return AnnotationDict

def annotateImage(image, annotation, colorIndex=colorIndex, categoryIndex=categoryIndex, resize=True):
    w,h = image.size
    image_anno = image.copy()
    if resize:
        ratio = 1024 / max(w, h)
        w = int(w * ratio)
        h = int(h * ratio)
        image_anno = image_anno.resize((w, h), Image.Resampling.LANCZOS)
        
    draw = ImageDraw.Draw(image_anno)
    for key in annotation:
        category = annotation[key][0]
        color = colorIndex[category % len(colorIndex)]

        if len(annotation[key]) == 5:
            x = annotation[key][1] * w
            y = annotation[key][2] * h
            w_box = annotation[key][3] * w
            h_box = annotation[key][4] * h
            xmin = x - w_box // 2
            ymin = y - h_box // 2
            xmax = x + w_box // 2
            ymax = y + h_box // 2
            draw.rectangle([xmin, ymin, xmax, ymax], outline=color, width=5)
        
        elif len(annotation[key]) == 6:
            pass

        elif len(annotation[key]) >= 9 and len(annotation[key]) % 2 == 1:
            point = []
            box = []
            for i in range(1, len(annotation[key]), 2):
                x = int(annotation[key][i] * w)
                y = int(annotation[key][i+1] * h)
                point.extend([x, y])
            xmin = min(point[::2])
            ymin = min(point[1::2])
            xmax = max(point[::2])
            ymax = max(point[1::2])
            box = [xmin, ymin, xmax, ymax]
            draw.rectangle(box, outline=color, width=1)
            draw.polygon(point, outline=color, width=5)
        # print('category: ', category)
        # print(xmin, ymin, xmax, ymax)
        fontsize = 15
        x_text = xmin
        y_text = ymin-fontsize if ymin > fontsize else ymin
        text = categoryIndex[category]
        
        font = ImageFont.truetype("arial.ttf", fontsize)
        text_bbox = draw.textbbox((x_text, y_text-2), text, font=font)
        text_background = [text_bbox[0], text_bbox[1], text_bbox[2], text_bbox[3]]
        draw.rectangle(text_background, fill=color)
        draw.text((x_text, y_text), text, fill="black", font=font)
    return image_anno

def annotateImage_fullpoly(image, annotation, colorIndex=colorIndex, categoryIndex=categoryIndex, resize=True):
    w,h = image.size
    image_anno = image.copy()
    if resize:
        ratio = 1024 / max(w, h)
        w = int(w * ratio)
        h = int(h * ratio)
        image_anno = image_anno.resize((w, h), Image.Resampling.LANCZOS)
        
    draw = ImageDraw.Draw(image_anno)
    for key in annotation:
        category = annotation[key][0]
        color = colorIndex[category % len(colorIndex)]

        if len(annotation[key]) == 5:
            x = annotation[key][1] * w
            y = annotation[key][2] * h
            w_box = annotation[key][3] * w
            h_box = annotation[key][4] * h
            xmin = x - w_box // 2
            ymin = y - h_box // 2
            xmax = x + w_box // 2
            ymax = y + h_box // 2
            draw.rectangle([xmin, ymin, xmax, ymax], outline=color, width=5, fill=color)
        
        elif len(annotation[key]) == 6:
            pass

        elif len(annotation[key]) >= 9 and len(annotation[key]) % 2 == 1:
            point = []
            box = []
            for i in range(1, len(annotation[key]), 2):
                x = int(annotation[key][i] * w)
                y = int(annotation[key][i+1] * h)
                point.extend([x, y])
            draw.polygon(point, outline=color, width=5, fill=color)
    return image_anno

def makeLegend(colorIndex, categoryIndex, BlackBackground=False):
    legend = Image.new('RGB', (200, 1000), (255, 255, 255))
    draw = ImageDraw.Draw(legend)
    fontsize = 15
    font = ImageFont.truetype("arial.ttf", fontsize)
    fill_txt = 'black'
    if BlackBackground:
        fill_txt = 'white'
        draw.rectangle([0, 0, 200, 1000], fill="black")
    for i, category in enumerate(categoryIndex):
        color = colorIndex[i % len(colorIndex)]
        y = i * fontsize * 2
        draw.rectangle([0, y, 20, y + fontsize], fill=color)
        draw.text((30, y), category, fill=fill_txt, font=font)
    return legend

def plot_PolygonsInFolder(dir_path, colorIndex=colorIndex, categoryIndex=categoryIndex, resize=True, fillPoly=False):
    image_list = [f for f in os.listdir(dir_path) if f.endswith(('.jpg', '.png', '.jpeg', 'JPG', 'PNG', 'JPEG'))]
    number_of_label = 0
   
    output_dir = os.path.join(dir_path, 'output')
    os.makedirs(output_dir, exist_ok=True)
    print('output_dir: ', output_dir)
    print('outputting images...')
    for image_name in tqdm.tqdm(image_list, desc="Processing images"):
        label_name = os.path.splitext(image_name)[0] + '.txt'
        label_path = os.path.join(dir_path, label_name)
        output_image_path = os.path.join(output_dir, image_name)
        if not os.path.exists(label_path):
            #copy image to output folder
            shutil.copy(os.path.join(dir_path, image_name), output_image_path)
            continue
        number_of_label += 1
        image_path = os.path.join(dir_path, image_name)
        image = Image.open(image_path)
        image = image.convert('RGB')
        annotations = readText(label_path)
        if fillPoly:
            image_anno = annotateImage_fullpoly(image, annotations, categoryIndex=categoryIndex, resize=resize)
        else:
            image_anno = annotateImage(image, annotations, categoryIndex=categoryIndex, resize=resize)        
        image_anno.save(output_image_path)
    print('number_of_images: ', len(image_list))
    print('number_of_labels: ', number_of_label)
    print('plot done!')

def autoSplitImage_save(image_dir, size_max = 1024):
    image = Image.open(image_dir)
    output_dir = os.path.join(os.path.dirname(image_dir), 'output')
    os.makedirs(output_dir, exist_ok=True)
    w, h = image.size
    if w <= size_max and h <= size_max:
        print(f'{image_dir} is smaller than {size_max}, skip')
        #move image to output folder
        output_image_path = os.path.join(output_dir, os.path.basename(image_dir))
        image.save(output_image_path)
        return
    else:
        # print(f'{image_dir} is larger than {size_max}, splitting...')
        w_split = w // size_max + 1 if w % size_max != 0 else w // size_max
        h_split = h // size_max + 1 if h % size_max != 0 else h // size_max
        for i in range(w_split):
            for j in range(h_split):
                x0 = i * size_max
                y0 = j * size_max
                x1 = (i + 1) * size_max
                y1 = (j + 1) * size_max
                if x1 > w:
                    x1 = w
                if y1 > h:
                    y1 = h
                image_crop = image.crop((x0, y0, x1, y1))
                image_crop = image_crop.convert('RGB')
                filename = os.path.basename(image_dir).split('.')[:-1][0]
                filename += f'__split_{i}_{j}_#.jpg'
                output_image_path = os.path.join(output_dir, filename)
                image_crop.save(output_image_path)
        # print(f'{image_dir} is split into {w_split}x{h_split} images')

def autoSplitImageInFolder_save(folder_dir, size_max = 1024):
    image_list = [f for f in os.listdir(folder_dir) if f.endswith(('.jpg', '.png', '.jpeg', 'JPG', 'PNG', 'JPEG'))]
    print('splitting images...')
    for image_name in tqdm.tqdm(image_list, desc="Processing images"):
        image_path = os.path.join(folder_dir, image_name)
        autoSplitImage_save(image_path, size_max=size_max)

def autoUnifyImageInFolder_save(folder_dir):
    output_dir = os.path.join(folder_dir, 'output')
    os.makedirs(output_dir, exist_ok=True)
    allImage_list = [f for f in os.listdir(folder_dir) if f.endswith(('.jpg', '.png', '.jpeg', 'JPG', 'PNG', 'JPEG'))]
    splitFile_list = [f for f in os.listdir(folder_dir) if f.endswith(('_#.jpg', '_#.png', '_#.jpeg', '_#.JPG', '_#.PNG', '_#.JPEG'))]
    nonUnifiedFile_list = [f for f in allImage_list if f not in splitFile_list]
    if len(nonUnifiedFile_list) > 0:
        print('There are non-unified images in the folder: ', len(nonUnifiedFile_list))
        print('move them to output folder...')
        for file in nonUnifiedFile_list:
            shutil.copy(os.path.join(folder_dir, file), os.path.join(output_dir, file))
    bigFile_list = []
    for file in splitFile_list:
        bigFile_name = file.split('__split_')[0]
        if bigFile_name not in bigFile_list:
            bigFile_list.append(bigFile_name)
    print('Having find split images: ', len(splitFile_list))
    print('Which build images: ', len(bigFile_list))
    print('Unifying images...')
    for bigFile_name in tqdm.tqdm(bigFile_list, desc="Processing images"):
        bigFile_path = os.path.join(folder_dir, bigFile_name)
        output_image_path = os.path.join(output_dir, bigFile_name + '.jpg')        
        imageSplit_list = [f for f in splitFile_list if f.startswith(bigFile_name)]
        Image_dict = {}
        W, H = 0, 0
        w_std, h_std, w_min, h_min = 0, 0, 0, 0
        for file in imageSplit_list:
            i, j = map(int, file.split('__split_')[1].split('_')[:2])
            imageSplit = Image.open(os.path.join(folder_dir, file))
            w, h = imageSplit.size
            Image_dict[(i, j)] = imageSplit
            w_std = max(w, w_std)
            h_std = max(h, h_std)
            w_min = min(w, w_std)
            h_min = min(h, h_std)
        W = w_std * i + w_min
        H = h_std * j + h_min
        bigImage = Image.new('RGB', (W, H))
        px, py = 0, 0
        for a in range(0,i+1):
            px = a * w_std
            for b in range(0,j+1):
                py = b * h_std
                bigImage.paste(Image_dict[(a, b)], (px, py))
        bigImage.save(output_image_path)
    print('Unifying done!')
    



if __name__ == '__main__':   
    categoryIndex = ('COL', 'PLT', 'CHR', 'CRU', 'SNE', 'GRA', 'ALV', 'ERO', 'PEL', 'DEL', 'CRA', 'DIS')
  
    # # make legend and save
    # output_dir = r'D:\Kai\Kai_work\OneDrive - Politecnico di Milano\PaperInProcess\2024_lowCost3D\image'
    # legend = makeLegend(colorIndex, categoryIndex, BlackBackground=True)
    # legend.save(os.path.join(output_dir, 'legend_black.png'))

    # # split images
    # folder_dir = r'D:\Kai\Kai_work\000000_TA\2024_fall_arconati\Practice_AI\Orthos'
    # autoSplitImageInFolder_save(folder_dir, size_max = 3072)

    # make annotations on images
    dir_path = r'D:\Kai\Kai_work\000000_TA\2024_fall_arconati\Practice_AI\dataset\images'
    plot_PolygonsInFolder(dir_path, categoryIndex=categoryIndex, resize=False, fillPoly=False)

    # # unify images
    # folder_dir = r'D:\Kai\Kai_work\000000_TA\2024_fall_arconati\Practice_AI\Orthos\output\output'
    # autoUnifyImageInFolder_save(folder_dir)