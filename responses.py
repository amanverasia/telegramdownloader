import pafy, requests
def sample_responses(input_text):
	url = str(input_text)
	try:
		video = pafy.new(url)
		best = video.getbest()

		r = requests.get('http://tinyurl.com/api-create.php?url=' + best.url)
		return f'Download the video from here: {r.text}'
	except:
		return 'Something went wrong bruh, try again'


	

