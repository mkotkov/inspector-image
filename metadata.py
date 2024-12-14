from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_metadata(image_path):
    try:
        img = Image.open(image_path)
        exif_data = img._getexif()
        metadata = {}

        if exif_data:
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                if tag == 'GPSInfo':
                    gps_data = {}
                    for gps_id in value:
                        gps_tag = GPSTAGS.get(gps_id, gps_id)
                        gps_data[gps_tag] = value[gps_id]
                    metadata['GPSInfo'] = gps_data
                else:
                    metadata[tag] = value
        return metadata
    except Exception as e:
        print(f"Error extracting metadata: {e}")
        return None

def extract_coordinates(gps_info):
    def convert_to_degrees(value):
        if isinstance(value, tuple) and len(value) == 3:
            d, m, s = value
            return d + (m / 60.0) + (s / 3600.0)
        return None

    if 'GPSLatitude' in gps_info and 'GPSLongitude' in gps_info:
        lat = convert_to_degrees(gps_info['GPSLatitude'])
        lon = convert_to_degrees(gps_info['GPSLongitude'])
        if gps_info['GPSLatitudeRef'] != 'N':
            lat = -lat
        if gps_info['GPSLongitudeRef'] != 'E':
            lon = -lon
        return lat, lon
    return None
