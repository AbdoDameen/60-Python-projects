from textblob import TextBlob
words= ["Data Scence", "Machine Learnin"]
corrected_words=[]

for i in words:
    corrected_words.append(TextBlob(i))
print("wrong words:", words)
print("correct words are:")

for j in corrected_words:
    print(j.correct(), end=" ")
