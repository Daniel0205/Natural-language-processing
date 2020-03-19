#######################MODULES######################
import sentencepiece as spm

from tkinter import *
from tkinter.ttk import *
###################################################

###################################################
#                   MODELS                        #
###################################################
# train sentencepiece model from `botchan.txt` and makes `m.model` and `m.vocab`
# `m.vocab` is just a reference. not used in the segmentation.
spm.SentencePieceTrainer.train('--input=botchan.txt --model_prefix=m --vocab_size=2000')

spm.SentencePieceTrainer.train('--input=tweets_clean.txt --model_prefix=m_word --model_type=word --vocab_size=2000')


###################################################
def tokenizer():
    select = combo.get()
    text = inputText.get("1.0",END)
    sp = spm.SentencePieceProcessor()  

    if(select=="Prefixes"):
        print("entro1")

        sp.load('m.model')
    else:
        print("entro2")
        sp.load('m_word.model')

    tokens = sp.encode_as_pieces(text)
    
    
    outputText.configure(state='normal')
    outputText.delete('1.0', END)
    outputText.insert("insert", tokens)
    outputText.configure(state='disabled')

###################################################
#                   GUI                           #
###################################################

window = Tk()

window.title("Natural language processing")

window.geometry('500x500')

inputText = Text(window,height=14, width=25)
inputText.grid(column=0, row=0)

outputText = Text(window,height=14, width=25, state='disabled')
outputText.grid(column=0, row=1,)

btn = Button(window, text="Apply",command=tokenizer)
btn.grid(column=1, row=1)

combo = Combobox(window)
combo['values']= ("Prefixes","Words")
combo.current(0) #set the selected item
combo.grid(column=1, row=0)

window.mainloop()


