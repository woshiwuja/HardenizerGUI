from flask import Flask, render_template, request
import pandas as pd
import excel_parser as xp
from markupsafe import escape
app = Flask(__name__)
df_reg = pd.read_xml("assets/registries.xml")
df_cmd = pd.read_xml("assets/commands.xml")

@app.route("/")
def index():
    return render_template('index.html') 
@app.route("/about")
def about():
    return render_template('about.html') 


@app.route("/main")
def main():
    return render_template('main.html') 

@app.route("/registry")
@app.route("/registry/<id>")
def registry(id=None):
    df = pd.read_xml("assets/registries.xml")
    if id == None:
        return render_template('registry.html', registry_dataframe = df.iloc[0])
    else:
        df = df.loc[df['id'] == int(id)]
        return render_template("registry.html",registry_dataframe = df )

@app.route("/commands")
@app.route("/commands/<id>")
def commands(id=None):
    if id == None:
        return render_template('commands.html', commands_dataframe = df_cmd.iloc[0])
    else:
        df = df_cmd.loc[df_cmd['id'] == int(id)]
        return render_template("commands.html",commands_dataframe = df )
@app.route("/sidebar")
def sidebar():
    #choice = request.args.get('choice','')
    #if choice == 'registry':
    if request.args.get('sidebar') == "registries": 
        return render_template('sidebar.html',df = df_reg, path="/registry")
    elif request.args.get('sidebar') == "commands":
        return render_template('sidebar.html',df = df_cmd, path="/commands")
    else:
        return render_template('sidebar.html',df = df_reg, path="/registry")
if __name__ == '__main__':
    app.run()
