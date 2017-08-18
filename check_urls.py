import requests
import argparse
import sys


def read_urls_from_file(path):
    '''Returns a list of URLs'''
    url_list = []
    with open(path) as f:
        lines = f.readlines()
        for l in lines:
            url_list.append(l.rstrip())
    return url_list


def get_status_code(url):
    '''Returns the HTTP Status of the request'''
    r = requests.get(url)
    return r.status_code


def parse_options():
    '''Returns a dictionary-like object of command line arguments'''
    parser = argparse.ArgumentParser(description='Test PCC options')
    parser.add_argument('-o', '--output', help='Output file name', default='', dest='logger')
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('-i', '--input', help='Input url file', required=True, dest='url_file')
    args = parser.parse_args()
    return args


def get_current_log(target):
    '''Returns the location of output, either stdout or a file open for writing'''
    log = sys.stdout
    if target:
        log = target and open(target, 'w') or sys.stdout
    return log


def main():
    cmd_args = parse_options()
    url_file = cmd_args.url_file
    url_list = read_urls_from_file(url_file)
    log = get_current_log(cmd_args.logger)

    for url in url_list:
        try:
            code = get_status_code(url)
            if code == 200:
                log.write("\n" + '{0} returned {1}'.format(url,code))
            else:
                log.write("\n" + 'WARNING! {0} returned {1}'.format(url,code))
        except:
            log.write("\n" + 'Invalid URL!')


if __name__ == '__main__':
    main()
