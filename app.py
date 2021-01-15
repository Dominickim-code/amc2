from scholarly import  scholarly
from flask import Flask, render_template,jsonify,request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['GET'])
def get_citation():
    keyword_receive = request.args.get('search')
    print(keyword_receive)
    raw_citation_info = scholarly.search_pubs(keyword_receive.replace("'",""))
    citation_info = next(raw_citation_info)
    # scholarly.pprint(citation_info)
    myResult = scholarly.pprint(citation_info)
    return render_template('index.html', webResult=myResult)
    # return jsonify({'result': 'success', 'citation': 'temp','name': '','affiliation': '', })

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
# 잠시만요!!
어떤 드라이버요??네네
