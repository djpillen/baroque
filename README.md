# baroque
BAroQUe: Bentley Audiovisual Quality control Utility

The **Bentley Audiovisual Quality control Utility (BAroQUe)** is a Python 3-based Command Line Interface (CLI) computer program primarily intended for in-house use. It performs Quality Control (QC)--with microservices for: 1) file naming and organization; 2) METS validation and verification; 3) WAV BEXT chunk validation and verification; 4) file format validation; and 5) checksum verification--for audio (and, eventually, video) digitized by vendors according to Bentley specifications.

## Use
BAroQUe is implemented in `baroque.py`, which is a command line script that takes as its input 3 arguments:
- The path to a source_directory that corresponds to either a shipment, a collection, or an item directory
- The path to a destination directory where reports and logs will be stored
- The validation action to be run against the source directory

Available actions include:
|Argument | Description |
| --- | --- |
| -d, --directories | Validate directory structure |
| -m, --mets | Validate METS XML |
| -w, --wav | Validate WAV BEXT Chunks
| -f, --files | Validate files |
| -c, --checksums | Validate checksums |

An example command to validate directory structure might look like:

`baroque.py /path/to/shipment /path/to/reports -d`

BAroQUe will run the validation steps and output a report, including errors, in the specified destination_directory
