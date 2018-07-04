import json
import sys

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


def parse_json(code, channel='stable', crate_type='bin',
               mode='debug', tests=False):

    json_data = {'channel': channel,
                 'code': content.decode('utf-8'),
                 'crateType': crate_type,
                 'mode': mode,
                 'tests': tests }

    return json_data


def make_request(json_data):
    url = 'http://play.rust-lang.org/execute'
    data = json.dumps(json_data).encode('utf-8')
    response = urlopen(url, data)
    return json.loads(response.read())


if __name__ == '__main__':
    with open(sys.argv[1], 'rb') as raw_data:
        content = raw_data.read()

    json_data = parse_json(content)
    response = make_request(json_data)

    print(response['stderr'])
    print(response['stdout'])
