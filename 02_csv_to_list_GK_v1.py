import pandas as pd


data = pd.read_csv ('04_Trivia_quiz\General_Quiz.csv')   
df = pd.DataFrame(data, columns= ['Category', 'Card Name','Answer', 'Incorrect 1', 'Incorrect 2', 'Incorrect 3'])
print (df)
print()

data = pd.read_csv ('04_Trivia_quiz\Horror_Quiz.csv')   
df = pd.DataFrame(data, columns= ['Category', 'Card Name','Answer', 'Incorrect 1', 'Incorrect 2', 'Incorrect 3'])
print (df)
print()

data = pd.read_csv ('04_Trivia_quiz\Tv_Movie_Quiz.csv')   
df = pd.DataFrame(data, columns= ['Category', 'Card Name','Answer', 'Incorrect 1', 'Incorrect 2', 'Incorrect 3'])
print (df)
print()

data = pd.read_csv ('04_Trivia_quiz\Video_Game_Quiz.csv')   
df = pd.DataFrame(data, columns= ['Category', 'Card Name','Answer', 'Incorrect 1', 'Incorrect 2', 'Incorrect 3'])
print (df)
print()