class Parsers:
    @staticmethod
    def try_parse_int(some_str):
        try:
            int(some_str)
            return True
        except Exception:
            return False

    @staticmethod
    def try_parse_double(some_str):
        try:
            float(some_str)
            return True
        except Exception:
            return False