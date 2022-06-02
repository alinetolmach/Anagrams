from flask import Flask, render_template

app = Flask(__name__)


@app.route("/anagrams/<word>")
def start(word="horse"):
    title = "Anagrams"

    
    text = "Anagrams for the FizzBuzz website"

    choices = anagrams (word)

    return render_template('main.html', title=title, text=text, choices=choices)

def anagrams(word):
    
    word = word.upper()
    
    result = []
    
    f = open("words.txt")
    word_list = f.read().splitlines()
    
    letters = sorted(list(word))
    
    for dict_word in word_list:
        
        if dict_word != word and sorted(list(dict_word)) == letters:
            
            result.append(dict_word)
            
    f.close()
            
    return result


