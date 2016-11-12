"""
Get local weather info from Yahoo! Weather
For More Information, see Reference: https://developer.yahoo.com/weather/

"""
import sys
import json
from argparse import ArgumentParser
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

try:
    import urlparse
    from urllib import urlencode
except: # For Python 3
    import urllib.parse as urlparse
    from urllib.parse import urlencode


def get_weather(location):
    args = (('q',"select * from weather.forecast where woeid=" + str(location)), ('format','json'), ('diagnostics', 'true'), ('callback', ''))
    url = "https://query.yahooapis.com/v1/public/yql?" + urlencode(args)

    try:
        html = urlopen(url)
    except Exception:
        return None


    result = html.read().decode('utf-8')
    data = json.loads(result)

    return (data['query']['results']['channel']['title'], data['query']['results']['channel']['item']['condition']['text'])


def create_cli_parser():
    """
    Creates a command line interface parser.
    """

    cli_parser = ArgumentParser(description=__doc__)

    cli_parser.add_argument('location', default="2459115",
        help="The location code for the city. Could get location code via http://woeid.rosselliot.co.nz/lookup/")

    cli_parser.add_argument('-o', '--output', action='store',
        help="output the result to a file",
        default="")

    return cli_parser

def main(argv):
    # Create the command line parser.
    cli_parser = create_cli_parser()
    # Get the options and arguments.
    args = cli_parser.parse_args(argv)

    weather = get_weather(args.location)

    if args.output == '':
        print (weather)
    else:
        # Write info to a file
        try:
            with open(args.output, "w") as output_file:
                output_file.writelines(weather)
        except IOError:
            print ("Unable to open file " + args.output + " for output")




if __name__ == "__main__":
    main(sys.argv[1:])
