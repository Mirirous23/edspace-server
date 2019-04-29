import json
import random

import matplotlib.pyplot as plt;
from django.shortcuts import render

plt.rcdefaults()
import matplotlib.pyplot as plt

from core.dto import Item

colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow", "gray", "firebrick", "lightcoral",
          "cadetblue", "skyblue", "darkseagreen", "lime", "cyan", "indigo", "violet", "navy", "tomato",
          "linen", "coral", "silver", "tan", "olive", "teal"]


def process_items_solr():
    items = read_items_solr()
    objects = list(
        map(lambda item: (item.dc_subject + "-" + item.author)[:50] if len(
            item.dc_subject + "-" + item.author) > 50 else (item.dc_subject + "-" + item.author), items))
    visits = tuple(map(lambda item: int(item.search_resource_id), items))
    colors = tuple(map(lambda item: item.color, items))
    patches, _, texts = plt.pie(visits, colors=colors, autopct='%1.1f%%', )
    for text in texts:
        text.set_color('white')
    plt.legend(patches, objects, loc='best', ncol=2, prop={'size': 6})
    plt.axis('equal')
    plt.tight_layout()
    plt.title('Descargas de Items')
    plt.savefig('static/img/pie_chart_items.png')


def index(request):
    image="pie_chart_items.png"
    return render(request, 'index.html', locals())

def generate_graph(request):
    process_items_solr()
    return render(request, 'index.html', locals())

def read_items_solr():
    try:
        items = []

        with open('data-solr/itemsSolr.json') as json_file:
            data = json.load(json_file)
            for doc in data['response']['docs']:
                item = Item()
                item.author = doc['author'][0] if 'author' in doc else ''
                item.dc_subject = doc['subject'][0] if 'subject' in doc else ''
                item.dc_title = doc['dc.title'][0] if 'dc.title' in doc else ''
                item.search_resource_id = doc['search.resourceid'] if 'search.resourceid' in doc else 0
                item.dc_type = doc['dc.type'][0] if 'dc.type' in doc else ''
                item.date_issued = doc['dateIssued'][0] if 'dateIssued' in doc else ''
                item.color = add_color(items, item.color)
                items.append(item)
        return items
    except Exception as e:
        print(e)


def add_color(items, color):
    i = 0
    while contain_color(items, color) and i < 10:
        color = random.choice(colors)
        i += 1
    return color


def contain_color(items, color):
    for c in items:
        if c.color == color:
            return True
    return False
