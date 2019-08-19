import argparse

from baroque.baroque_project import BaroqueProject
from baroque.directory_validation import validate_directories
from baroque.mets_validation import validate_mets
from baroque.wav_bext_chunk_validation import validate_wav_bext_chunks
from baroque.file_format_validation import validate_file_formats
from baroque.checksum_validation import validate_checksums
from baroque.report_generation import generate_reports


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="Path to source directory")
    parser.add_argument("destination", help="Path to destination for reports")
    parser.add_argument("-d", "--directories", action="store_true", help="Validate directories")
    parser.add_argument("-m", "--mets", action="store_true", help="Validate METS")
    parser.add_argument("-w", "--wav", action="store_true", help="Validate WAV BEXT chunks")
    parser.add_argument("-f", "--files", action="store_true", help="Validate file formats")
    parser.add_argument("-c", "--checksums", action="store_true", help="Validate checksums")
    args = parser.parse_args()

    project = BaroqueProject(args.source, args.destination)
    if args.d:
        validate_directories(project)
    if args.m:
        validate_mets(project)
    if args.w:
        validate_wav_bext_chunks(project)
    if args.f:
        validate_file_formats(project)
    if args.c:
        validate_checksums(project)

    generate_reports(project)


if __name__ == "__main__":
    main()
