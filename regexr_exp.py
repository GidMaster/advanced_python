import re

def main():
    line = 'I think I understand regular expressions.'

    matchResults = re.match('think', line, re.M|re.I)
    if matchResults:
        print(f'Match Found: {matchResult.group()}')
    else:
        print('No Match was found.')

    searchResult = re.search('think', line, re.M|re.I)
    if searchResult:
        print(f'Search Found: {searchResult.group()}')
    else:
        print('No Match was found.')

if __name__ == '__main__':
    main()