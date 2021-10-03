from os import PathLike
from typing import Any, Union

from loguru import logger

from .line_parsers.hy3 import LINE_PARSERS
from .schemas import ParsedHytekFile

StrOrBytesPath = Union[
    str, bytes, PathLike[str], PathLike[bytes]
]  # from python/typeshed


def parse_hy3(
    file: StrOrBytesPath, validate_checksums: bool = False, default_country: str = "USA"
) -> ParsedHytekFile:
    """Parse a Hytek MeetManager .hy3 file.

    Args:
        file (StrOrBytesPath): A path to the file to parse.
        validate_checksums (bool, optional): Validate line checksums. Defaults to False.
        default_country (str, optional): Default country for meet. Defaults to "USA".

    Returns:
        ParsedHytekFile: The parsed file.
    """
    logger.info(f"Parsing Hytek meet entries file {file!r}.")

    # TODO: Implement checksum validation
    if validate_checksums:
        logger.warning("Checksum validation not implemented, ignoring.")
        validate_checksums = False

    # Set options dict
    opts: dict[str, Any] = {
        "validate_checksums": validate_checksums,
        "default_country": default_country,
    }

    # Read file
    with open(file) as f:
        lines = [line.strip() for line in f]

    # Make sure this is the right kind of file
    if lines[0][0:2] != "A1":
        raise ValueError("Not a Hytek file!")

    # Add terminator to file
    if lines[-1][0:2] != "Z0":
        lines.append("Z0")

    # Start parsing
    parsed_file = ParsedHytekFile()

    for line in lines:
        code = line[0:2]
        logger.debug(code)
        logger.debug(parsed_file)

        try:
            parsed_file = LINE_PARSERS[code](line, parsed_file, opts)
        except KeyError:
            logger.warning(f"Invalid line code: {code}")
            continue
        except ValueError:
            logger.exception("Error parsing line!")
            continue

    return parsed_file
