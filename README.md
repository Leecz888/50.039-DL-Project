# 50.039 Deep Learning Project

Before starting, clone the GitHub repository into your desired folder with the following command:

`git clone https://github.com/Leecz888/50.039-DL-Project.git`

This is the folder structure of our code:
```
.
├── 📁 Data/
│   ├── 📁 Covid
│   └── 📁 Healthy
├── 📒 model.ipynb
├── 📄 requirements.txt
└── 📄 README.md
```
Before running the code in model.ipynb, it is recommended to set up a virtual environment to install the required dependencies for this project. Please install Conda in your system if it is not already installed. Follow the instructions in the official Conda documentation for installing Conda for your operating system. While we used Conda to set up the virtual environment, there are other ways of setting up a virtual environment as well, however the following instructions for creating a virtual environment are applicable only for Conda.

## Creating a virtual environment in Conda

To create a virtual environment in Conda, run the following command:

`conda create -n <ENVIRONMENT NAME> python `

Replace `<ENVIRONMENT NAME>` with your desired name for the virtual environment.
Follow the instructions in the command line interface to finish creating the virtual environment

Upon creating the virtual environment, we will need to activate it with the following command:

`conda activate <ENVIRONMENT NAME>`

To deactivate your virtual environment, run the following command:

`conda deactivate <ENVIRONMENT NAME>`

To delete your virtual environment, run the following command:

`conda remove -n <ENVIRONMENT NAME> --all`

This will delete the entire virtual environment and all the dependencies installed in it.

## Installing the required dependencies

Run the following command in your virtual environment:

`pip install -r requirements.txt`

This will install all the required dependencies for this project.

Apart from this, it might be good to install FFmpeg before running the project. As our project works with audio files, FFmpeg is a required dependency in most audio related tasks such as audio conversion. While we have already converted the audio files to the correct format, FFmpeg would be required if you wish to run the cell for the audio conversion.

