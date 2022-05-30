# Development of a generative chatbot api


## Setup
### Clone the project

### Installing Python3

This project runs on the latest stable version of python.

First install [Python3](https://www.python.org/downloads/).

## Package management

For this project conda was used to manage the packages.

#### Installing conda

Follow this [guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) to install conda.

## Dependencies

This project relies on the following dependencies:

- numpy

- tensorflow

- flasgger



### Install dependencies

Install the dependencies with condo by running the following commands:

```bash
conda install -c conda-forge numpy

conda install -c conda-forge tensorflow

conda install -c conda-forge flasgger
```

## Testing the prototype
Unfortunately the link between the chatbot_controller and api_controller did not work out. Therefore, both of these components can only be tested separately.
Running the app.py shows the Swagger UI document and by running the chatbot_py, the chatbot can be tested with input from the user.

![2022-05-31_03-55-44 (2)](https://user-images.githubusercontent.com/78908824/171054986-da6835fd-085e-4b3a-b37c-0e037ba34fac.gif)

To start the chatbot, it requires some time and processing power to train the model. Each epoch decreases the loss of the data and the accuracy increases each time.
![2022-05-31_04-08-24 (1)](https://user-images.githubusercontent.com/78908824/171055062-c098c967-3c36-4d69-aa88-8799d29be344.gif)

The output response of the chatbot depends on the training. Since the dataset is small, the prediction of the model is rather inaccurate and still makes some mistake.
![2022-05-31_04-08-24 copy (1)](https://user-images.githubusercontent.com/78908824/171055369-4e93872c-4ed4-4e4a-875e-6358738e0a55.gif)
