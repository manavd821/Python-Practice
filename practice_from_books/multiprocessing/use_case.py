import concurrent
import concurrent.futures
import pathlib
import time
from PIL import Image, ImageFilter
start = time.perf_counter()

photos_dir = pathlib.Path('photos')
if not photos_dir.exists():
    print('photos dir does not exists')
    exit(code=1)
image_names = [file.name for file in photos_dir.iterdir() if file.is_file()]

processed_dir = pathlib.Path('processed')
processed_dir.mkdir(exist_ok=True)

size = (1200, 1200)

def process_image(img_name):
        try:
            print(f'{img_name} process start.')
            img_path = photos_dir / img_name
            img = Image.open(img_path)
            img = img.filter(ImageFilter.GaussianBlur(15))
            img.thumbnail(size)
            img.save(processed_dir / img_name)
            print(f'{img_name} process end.')
        except Exception as e:
            print(f'Skipping {img_name}: {e}')
            
if __name__ == '__main__':
    # Synchronous flow
    
    # for img_name in image_names:
    #     try:
    #         print(f'{img_name} process start.')
    #         img_path = photos_dir / img_name
    #         img = Image.open(img_path)
    #         img = img.filter(ImageFilter.GaussianBlur(15))
    #         img.thumbnail(size)
    #         img.save(processed_dir / img_name)
    #         print(f'{img_name} process end.')
    #     except Exception as e:
    #         print(f'Skipping {img_name}: {e}')
    
    # Parallel flow
    
    with concurrent.futures.ProcessPoolExecutor() as executore:
        executore.map(process_image, image_names)
            
    end = time.perf_counter()
    print(f"Finished in {round(end - start, 2)} seconds")