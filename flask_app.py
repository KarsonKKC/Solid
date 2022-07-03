from flask import Flask
import ghhops_server as hs
import pandas as pd
import rhino3dm
import numpy as np

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/joindf",
    name="joindf",
    description="join DataFrame",
    inputs=[
        hs.HopsNumber("n1", "n1", "n1", access=hs.HopsParamAccess.LIST),
        hs.HopsNumber("n2", "n2", "n2", access=hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("n3", "n3", "n3")
    ]
)
@app.route("/joindf")
def join_df(n1, n2):
    df = pd.DataFrame({'Name': {0: 'Line', 1: 'Curve', 2: 'Points'},
                       'X': {0: '1', 1: '1', 2: '1'},
                       'Y': {0: '3', 1: '2', 2: '3'}})

    pd.melt(df, id_vars=[n1], value_vars=[n2])

    line1 = pd.array([n1], dtype=str)
    line2 = pd.array([n2], dtype=str)

    join = np.add(line1, line2)
    join = join.flatten()
    print(join)
    return list(join)


if __name__ == "__main__":
    app.run()
