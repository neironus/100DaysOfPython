import csv
from flask import Flask, render_template
import os
from collections import namedtuple, Counter
from typing import List

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8
from bokeh.models import ColumnDataSource

app = Flask(__name__)
app.config.from_object('config')

accidentTuple = namedtuple('Accident', 'groupe commune')


def get_datas_accidents() -> List[accidentTuple]:
    datas = []

    base_folder = os.path.dirname(__file__)
    full_path = os.path.join(base_folder, 'datas', 'OTC_ACCIDENTS.csv')

    with open(full_path) as f:
        reader = csv.DictReader(f)
        for r in reader:

            if r['COMMUNE'] != 'Genève':  # Remove Genève because too much datas
                datas.append(accidentTuple(r['GROUPE_ACCIDENT'], r['COMMUNE']))

    return datas


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/accidents', methods=['GET'])
def accidents():
    cnt_accidents = Counter(get_datas_accidents()).most_common()

    communes = list(set([accident.commune for accident, cnt in cnt_accidents]))
    communes = sorted(communes, key=lambda x: x)

    datas = {}
    groupe_accident = []

    for accident, cnt in cnt_accidents:

        if accident.groupe not in groupe_accident:
            groupe_accident.append(accident.groupe)

        if accident.groupe not in datas:
            datas[accident.groupe] = {commune: 0 for commune in communes}

        datas[accident.groupe][accident.commune] = cnt

    groupe_accident = sorted(groupe_accident, key=lambda x: x)

    data = {}

    for gr, items in datas.items():
        data[gr] = []

        for commune in communes:
            data[gr].append(items.get(commune))

    colors = ['#9d57d2', '#bcf638', '#bdef8a', '#c235af', '#308ca0', '#cda1d8',
              '#f4e4b9', '#ba2c69', '#441fcd', '#01844b', '#ff0012']

    colors = colors[:len(groupe_accident)]

    data = {
        'commune': communes,
        **data,
    }
    source = ColumnDataSource(data=data)

    fig = figure(x_range=communes, sizing_mode='stretch_both',
                 title='Accidents', toolbar_location=None, tools="")

    fig.vbar_stack(groupe_accident, x='commune', width=1, fill_color=colors,
                   name=groupe_accident, source=source)

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    script, div = components(fig)

    html = render_template(
        'accidents.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources
    )

    return encode_utf8(html)


def main():
    app.run()


if __name__ == '__main__':
    main()
