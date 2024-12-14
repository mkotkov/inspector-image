import argparse
from PIL import Image
from stegano import lsb # type: ignore
import exifread # type: ignore

def extract_metadata(image_path):
    """Извлечение метаданных EXIF из изображения."""
    with open(image_path, 'rb') as img_file:
        tags = exifread.process_file(img_file)
        gps_info = {}
        for tag in tags.keys():
            if tag.startswith("GPS"):
                gps_info[tag] = tags[tag]
        return gps_info

def extract_steganography(image_path):
    """Извлечение скрытой информации из изображения."""
    secret = lsb.reveal(image_path)
    return secret

def main():
    parser = argparse.ArgumentParser(description="Image analysis tool")
    parser.add_argument("-map", type=str, help="Extract GPS metadata")
    parser.add_argument("-steg", type=str, help="Extract hidden information")
    args = parser.parse_args()

    if args.map:
        metadata = extract_metadata(args.map)
        lat = metadata.get("GPS GPSLatitude")
        lon = metadata.get("GPS GPSLongitude")
        print(f"Lat/Lon: {lat} / {lon}")

    if args.steg:
        secret = extract_steganography(args.steg)
        if secret:
            print(secret)
        else:
            print("No hidden message found!")

if __name__ == "__main__":
    main()