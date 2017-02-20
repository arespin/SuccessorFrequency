
We are given a word list, and a specific word w, and a specific position k in
the word: then the successor frequency of that word at that position is this: we
find the first k letters of word w, and ask how many different letters follow that
prefix in the word list. You see in the list below that with the word advise and
position 5, the successor frequency is 4, because four letters follow: a,e,i,o.

 Output: print the parses in aligned columns, as in the example
below. Each column’s width should be based on the maximum length
of the piece that appears in that column.

_________________________________________________________________________
advis ab ility
advis ab le
advis e
advis e d
advis e d ly
advis e ment
advis e r
advis e r ’s
advis e r s
advis e r s ’
advis e s
advis ing
advis or
advis or ies
advis or s
advis or y
_________________________________________________________________________
h ouses
bird h ouses
coffe e h ouses
wa r e h ouses
sto r e h ouses
clear ing h ouses
meet ing h ouses
block h ouses
custo m h ouses
far m h ouses
green h ouses
slaught er h ouses
pow er h ouses
alm s h ouses
glas s h ouses
ligh t h ouses
cour t h ouses
play h ouses
m ouses
sp ouses
ar ouses

—————————————————————————————————————————————————————————————————————————————————————
Contains:
—————————————————————————————————————————————————————————————————————————————————————
run.py			-This is the file that you want to run.
				-Usage: python SFProblem.py [arg1] [arg2]
					“arg1” = filename to read from, which should be a list of words with each line containing only the word to parse
					“arg2 = K (minimal stem length)	
		
successor-predecessor-frequencies.txt - This is where the words will be output with the spaces at successor frequency indices >1, it outputs the left to right versions for the entire list and then the right to left
	
english1000.txt			-This is a sample file to run the above code on. You must use this file as an argument for “arg1”

1K-signatures.txt		-Output of lines ordered by number of stems associated with signature (Only top 20 signatures)

TomSawyerSignatures.txt	-This is where to output running SFProblem.py, put “TomSawyerSignatures.txt” in line 40 of SFProblem.py

TomSawyer.dx1			-This is a sample file to rub SFProblem.py on, it assumes that the numbers are part of the word and would need to be parsed to be rid of numbers if this assumption isn’t true