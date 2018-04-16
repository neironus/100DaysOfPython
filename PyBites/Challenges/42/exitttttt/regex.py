import re


def extract_course_times():
    '''Use re.findall to capture all mm:ss timestamps in a list'''
    flask_course = ('Introduction 1 Lecture 01:47'
                    'The Basics 4 Lectures 32:03'
                    'Getting Technical!  4 Lectures 41:51'
                    'Challenge 2 Lectures 27:48'
                    'Afterword 1 Lecture 05:02')

    return re.findall(r'\d+:\d+', flask_course)


def split_on_multiple_chars():
    '''Use re.split to split log line by ; , .
       but not on the last ... so list should have len of 4
       (hint check re.split docs for extra switches)'''
    logline = ('2017-11-03T01:00:02;challenge time,regex!.'
               'hope you join ... soon')
    # they will be a maximum of 3+1 string in the list
    m = re.split(r';|,|\.', logline, 3)
    print(m)
    return m


def get_all_hashtags_and_links():
    '''Use re.findall to extract the URL and 2 hashtags of this tweet'''
    tweet = ('New PyBites article: Module of the Week - Requests-cache '
             'for Repeated API Calls - http://pybit.es/requests-cache.html '
             '#python #APIs')

    m = re.findall(r'((?:#|http)\S+)', tweet)
    print(m)
    return m


def match_first_paragraph():
    '''Use re.sub to extract the content of the first paragraph (excl tags)'''
    html = ('<p>pybites != greedy</p>'
            '<p>not the same can be said REgarding ...</p>')

    m = re.match(r'<p>(.*?)</p>', html)
    print(m.groups()[0])
    return m.groups()[0]


def find_double_words():
    '''Use re.search(regex, text).group() to find the double word'''
    text = 'Spain is so nice in the the spring'
    m = re.search(r'(\b\w+)\s+\1', text)

    return m.group()


def match_ip_v4_address(ip):
    '''Use re.match to match an ip v4 address (no need for exact IP ranges)'''
    # m = re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ip)
    m = re.match(r'(\d{1,3}\.){3}\d{1,3}', ip)
    return m
