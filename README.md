## MBP2011 Fix
A program to temporarily fix the Macbook Pro 2011 GPU errors by forcing the use of Intel Integrated graphics rather than
the failing AMD GPU. 

## How do I use this program to fix my laptop?

This is **not** a fix, it only temporarily resolves the issue, allowing you to actually use your machine.

You can use Curl to download the programs from this repository, or Git Clone: <br /> 
_curl -o program.py https://github.com/Elliot-Potts/MBP-2011-AMD-GPU-Quickfix/main.py_
or <br />
_https://github.com/Elliot-Potts/MBP-2011-AMD-GPU-Quickfix.git_

then see below on usage options.

## Parameters and usage options
Downloading and running the program was described above. Use the following information to operate the program.
<br />
<br />
**Parameters** <br /> <br />
_python main.py -move_ <br />
This will apply the quickfix, which means Intel Integrated graphics will now be forced.

<br />
<i>python main.py -undo</i>
<br />
This will undo the quickfix. This will move the framework files back where they belong, undoing the patch.

