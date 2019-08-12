# pip install pillow
# Need imagemagick installed (http://docs.wand-py.org/en/0.5.4/guide/install.html)
# Need ffmpeg (ffprobe) installed
# pip install wand
# pip install filetype
import os
import platform
import time
import datetime
import argparse
from PIL import Image
from PIL.ExifTags import TAGS
from wand.image import Image as wand_img
import filetype  # To decide whether a file is valid or not
import filecmp  # To identify duplicate files (byte-by-byte analysis)
import subprocess  # To execute commands (for ffprobe)
import json  # To deserialise JSON
import shlex  # To split up the arguments for ffmpeg
import shutil # To support copying of files and their metadata

# Images Dictionary Layout:
# key = full path of image
# images[key][0] = year
# images[key][1] = month
# images[key][2] = day
# images[key][3] = time


def convert_image(source_path, old_extension):
    kind = filetype.guess(source_path)
    if "video" not in kind.mime:  # ImageMagick converts frames of videos to images, not desirable
        destination_path = source_path.replace(old_extension, '.jpg')
        with wand_img(filename=source_path) as img:
            img.format = 'jpg'
            img.save(filename=destination_path)
        print("Converting " + source_path + " to JPG...")
        os.remove(source_path)
        return file.replace(old_extension, '.jpg')
    else:
        raise TypeError("Video files cannot be converted.")


def valid_file(file_path):
    kind = filetype.guess(file_path)
    if kind is None:
        print("Invalid", file_path)
        return False
    else:
        return True


def get_field(exif, field):
    try:
        for (tag, value) in exif.items():
            if TAGS.get(tag) == field: # If the photo has EXIF with correct tags
                return value # If the photo has EXIF with correct tags
        return 0 # If the photo has EXIF, with incorrect tags
    except AttributeError: # If there is no EXIF data
        return 0


def retrieve_creation_date(current_path):
    if platform.system() == 'Windows':
        return os.path.getmtime(current_path)
    else:
        stat = os.stat(current_path)
        try:
            return stat.st_birthtime
        except AttributeError:
            # No easy way to get creation dates on Linux
            # so we'll settle for the last time it was modified
            return stat.st_mtime

def get_time_taken_video(video_path):
    cmd = "ffprobe -v quiet -print_format json -show_entries stream_tags=creation_time:format_tags=creation_time"
    args = shlex.split(cmd)
    args.append(video_path)
    ffprobe_output = subprocess.check_output(args).decode('utf-8')
    ffprobe_output = json.loads(ffprobe_output)
    try:
        time_taken = ffprobe_output['format']['tags']['creation_time']
    except KeyError:
        print("Fail")
        return None

    print("Success")
    time_taken = ffprobe_output['format']['tags']['creation_time']
    # Example output: 2018-07-20T15:37:00.000000Z

    # Convert into a DateTime object
    if platform.system() == 'Windows':
        time_taken = datetime.datetime.strptime(time_taken, '%Y-%m-%dT%H:%M:%S.000000Z')
    else:
        time_taken = datetime.datetime.strptime(time_taken, '%Y-%m-%d %H:%M:%S')
    print(time_taken)
    return time_taken


def format_exif(exif_date):
    year = exif_date[:4]
    month = exif_date[5:7]
    day = exif_date[8:10]
    time = exif_date[11:16].replace(':', '')

    return year, month, day, time


def format_created_date(created_date):
    year = created_date.strftime("%Y")
    month = created_date.strftime("%m")
    day = created_date.strftime("%d")
    time = created_date.strftime("%H%M")

    return year, month, day, time


def get_formatted_month(month):
    return {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }[month]


def get_new_path(images, image_num, key, output_path, file_extension):
    # Constructs a path with the year, month and then file name
    return os.path.join(output_path, images[key][0], images[key][1] + " " + get_formatted_month(images[key][1]),
                        images[key][2] + " " + get_formatted_month(images[key][1]) + " " + images[key][0] + " " +
                        images[key][3] + ("_" + image_num if image_num else "") + file_extension)
                        # Coalescing the number if there are duplicates (last line)


def get_key_format(parent_dir, image_name):
    return os.path.join(parent_dir, image_name)


def get_file_from_key(key):
    return os.path.basename(key)


def create_folder(images, output_path, key):
    try:
        os.makedirs(os.path.join(output_path, images[key][0], images[key][1] + " " + get_formatted_month(images[key][1])))
    except FileExistsError:
        pass


def action_file(images, output_path, key, file_extension, copy_files):
    source = key
    destination = get_new_path(images, None, key, output_path, file_extension)
    num = 1  # Counter for number after image
    same_file = False
    while os.path.exists(destination):
        same_file = filecmp.cmp(source, destination)
        if not same_file:
            num = num + 1
            destination = get_new_path(images, str(num), key, output_path, file_extension)
        else:  # If there are duplicate files
            if copy_files:
                break
            else:
                os.remove(source)  # Remove the duplicate file
                break
    if not same_file:  # Only move files that aren't duplicate
        if copy_files:
            shutil.copy2(source, destination)
        else:
            os.rename(source, destination)


def reject_file(key, file, output_path, copy_files):
    invalid_dir = os.path.join(output_path, "invalid")
    try:
        os.makedirs(invalid_dir)
    except FileExistsError:
        pass
    if copy_files:
        shutil.copy2(key, invalid_dir)
    else:
        os.rename(key, os.path.join(invalid_dir, file))


# Construct the argument parser and parse the arguments provided
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
                help="path to the input folder of images/videos")
ap.add_argument("-o", "--output", required=True,
                help="path to the organised, output folder")
ap.add_argument("-c", "--copy", required=False, action="store_true",
                help="specify if the photos should be copied and not moved")
ap.add_argument("-l", "--del-live-photos", required=False, action="store_true",
                help="specify whether to delete apple live photos")
ap.add_argument("-r", "--reject-modification-date", required=False, action="store_true",
                help="use if modification/creation date of files is incorrect")
args = vars(ap.parse_args())
print(args)

input_path = args["input"]
output_path = args["output"]
copy_files = args["copy"]
del_live_photos = args["del_live_photos"]
reject_mdate = args["reject_modification_date"]

images = {}
valid = True

# Import file names and EXIF data
for files in os.walk(input_path):
    for file in files[2]:
        valid = True
        parent_dir = files[0]
        file_extension = os.path.splitext(file)[1]
        current_path = os.path.join(parent_dir, file)
        if os.path.exists(current_path):  # Protects against files being deleted
            live_photo_path = current_path.replace(file_extension, '.MOV')
            if del_live_photos and os.path.exists(live_photo_path) and file_extension.lower() == '.heic':
                print("Deleting " + live_photo_path + " as it is a live photo...")
                os.remove(live_photo_path)
            if file_extension.lower() != '.jpg':  # If the image is not a JPG
                try:
                    file = convert_image(current_path, file_extension)  # Try to convert it to JPG
                except:  # If the file is not supported
                    valid = False
            if valid:
                file_extension = '.jpg'
                current_path = os.path.join(parent_dir, file)  # Update the path in case the image has been converted
                try:
                    image = Image.open(current_path)
                    exif_data = image._getexif()
                    image.close()
                except OSError: # If the file has no EXIF data
                    valid = False
                    exif_data = ""
                if get_field(exif_data, 'DateTime') != 0:  # If the image has sufficient EXIF data, use that
                    date = get_field((exif_data), 'DateTime')
                    # Use the entire path as a key (so duplicate names in different paths aren't overwritten)
                    images[current_path] = format_exif(date)
                elif not reject_mdate:  # If not, use the creation time
                    date = time.ctime(retrieve_creation_date(current_path))
                    date = datetime.datetime.strptime(date, "%a %b %d %H:%M:%S %Y")
                    images[current_path] = format_created_date(date)
                else:  # If the creation/modification time should be rejected
                    reject_file(current_path, file, output_path, copy_files)
                    valid = False

            elif (file_extension.lower() == ".mov" or file_extension.lower() == ".mp4") and \
                    get_time_taken_video(current_path) is not None:
                time_taken = get_time_taken_video(current_path)
                images[current_path] = format_created_date(time_taken)
                valid = True
            elif valid_file(current_path):  # If the file is not an image, but is still accepted e.g. a video file
                if not reject_mdate:
                    valid = True
                    date = time.ctime(retrieve_creation_date(current_path))
                    date = datetime.datetime.strptime(date, "%a %b %d %H:%M:%S %Y")
                    images[current_path] = format_created_date(date)
                else:  # If the creation/modification time should be rejected for other valid files
                    reject_file(current_path, file, output_path, copy_files)
                    valid = False

            if valid:  # If the image is valid after conversion/checks
                #  Call functions here
                create_folder(images, output_path, current_path)
                action_file(images, output_path, current_path, file_extension, copy_files)
