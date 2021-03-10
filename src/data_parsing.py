from dataclasses import dataclass

import pandas as pd

from src.user_input import UserInput


@dataclass
class CountyData:
    """
    Class to hold all county data in one spot
    """
    general_data: pd.DataFrame
    case_data: pd.DataFrame


def parse_county_data(user_input: UserInput) -> CountyData:
    """
    Parses given files into pandas dataframes
    :param user_input: Input from user that parsing may need
    :return: Dataframes of general and case data
    """
    # Assume file validity has already been checked
    gen_data: pd.DataFrame = pd.read_csv(user_input.county_general_filepath)
    case_data: pd.DataFrame = pd.read_csv(user_input.county_cases_filepath)
    return CountyData(general_data=gen_data, case_data=case_data)
