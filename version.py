import pyinstaller_versionfile
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Generate version file for PyInstaller."
    )
    parser.add_argument("version", type=str, help="Version number (e.g., 0.0.1)")
    args = parser.parse_args()

    pyinstaller_versionfile.create_versionfile(
        output_file="versionfile.txt",
        version=args.version,
        company_name="spoo.me",
        file_description="QR Grabber",
        internal_name="QR Grabber",
        legal_copyright="© spoo.me. All rights reserved.",
        original_filename="qr-grabber.exe",
        product_name="QR Grabber",
    )


if __name__ == "__main__":
    main()
