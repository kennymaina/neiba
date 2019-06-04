# kennyNeighbourhood

This a web app that allows to commuicate with people around your home

## Author name

https://github.com/kennymaina

## Project Description

the application updates you of what is happenning in your neighbourhood

## Technologies Used
- Python3.6
- Django=1.11
- HTML5
-Boostrap3
- CSS3

##  Features
* Users can create their neighbourhoods
* Users can view existing neighbourhoods or their own created ones.
* Users can post on their neighbourhoods.
* Users can view businesses available in their own neighbourhoods

## Application requirements

1. Ensure you have Python3.6 installed in your computer. you can download it by running this command.

`$ sudo apt-get update sudo apt-get install python3.6.`

2. Ensure you have PiP installed in your computer, you can download it by running this command:

`$ python get-pip.py`

3. set up a virtual environment using the following command;

`$ python3.6 -m venv --without-pip virtual`

4. Run the following command to install all your dependencies in your local computer;

`$ pip install -r requirements.txt`

5. Run Migrations `python3.6 manage.py makemigrations <name of the app>` then `python3.6 manage.py migrate`

6. On terminal run `python3.6 manage.py runserver`

## Project setup installation

1. From the repository, click + in the global sidebar and select Clone this repository .

2. Copy the clone command.

3. From a terminal window, change to the local directory where you want to clone your repository.

or just use this

`$ git clone : https://github.com/kennymaina/Neiba.git`

5. Run this command to open the app

`$ python3.6 manage.py runserver`

## BDD

Behavior               |                                 Result
---------------------- | :--------------------------------------------------------------------:
user loads the page    |       requested to login or signup
user signup to the app |       user is redirect to login page and later the home page     
user Registers any hood|       user is redirected to their hood and details about the hood are loaded


## TDD

-To test the app, run this commands in the terminal.



## Contact Information

kenmaina2022@gmail.com


## License


This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
