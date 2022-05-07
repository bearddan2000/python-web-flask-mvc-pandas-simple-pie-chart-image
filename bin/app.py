from flask import Flask, render_template
import matplotlib.pyplot as plt
import pandas as pd
# from manifesAtData import get_dataframe

# Create Flask's `app` object
app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates"
)

@app.route('/', methods=['GET'])
def getCapatcha():
    dataframe = pd.DataFrame({'Name': ['Aparna', 'Aparna', 'Aparna',
                                   'Aparna', 'Aparna', 'Juhi',
                                   'Juhi', 'Juhi', 'Juhi', 'Juhi',
                                   'Suprabhat', 'Suprabhat', 'Suprabhat',
                                   'Suprabhat', 'Suprabhat'],
                          'votes_of_each_class': [12, 9, 17, 19, 20,
                                                  11, 15, 12, 9, 4,
                                                  22, 19, 17, 19, 18]})

    # Plotting the pie chart for above dataframe
    chart = dataframe.plot(kind='pie', y='votes_of_each_class').get_figure()

    chart.savefig('static/image/out.png')
    return render_template(
    "index.html"
    )

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
