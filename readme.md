1. create vertual environment using "python -m venv venv" command.
2. activate python environment by typing "./venv/Scripts/activate".
3. install required libaries using "pip install -r "./requierments.txt" command.
4. run main application. type "python app.py" and run the flask server.
use api "http://localhost:5000/upload/css" with POST request. add form data "css" and upload CSS files.

5. to use fine-tuned model add "get_completion_langchain_fine_tune()" function in "app.py" line 44.
6. to use ChatGPT model add "get_completion_langchain()" function in "app.py" line 44.