from flask import jsonify, request;
from functions import youtube;
yt = youtube.YouTubeHandler();


def _init_(app):

	@app.post('/youtubes/')
	def save():
	    return jsonify(yt.save(request.get_json()));


	@app.get('/youtubes/')
	def get():
	    return jsonify(yt.get(request.get_json()));


	@app.route('/youtubes/', METHOD=['PUT', "UPDATE"])
	def update():
	    return jsonify(yt.update(request.get_json()));



	@app.delete('/youtubes/')
	def delete():
	    return jsonify(yt.delete(request.get_json()));

