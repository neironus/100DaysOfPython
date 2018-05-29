from collections import Counter

import feedparser
import plotly
import plotly.graph_objs as go


def transpose_list_to_tuples(datas):
    if isinstance(datas, dict):
        datas = datas.items()

    return list(zip(*datas))


def main():
    url = 'https://feeds.feedburner.com/fstoppers/articles'

    datas = feedparser.parse(url)

    tags = [tag.term.lower() for entry in datas['entries'] for tag in entry.tags]
    cnt = Counter(tags).most_common(10)

    labels, values = transpose_list_to_tuples(cnt)

    pie = go.Pie(labels=labels, values=values)
    plotly.offline.plot([pie], filename='tst')


if __name__ == '__main__':
    main()
