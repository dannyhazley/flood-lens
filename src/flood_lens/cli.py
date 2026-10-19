import argparse
from importlib.metadata import version


def main(argv=None):
    parser = argparse.ArgumentParser(description="Flood Lens")

    parser.add_argument(
        "--version",
        action="version",
        version=version("flood-lens"),
    )
    parser.add_argument("--location", required=True)

    args = parser.parse_args(argv)
    print(f"Checking flood risk for {args.location}")
