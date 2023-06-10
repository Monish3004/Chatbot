from flask import Flask, render_template, request, Response
import CBSqliteHelperV4 as bot
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from waitress import serve

def work(a):
	query=a
	send=''
	print("Plot needed")
	#ans=bot.give_res(query)
	if query in exit:
		send="\nBye\n"
		return send
	else:
		send=bot.give_res(query)
		send=str(send)
		if "plot" in query:
			send=plot()
		if send in ["Bad","bad"]:
			send="Sorry I didn't understand you"
	#print("the bot says",send)
	return send
exit=["bye","Bye","Cu","exit","Quit","q","quit","Exit","See you later"]
def plot():
		img = BytesIO()
		plt.plot([1,2,3,4],[1,2,3,4])
		plt.savefig(img, format='png')
		plt.close()
		img.seek(0)
		plot_url = base64.b64encode(img.getvalue()).decode('utf8')
		send = plot_url
		print(send)
		#send = request.args.get(plot_url)
		return send

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index2.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return work(userText)

if __name__ == "__main__":
    serve(app,host='0.0.0.0',port=5000,threads=1)

