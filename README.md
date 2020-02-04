# python-zxing-zbar-dbr
The Python code is used to compare the barcode recognition rate among [ZXing](https://github.com/oostendo/python-zxing), [ZBar](https://github.com/NaturalHistoryMuseum/pyzbar/), and [Dynamsoft Barcode Reader](https://github.com/dynamsoft-dbr/python-barcode).

## Dataset
The dataset is from https://drive.google.com/uc?id=1uThXXH8HiHAw6KlpdgcimBSbrvi0Mksf&export=download

## Installation and Usage

### ZXing

Installation

1. Build the ZXing source code

    ```
    git clone https://github.com/zxing/zxing.git
    cd zxing
    mvn install
    cd javase 
    mvn package assembly:single -DskipTests
    ```

2. Get the source code of Python ZXing:

    ```
    git clone https://github.com/oostendo/python-zxing.git
    cd python-zxing
    ```

3. Open `zxing\__init__.py` and replace the lib file with the `javase-3.4.1-SNAPSHOT-jar-with-dependencies.jar` file built from the source code:

    ```py
    libs = ["javase/target/javase-3.4.1-SNAPSHOT-jar-with-dependencies.jar"]
    ```

4. Build and install the Python ZXing module:

    ```
    python setup.py build install
    ```


Usage

```py
import zxing
reader = zxing.BarCodeReader('<ZXing Project>') # Set the ZXing project directory
barcode = reader.decode('file:///' + image.replace('\\', '/'))
print('{}'.format(barcode.data.rstrip())))
```

### ZBar

Installation

```
pip install pyzbar
```

Usage

```py
import pyzbar.pyzbar as zbar
barcode = zbar.decode(Image.open(image))
print('{}'.format(barcode[0].data.decode("utf-8"))
```

### Dynamsoft Barcode Reader

Installation

```
pip install dbr
```

Usage

```py
from dbr import DynamsoftBarcodeReader
reader = DynamsoftBarcodeReader()
reader.InitLicense('LICENSE-KEY') # Get the license from https://www.dynamsoft.com/CustomerPortal/Portal/Triallicense.aspx
try:
    results = reader.DecodeFile(image)
    textResults = results["TextResults"]
    resultsLength = len(textResults)
    if resultsLength > 0:
        for textResult in textResults:
            print('{}'.format(textResult["BarcodeText"]))
    else:
        print("No barcode detected")
except Exception as err:
    print(err)
```

