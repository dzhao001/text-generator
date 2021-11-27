# Overview:
This is a relatively simple text generator that takes a piece of text and tracks its patterns and letter placement
to generate random text of its own following said patterns and letter placement. The user can specify word count. Please view the example below. (Text Size: 50 words)


![alt text](https://github.com/dzhao001/text-generator/blob/master/example.png)


One can replace the text file in the "text" repository to whatever text file they wish. The contents text file will then be used to track the frequency of every letter coming after another.
A probability table is then created and using chance, it will then attempt to construct a single word, one letter at a time. At every step, the word in creation will be compared
to an exhuastive list of all the english words in the english language to check whether the word is an english word or could become one. Once a blank space instead of a letter is added
to the word (and the word is valid), word generation stops. This finished word will then be analyzed against the original text file to determine if it exists in that text. If it does, it will be accepted and
another word will begin creation, with the first letter of that word determined by the last letter of the previously created word. This continues until the amount of words the user 
specifies is satisfied. The output text will then be printed.
