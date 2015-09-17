# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api
import views

def eventplot(views.events):

    import plotly.plotly as py
    py.sign_in(username='abahuguna', api_key='5gmqkudahe', stream_ids=['avebr1c422', 'mwhbc95775'])
    from plotly.graph_objs import *
    """
    events=[
        {"eventid":1, "prefearfactor":8, "postfearfactor":5},
        {"eventid":2, "prefearfactor":7, "postfearfactor":3},
        {"eventid":3, "prefearfactor":6, "postfearfactor":2},
        {"eventid":4, "prefearfactor":8, "postfearfactor":4}
       ]
    """

    trace1 = Bar(
            x=[i.eventid for i in events],
            y=[j.prefearfactor for j in events],
            name='Projected fear'
            )

    trace2 = Bar(
            x=[i.eventid for i in events],
            y=[j.postfearfactor for j in events],
            name='Actual fear'
            )

    data = Data([trace1, trace2])
    layout=Layout(
       barmode='group'
           )

    fig=Figure(data=data, layout=layout)
    plot_url = py.plot(data, filename='grouped-bar')
    print "**************"
    print plot_url

    return plot_url
