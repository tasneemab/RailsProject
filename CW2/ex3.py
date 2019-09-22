from urllib.parse import urlparse


def url_parser(link):
    scheme = link.find(':')
    netloc = scheme + 3 + link[scheme + 3:].find('/')
    dictionary = {'scheme': link[:scheme], 'netloc': link[scheme + 3:netloc], 'path': link[netloc:-1]}
    return dictionary


def urlparser():
    parsed = urlparse('https://google.com/ProjectRails/KISS/')
    dictionary = {'scheme': parsed[0], 'netloc': parsed[1], 'path': parsed[2]}
    return dictionary


def main():
    link = input('Enter a URL link:\n')
    print(url_parser(link))
    print(urlparser())


if __name__ == '__main__':
    main()
