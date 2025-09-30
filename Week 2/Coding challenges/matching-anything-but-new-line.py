regex_pattern = r'^.{3}\..{3}\..{3}\..{3}$'
# regex_pattern = r'^.{3}(\..{3}){3}$' #refactored version
import re

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())