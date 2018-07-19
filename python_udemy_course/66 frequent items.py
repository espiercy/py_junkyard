from collections import Counter

str="The Dark Powers most frequently serve as a plot device for Ravenloft, especially concerning the Dark Lords, the de facto visible rulers of the Ravenloft Demiplane. Where the players are often tormented and opposed by the Dark Lords, the Dark Lords are themselves tormented and opposed by the Dark Powers. Of course, the difference lies in order of power—while many D&D adventures focus on allowing a band of heroes to prevail over a Dark Lord (much as in the spirit of Bram Stoker's novel Dracula), no such victory over the Dark Powers is conceivable. Vecna, (a demi-god and darklord) and Lord Soth \"escaped\" Ravenloft, but are the only two known to have done so."

#break into words
text=str.split()

print(text)

count = Counter(text)

common = count.most_common()

print(common)

#get five most common words
common_words = count.most_common(5)

print(common_words)