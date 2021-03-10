from src.data_parsing import parse_county_data, CountyData
from src.user_input import UserInput, user_input_request


def main() -> None:
    user_input: UserInput = user_input_request(use_county_files=True)
    county_data: CountyData = parse_county_data(user_input=user_input)


if __name__ == '__main__':
    main()
