"""Header lists for the `csv.DictReader` when reading Hytek-produced CSVs."""
from csv import DictReader
from functools import partial

EVENT_RESULT_CSV_HEADER = [
    "licensee",
    "meet_manager_info",
    "meet_name",
    "meet_host",
    "meet_other",
    "export_name",
    "unknown_1",
    "event_name",
    "event_header",
    "unknown_2",
    "unknown_3",
    "unknown_4",
    "unknown_5",
    "record_header",
    "record_time",
    "reacord_date_pre",
    "record_date",
    "record_holder",
    "record_team",
    "unknown_6",
    "unknown_7",
    "unknown_8",
    "unknown_9",
    "unknown_10",
    "unknown_11",
    "unknown_12",
    "unknown_13",
    "unknown_14",
    "unknown_15",
    "unknown_16",
    "unknown_17",
    "unknown_18",
    "unknown_19",
    "unknown_20",
    "unknown_21",
    "unknown_22",
    "unknown_23",
    "unknown_24",
    "unknown_25",
    "unknown_26",
    "unknown_27",
    "unknown_28",
    "unknown_29",
    "unknown_30",
    "unknown_31",
    "unknown_32",
    "unknown_33",
    "unknown_34",
    "unknown_35",
    "unknown_36",
    "unknown_37",
    "unknown_38",
    "unknown_39",
    "unknown_40",
    "unknown_41",
    "unknown_42",
    "unknown_43",
    "unknown_44",
    "unknown_45",
    "unknown_46",
    "unknown_47",
    "unknown_49",
    "unknown_50",
    "unknown_51",
    "unknown_52",
    "unknown_53",
    "unknown_54",
    "unknown_55",
    "unknown_56",
    "unknown_57",
    "unknown_58",
    "unknown_59",
    "unknown_60",
    "unknown_61",
    "unknown_62",
    "unknown_63",
    "unknown_64",
    "unknown_65",
    "unknown_66",
    "unknown_67",
    "unknown_68",
    "unknown_69",
    "unknown_70",
    "qualifying_time_1",
    "qualifying_time_1_desc",
    "qualifying_time_2",
    "qualifying_time_2_desc",
    "qualifying_time_3",
    "qualifying_time_3_desc",
    "qualifying_time_4",
    "qualifying_time_4_desc",
    "unknown_71",
    "unknown_72",
    "unknown_73",
    "unknown_74",
    "unknown_75",
    "unknown_76",
    "unknown_77",
    "unknown_78",
    "unknown_79",
    "unknown_80",
    "unknown_81",
    "unknown_82",
    "unknown_83",
    "unknown_84",
    "unknown_85",
    "unknown_86",
    "meet_qualifying_info",
    "unknown_87",
    "unknown_88",
    "unknown_89",
    "unknown_90",
    "unknown_91",
    "header_name",
    "header_age",
    "header_team",
    "header_seed_time",
    "header_prelim_time",
    "unknown_92",
    "unknown_93",
    "swim_type",
    "header_swim_off_required",
    "prelim_place",
    "finals_place",
    "name",
    "age",
    "team",
    "seed_time",
    "seed_time_extra",
    "unknown_94",
    "prelim_time",
    "prelim_time_extra",
    "prelim_time_qualifications",
    "unknown_95",
    "unknown_time",
    "unknown_96",
    "dq_reason",
    "unknown_98",
    "unknown_99",
    "unknown_100",
    "unknown_101",
    "unknown_102",
    "unknown_103",
    "unknown_104",
    "unknown_105",
    "unknown_106",
    "unknown_107",
    "unknown_108",
    "unknown_109",
    "unknown_110",
    "unknown_111",
    "unknown_112",
    "unknown_113",
    "unknown_114",
    "unknown_115",
    "unknown_116",
    "unknown_117",
    "unknown_118",
    "unknown_119",
    "unknown_120",
    "unknown_121",
    "unknown_122",
    "unknown_123",
    "unknown_124",
    "unknown_125",
    "unknown_126",
    "unknown_127",
    "unknown_128",
    "unknown_129",
    "unknown_130",
    "unknown_131",
    "unknown_132",
    "unknown_133",
    "unknown_134",
    "unknown_135",
    "unknown_136",
    "unknown_137",
    "unknown_138",
    "unknown_139",
    "unknown_140",
    "unknown_141",
    "unknown_142",
    "unknown_143",
    "unknown_144",
    "unknown_145",
]

HytekExportCsvReader = partial(DictReader, fieldnames=EVENT_RESULT_CSV_HEADER)

__all__ = ["EVENT_RESULT_CSV_HEADER", "HytekExportCsvReader"]
