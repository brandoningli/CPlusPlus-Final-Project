#Pig Latin Translator.

#Input One Sentence/phrase per line. NO PUNCTUATION
#Output original and translated sentence/phrase to file.

#RULES OF PIG LATIN:
#   Words that begin with consonant sounds,
#       move all letters before initial vowel to end, then add "ay"
#   Begins with vowel sound, just add "way" to end


#First, prepare the files for input and output.
#If you look at the polish notation example with file input,
#we used the fileinput module.
#This is convenient, especially when reading multiple files,
#but is not the standard way, and you can't write to files
#this way.

#Use the open(file, mode='r') function
#file is the filename
#mode is one of the following...
# 'r' for reading (default)
# 'w' for writing, truncating the file first
# 'x' for creation only; fails if exists
# 'a' for writing, appending if it exists


#For the input file, called "pig.ipt"

ipt = open("pig.ipt", mode='r')

#for the output file, called "pig.out"
#We'll write the initial phrase then the translation, so we
#can safely append to this file.

out = open("pig.out", mode='a')

#Now, let's loop through each line in the input file

for line in ipt:
    #Send the line to the output file
    out.write(line)

    #variable to hold the translated phrase
    translated = ''
    
    #Split into words
    words = line.split()

    #Loop through the words
    for word in words:
        #Make it lowercase
        word = word.lower()

        #check for first vowel and move on
        if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
            word = word + 'way'

        #Otherwise start moving until you reach a vowel
        else:
            while word[0] != 'a' and word[0] != 'e' and word[0] != 'i' and word[0] != 'o' and word[0] != 'u':
                word = word[1:] + word[0]
            word = word + 'ay'

        #add to the phrase
        translated += word + " "

    #write the phrase to the file
    out.write(translated + '\n')

#close the files
ipt.close()
out.close()

#Let the user know it's done
print("Translated values stored in pig.out.")
    
