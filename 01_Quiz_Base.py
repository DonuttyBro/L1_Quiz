import pandas as pd

data = pd.read_csv ('04_Trivia_quiz\Video_Game_Quiz.csv')   
df = pd.DataFrame(data, columns= ['Category', 'Card Name'])
print (df)