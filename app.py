import argparse
import pyzbar.pyzbar as zbar
from PIL import Image
import zxing
from dbr import DynamsoftBarcodeReader
import time

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", type=str,
        help="path to input image")
    args = vars(ap.parse_args())
 
    image = args["image"]
    if image == None:
        print('Try command: python app.py -i <image_file> ')
        return

    # ZXing
    reader = zxing.BarCodeReader('D:/zxing') # Set the ZXing project directory
    start = time.time()
    barcode = reader.decode('file:///' + image.replace('\\', '/'))
    elapsed_time = time.time() - start
    print('ZXing: {}. Elapsed time: {}ms'.format(barcode.data.rstrip(), int(elapsed_time * 1000)))

    # ZBar
    start = time.time()
    barcode = zbar.decode(Image.open(image))
    elapsed_time = time.time() - start
    print('ZBar: {}. Elapsed time: {}ms'.format(barcode[0].data.decode("utf-8"), int(elapsed_time * 1000)))

    # Dynamsoft Barcode Reader
    reader = DynamsoftBarcodeReader()
    reader.InitLicense('LICENSE-KEY') # Get the license from https://www.dynamsoft.com/CustomerPortal/Portal/Triallicense.aspx
    try:
        start = time.time()
        results = reader.DecodeFile(image)
        elapsed_time = time.time() - start
        textResults = results["TextResults"]
        resultsLength = len(textResults)
        if resultsLength > 0:
            for textResult in textResults:
                print('Dynamsoft Barcode Reader: {}. Elapsed time: {}ms'.format(textResult["BarcodeText"], int(elapsed_time * 1000)))
        else:
            print("No barcode detected")
    except Exception as err:
        print(err)

# Command: python app.py -i <image_file>
if __name__ == "__main__":
    main()