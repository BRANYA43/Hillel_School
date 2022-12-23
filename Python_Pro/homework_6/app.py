from flask import Flask

import utils


app = Flask(__name__)


@app.route('/')
def index():
    with open('requirements', 'r') as f:
        module_list = f.readlines()
        html_str_module_list = utils.get_module_list_in_html_str(module_list)
    text_page = f'''
    <h2>Module list to need for to work Flask</h2>
    <blockquote>{html_str_module_list}</blockquote>
    '''
    return text_page


app.run(debug=True)
