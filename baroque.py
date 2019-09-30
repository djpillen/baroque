import argparse

from baroque.baroque_project import BaroqueProject
from baroque.checksum_validation import validate_checksums
from baroque.file_format_validation import validate_file_formats
from baroque.mets_validation import validate_mets
from baroque.report_generation import generate_reports
from baroque.wav_bext_chunk_validation import validate_wav_bext_chunks

from baroque.structure_validation import StructureValidator


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="Path to source directory")
    parser.add_argument("destination", help="Path to destination for reports")
    parser.add_argument("-s", "--structure", action="store_true", help="Validate directory and file structure")
    parser.add_argument("-e", "--export", help="Path to metadata export")
    parser.add_argument("-m", "--mets", action="store_true", help="Validate METS")
    parser.add_argument("-w", "--wav", action="store_true", help="Validate WAV BEXT chunks")
    parser.add_argument("-f", "--files", action="store_true", help="Validate file formats")
    parser.add_argument("-c", "--checksums", action="store_true", help="Validate checksums")
    args = parser.parse_args()

    project = BaroqueProject(args.source, args.destination, args.export)

    if (args.structure or args.mets) and not args.export:
        print("SYSTEM ERROR: metadata export [-e] is required for structure and METS validation")

    if args.structure:
        StructureValidator(project).validate()
    if args.mets:
        validate_mets(project)
    if args.wav:
        validate_wav_bext_chunks(project)
    if args.files:
        validate_file_formats(project)
    if args.checksums:
        validate_checksums(project)

    generate_reports(project)


if __name__ == "__main__":
    print("SYSTEM ACTIVITY: baroque starting")
    main()
    print("SYSTEM ACTIVITY: baroque finished")
