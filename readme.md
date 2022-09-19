
# [Minoxo](https://jerx.pythonanywhere.com/)

Minoxo is a data driven web app based on a versatile [machine learning model](https://huggingface.co/facebook/bart-large-cnn) by Facebook (now Meta), which uses articles by (CNN)[https://edition.cnn.com/] and can be used for various types of text processing purposes.

One of such purpose is what I took into account for this particular project called Minixo.
Visit Minixo (here)[https://jerx.pythonanywhere.com/].

![demo of the working model](https://raw.githubusercontent.com/thatsameguyokay/images/main/minixoo.gif)

This is an all-in-one text summarizer which gathers logic laid down by complex neural networks created by Facebook's open source community. All you need to do in order to get your essays summarized is, just paste the text and set a range for your query. Minixo handles the REST, both literally and figuratively.

Along with this, Minixo also offers the following advantages:
* **Flexible range:** The range for both input and output text could be given by the user.
* **Minimum system load:** The API never uses system GPUs in order to get any results and hence, are totally load free.
* **Instant copy and paste:** Don't even use your shortcuts, just a clink and it's done.
* **Trusted community:** The model is backed by one of the most trusted communities on the planet.

## Installation

Follow the steps to install the application to your local machine:
* Fork and clone [this](https://github.com/sambhavsaxena/minixo) repository make an instant copy of the content.
* Alternatively, you can download the source and set it up with Github Desktop.
* Make sure you have the latest version of Python interpreted installed.
* Open the root folder in the code editor you prefer, and run the following commands:

```
1) python3 -m pip install virtualenv
2) python3 -m virtualenv <name-of-your-env>
3) source <path-to-your-env-activation-bash>
4) pip install requests flask
```

* Set the environment variables for your API key.
* The environment variables can be mapped using the `export PATH` command.
* Run the `app.py` file in the virtual environment.

## To-do
   - Make the app responsive.
   - Create an additional CSS file and upload it to the repository on [pythonanywhere](https://pythonanywhere.com/).
   - Add additional CI to setup Github workflows.

## Contributing
In order to contribute, start with getting familiar with machine learning models. You might use [Kaggle](https://www.kaggle.com/learn) to get started with. It's a huge playground for ML/AI enthusiasts and professionals.

### License
None.
