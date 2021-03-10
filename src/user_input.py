from dataclasses import dataclass
from typing import List, Union


@dataclass
class UserInput:
    """
    Class that holds any input a user may enter
    """
    county_general_filepath: str
    county_cases_filepath: str


def user_input_request(use_county_files: bool) -> UserInput:
    """
    Get all potential user input
    :param use_county_files: Whether to request county-level files from user
    :return: User input gathered, in one location
    """
    user_input: UserInput = UserInput("", "")
    if use_county_files:
        user_input.county_general_filepath = _request_file(desc="General County Data", extension="csv")
        user_input.county_cases_filepath = _request_file(desc="County Case File", extension="csv")
    return user_input


def _request_file(desc: str, extension: Union[str, List[str]]) -> str:
    """
    Gets a file from the user and validates it exists
    :param desc: How the file should be described to the user
    :param extension: File extension must match one of the extensions passed in
    :return: Filepath given by user
    """
    return ""
