## Chatbot Eval

- ```bot_questions.py``` : programatically or manually generate a file "questions.csv" with formatted sample questions, maybe by "category" if manually entered.  {no, cat, question, answer}
- ```bot_test.py outname.json``` process them by each model, and save each model's "answers". "model_answers.csv" {no, answer}
- ```bot_survey.py``` streamlit app to randomly generate questions and their answers by each model, and ask users to click on the best one, then the app will collect the clicks and come up with a score.
- ```bot_grading.py``` a auto-grader app that load the answers and grade them.

### To launch
Use mumoa docker.

    docker run -p 8501:8501 -p 5005:5005 -p 5002:5002 -p 5055:5055 -p 80:80 -p 8888:8888 --name mumoa -e GRANT_SUDO=yes --user root -e JUPYTER_ENABLE_LAB=yes -v %cd%:/home/jovyan julianweng/mumoa

pip3 install pandas==1.3.2 streamlit==0.86.0