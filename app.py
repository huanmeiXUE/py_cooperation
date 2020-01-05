from flask import Flask, render_template, request
from pyecharts.charts import Map, Geo, EffectScatter
from pyecharts import options as opts
import pandas as pd
import cufflinks as cf
import plotly as py
import getpicture
import json

app = Flask(__name__)

# 准备工作
cf.set_config_file(offline=True, theme="ggplot")
#py.offline.init_notebook_mode()

@app.route('/getSelect', methods=['GET', 'POST'])
def get_select() -> 'html':
    select = {
        "picture1" : "图一",
        "picture2" :  "图二",
        "picture3" :  "图三",
        "picture4" :  "图四",
        "picture5" :  "图五",
        "picture6" :  "图六",
        "picture7" :  "图七"
    }
    return json.dumps(select)
        

@app.route('/', methods=['GET'])
def hu_run_2019():
    path = getpicture.get_picture1()
    with open(path, encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

    with open('./temp/analyse.html', encoding="utf8", mode="r") as f:
        describe = "".join(f.readlines())

    return render_template('results2.html', the_plot_all=plot_all,
                           the_describe=describe)
    #return render_template('results2.html')


@app.route('/hurun', methods=['GET', 'POST'])
def hu_run_select() -> 'html':
    the_select = request.values.get('the_region_selected')
    if(the_select=="picture1"):
        path = getpicture.get_picture1()
    if(the_select=="picture2"):
        path = getpicture.get_picture2()
    if(the_select=="picture3"):
        path = getpicture.get_picture3()
    if(the_select=="picture4"):
        path = getpicture.get_picture4()
    if(the_select=="picture5"):
        path = getpicture.get_picture5()
    if(the_select=="picture6"):
        path = getpicture.get_picture6()
    if(the_select=="picture7"):
        path = getpicture.get_picture7()
 
    with open(path, encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

    with open('./temp/analyse.html', encoding="utf8", mode="r") as f:
        describe = "".join(f.readlines())

    # plotly.offline.plot(data, filename='file.html')
    return render_template('results2.html', the_plot_all=plot_all,
                           the_describe=describe)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
