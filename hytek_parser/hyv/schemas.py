from datetime import date

from attrs import define

from hytek_parser.hy3.enums import Course, Gender
from hytek_parser.hyv.enums import ChampionshipEventType, SwimmersEventType


@define
class EventExport:
    """An exported event in an HYV file."""

    number: int
    championship_type: ChampionshipEventType
    swimmer_type: SwimmersEventType
    gender: Gender

    min_age: int
    max_age: int
    open_: bool

    distance: int
    num_heats_maybe: int

    unknown1: str
    unknown2_time: str
    unknown3: str
    unknown4: str
    unknown5: str
    unknown6_time: str
    unknown7: str
    unknown8_time: str
    unknown9: str
    unknown10: str


@define
class ParsedEventHyvFile:
    """A Parsed Event Entries HYV file."""

    meet_name: str
    meet_course: Course
    meet_pool: str

    meet_start_date: date
    meet_end_date: date
    meet_date_other: date

    file_software_vendor: str
    file_software_version: str

    file_unknown_space_7: str
    file_unknown_code: str
    file_unknown_id: str

    events: list[EventExport]
