from src.domain.result.result_error import ResultError


class UserErrors:
    too_short_name: ResultError = ResultError("name", "TOO_SHORT_NAME")
