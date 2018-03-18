# importing flask
from flask import Flask,redirect,render_template,request,jsonify
import time

# creating an object of flask
app = Flask(__name__)

#jsonify
urls = [
{
  'id': 1,
  'l_url':'http://www.google.com',
  's_path':'abc'
}
]
# specify when to execute
@app.route('/<string:url>')
# function
def url_shorten(url):
	for single_url in urls:
		if url == single_url['s_path']:
			return redirect(single_url['l_url'])
	return 'request url doesnt exist'

@app.route('/home')
def fun():
    return render_template('home.html')
@app.route('/add_url', methods=['POST'])
def f():
    if request.form['url']:
        url_payload={
                    'id': len(urls)+1,
                    's_path':  str(time.time()),
                    'l_url': request.form['url']
                    }
    urls.append(url_payload)

    def url_shorten(url):
        for single_url in urls:
            if url == single_url['s_path']:
                return redirect(single_url['l_url'])
    return jsonify(urls)


    #return render_template('home.html')

#run the server
if __name__ == '__main__':
    app.run(debug=True)
