import random
import os
import requests
from flask import Flask, render_template, abort, request
from meme_generator import MemeEngine
from quote_engine import Ingestor

# @TODO Import your Ingestor and MemeEngine classes

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        try:
            quotes.extend(Ingestor.parse(f))
        except Exception as error:
            print(f"Exception while getting quotes: {error}")

    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []
    for root, dirs, files in os.walk(images_path):
        try:
            imgs = [os.path.join(root, name) for name in files]
        except Exception as error:
            print(f"Exception while getting Images: {error}")

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    img = "./temp_image.jpg"
    image_url = request.form.get("image_url")
    img_data = requests.get(image_url, stream=True).content
    with open(img, "wb") as f:
        f.write(img_data)

    body = request.form.get("body", "")
    author = request.form.get("author", "")
    path = meme.make_meme(img, body, author)
    print(path)
    os.remove(img)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
