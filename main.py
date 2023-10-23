import os
import argparse
from pypdf import PdfReader, PdfWriter


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Replace PDF Title Metadata with File Name")

    parser.add_argument('filepath', type=str, help='Input File Path')

    args = parser.parse_args()

    reader = PdfReader(args.filepath)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    metadata = reader.metadata
    writer.add_metadata(metadata)

    directory = os.path.dirname(args.filepath)
    filename_with_extension = os.path.basename(args.filepath)
    filename = os.path.splitext(filename_with_extension)[0]

    writer.add_metadata(
        {
            "/Author": "ZingerBee",
            "/Title": filename,
            "/Creator": "ZingerBee",
        }
    )

    with open(os.path.join(directory, f"{filename}-copy.pdf"), "wb") as f:
        writer.write(f)
