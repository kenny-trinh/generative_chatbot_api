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
