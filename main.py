import sys
from metadata import get_metadata, extract_coordinates
from steg import extract_steg_message


def format_pgp_key(message):
    lines = [message[i:i+64] for i in range(0, len(message), 64)]
    return "\n".join(lines)

def main():
    

    if len(sys.argv) < 3:
        print("Usage: python main.py -option image_path")
        print("Options:")
        print("  -map   Extract GPS coordinates from image metadata")
        print("  -steg  Extract hidden message (e.g., PGP key) from the image")
        return

    # Получаем аргументы командной строки
    option, image_path = sys.argv[1], sys.argv[2]

    # Вариант: извлечение GPS координат
    if option == "-map":
        metadata = get_metadata(image_path)
        gps_info = metadata.get('GPSInfo', {})
        coordinates = extract_coordinates(gps_info)
        if coordinates:
            print(f"Lat/Lon: {coordinates}")
        else:
            print("No GPS data found.")

    # Вариант: извлечение скрытого сообщения
    elif option == "-steg":
        message = extract_steg_message(image_path)
        if message:
            # formatted_body = format_pgp_key(message.strip())
            formatted_message = f"-----BEGIN PGP PUBLIC KEY BLOCK-----\n{message}\n-----END PGP PUBLIC KEY BLOCK-----"
            print(f"{formatted_message}\n")
        else:
            print("No hidden message found.")


    # Если флаг некорректный, выводим сообщение об ошибке
    else:
        print("Invalid option. Use -map or -steg.")

# Запускаем главный модуль
if __name__ == "__main__":
    main()
