
from pyecharts.charts import Map, Geo, EffectScatter,Bar
from pyecharts import options as opts
import pandas as pd
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go
from pyecharts import options as opts

UPLOAD_FOLDER = './static/data/'  # 文件存放路径

def get_picture1():
    df = pd.read_csv(UPLOAD_FOLDER + '地区生产总值.csv', encoding='gbk')

    locate = list(df.地区)
    for i in range(0, len(locate)):
        locate[i] = locate[i].replace('市', '')
        locate[i] = locate[i].replace('省', '')
        locate[i] = locate[i].replace('维吾尔自治区', '')
        locate[i] = locate[i].replace('壮族自治区', '')
        locate[i] = locate[i].replace('回族自治区', '')
        locate[i] = locate[i].replace('自治区', '')
    print(locate)
    地区生产总值 = list(df.地区生产总值)
    list1 = [[locate[i], 地区生产总值[i]] for i in range(len(locate))]
    map_1 = Map()
    map_1.set_global_opts(
        title_opts=opts.TitleOpts(title="2018年中国各地区生产总值"),
        visualmap_opts=opts.VisualMapOpts(max_=100000, min_=1000)  # 最大数据范围
    )
    map_1.add("地区生产总值", list1, maptype="china")
    fig = map_1.render('./temp/example.html')
    return fig



def get_picture2():
    df = pd.read_csv(UPLOAD_FOLDER + '地区生产总值.csv', encoding='gbk')

    地区 = list(df.地区)
    地区生产总值 = list(df.地区生产总值)
    c = (
        EffectScatter()
            .add_xaxis(地区)
            .add_yaxis("地区生产总值", 地区生产总值)
            .set_global_opts(title_opts=opts.TitleOpts(title="EffectScatter-基本示例"))
    )
    fig = c.render('./temp/example.html');
    return fig


def get_picture3():
    dfe = pd.read_csv(UPLOAD_FOLDER + '生产总值指数.csv',index_col=0, encoding='gbk')

    国内生产总值指数 = go.Scatter(
    x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in dfe.columns.values],
    y=dfe.loc["国内生产总值指数",:].values,
    name = "国内生产总值指数"
    )

    地区生产总值指数 = go.Scatter(
    x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in dfe.columns.values],
    y=dfe.loc["地区生产总值指数",:].values,
    name = "地区生产总值指数"
    )

    layout = dict(xaxis=dict(rangeselector=dict(buttons=list([ 
                                                dict(count=3,
                                                        label="3年",
                                                        step="year",
                                                        stepmode="backward"),
                                                dict(count=5,
                                                        label="5年",
                                                        step="year",
                                                        stepmode="backward"),
                                                dict(count=10,
                                                        label="10年",
                                                        step="year",
                                                        stepmode="backward"),
                                                dict(step="all")
                                            ])),
                            rangeslider=dict(bgcolor="#FFF0F5"),
                            title='年份'
                        ),   
                yaxis=dict(title='生产总值指数'),
                title="2009-2018年全国、重庆GDP增速走势"      
                )  

    fig = dict(data=[国内生产总值指数,地区生产总值指数],layout=layout)

    py.offline.plot(fig,filename = './temp/example.html',auto_open=False)

    return './temp/example.html'


def get_picture4():
    dfe = pd.read_csv(UPLOAD_FOLDER + '固定资产投资.csv',index_col=0, encoding='gbk')

    dfe.columns = [int(x) for x in dfe.columns]
    dfe.index = ['全社会固定资产投资','房地产开发投资']

    全社会固定资产投资 = go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in dfe.columns.values],
        y=dfe.loc["全社会固定资产投资",:].values,
        name = "全社会固定资产投资"
    )

    房地产开发投资 = go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in dfe.columns.values],
        y=dfe.loc["房地产开发投资",:].values,
        name = "房地产开发投资"
    )


    layout = dict(xaxis=dict(rangeselector=dict(buttons=list([ 
                                               dict(count=3,
                                                    label="3年",
                                                    step="year",
                                                    stepmode="backward"),
                                               dict(count=5,
                                                    label="5年",
                                                    step="year",
                                                    stepmode="backward"),
                                               dict(count=10,
                                                    label="10年",
                                                    step="year",
                                                    stepmode="backward"),
                                               dict(step="all")
                                           ])),
                        rangeslider=dict(bgcolor="#FFF0F5"),
                        title='年份'
                       ),   
              title="2009-2018年重庆固定投资与房地产投资走势图"      
             )  

    fig = dict(data=[全社会固定资产投资,房地产开发投资],layout=layout)

    py.offline.plot(fig,filename = './temp/example.html',auto_open=False)

    return './temp/example.html'

def get_picture5():
    df = pd.read_csv(UPLOAD_FOLDER + '固定资产投资.csv',encoding='gbk',index_col = "指标名")
    x轴 = [int(x)for x in df.columns.values[-10:]]
    全社会固定资产投资= list(df.loc["全社会固定资产投资"].values)[-10:]
    房地产开发投资= list(df.loc["房地产开发投资"].values)[-10:]
    c = (
        Bar()
        .add_xaxis(x轴)
        .add_yaxis("固定资产投资", 全社会固定资产投资)
        .add_yaxis("房地产开发投资", 房地产开发投资)
        .set_global_opts(title_opts=opts.TitleOpts(title="2009年-2018年重庆固定投资与房地产投资走势图", subtitle="投资额/亿元"))
    )
    fig = c.render('./temp/example.html')
    return fig


def get_picture6():
    df = pd.read_csv(UPLOAD_FOLDER + '施工面积.csv',encoding='gbk',index_col = "指标")
    x轴 = [int(x)for x in df.columns.values[-10:]]
    商品住宅房屋施工面积= list(df.loc["商品住宅房屋施工面积"].values)[-10:]
    商品住宅房屋竣工面积 = list(df.loc["商品住宅房屋竣工面积"].values)[-10:]
    住宅商品房销售面积 = list(df.loc["住宅商品房销售面积"].values)[-10:]
    c = (
        Bar()
        .add_xaxis(x轴)
        .add_yaxis("施工面积", 商品住宅房屋施工面积)
        .add_yaxis("竣工面积", 商品住宅房屋竣工面积)
        .add_yaxis("销售面积", 住宅商品房销售面积)
        .set_global_opts(title_opts=opts.TitleOpts(title="2009年-2018年重庆商品房施工、竣工及销售面积年度走势", subtitle="面积/万平方米"))
    )
    fig = c.render('./temp/example.html')
    return fig

    

def get_picture7():
    df = pd.read_csv(UPLOAD_FOLDER +"商品房销售面积.csv",encoding="gbk")
    trace1 = go.Bar(x=['2018', '2017', '2016','2015', '2014', '2013', '2012','2011', '2010', '2009'],y=[6536.25,6711,6257.15,5381.37,5100.39,4817.56,4522.4,4533.5,4314.39,4002.89],name='住宅商品房销售面积')
    trace2 = go.Bar(x=['2018', '2017', '2016','2015', '2014', '2013', '2012','2011', '2010', '2009'],y=[5424.76,5452.65,5105.46,4477.71,4423.68,4359.19,4105.11,063.42,3986.31,3771.22],name='别墅、高档公寓销售面积')
    trace3 = go.Bar(x=['2018', '2017', '2016','2015', '2014', '2013', '2012','2011', '2010', '2009'],y=[127.37,168.47,106.99,115.84,98.15,68.67,62.3,43.88,62.6,29.15],name='办公楼商品房销售面积')
    trace4 = go.Bar(x=['2018', '2017', '2016','2015', '2014', '2013', '2012','2011', '2010', '2009'],y=[513.97,634.37,622.18,463.05,348.49,244.04,221.89,266.32,194.25,157.15],name='商业营业用房销售面积')
    data = [trace1, trace2,trace3, trace4]
    layout = go.Layout( barmode='stack')
    fig = go.Figure(data=data, layout=layout)
    py.offline.plot(fig, filename = './temp/example.html',auto_open=False)
    return './temp/example.html'