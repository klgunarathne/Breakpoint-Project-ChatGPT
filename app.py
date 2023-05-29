import datetime
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import time
from get_completion_langchain import get_completion_langchain
from get_completion_langchain_fine_tune import get_completion_langchain_fine_tune

from helper.cluster_css import clusterCSSCode
from helper.write_to_css_file import write_to_css_file

load_dotenv()

app = Flask(__name__)

# set the breakpoints
breakpoints = [
    375,
    480,
    620,
    768,
    990,
    1200,
    1400,
    1600,
    1920
]
@app.route('/upload/css', methods=['POST'])
def upload_files():
    if request.method == 'POST':
        css_file = request.files['css']
        
        css_content = css_file.read().decode('utf-8')
        
        clusters = clusterCSSCode(css_content) if len(clusterCSSCode(css_content)) > 0 else []
        
        # get completions
        lstResponse_css = []
        cluster_no = 0
        total_execution_time = 0
        print('Total number of clusters', len(clusters))
        for cluster in clusters:
            start_time = datetime.datetime.now()
            ai_response_css = get_completion_langchain_fine_tune(cluster)
            lstResponse_css.append(ai_response_css)
        
            write_to_css_file('\n /*===Original CSS Start===*/\n' +cluster + '\n /*===Original CSS End===*/\n', 'test.css')
            write_to_css_file(ai_response_css, 'test.css')
            end_time = datetime.datetime.now()
            execution_time = (end_time - start_time).total_seconds()
            total_execution_time += execution_time
            cluster_no += 1
            print('cluster_no:', cluster_no, 'execution time:', execution_time, 'seconds')
            # time.sleep(30)
            if(cluster_no == len(clusters)):
                break
            
        print('Total execution time:', total_execution_time/60, 'minute(s)')
        print("Generating stoped at", cluster_no)
         
        return jsonify(response=lstResponse_css, noOfClusters=len(clusters))

if __name__ == '__main__':
    app.run(debug=True)