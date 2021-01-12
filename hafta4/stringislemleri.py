yazi = """
Until recently, the prevailing view assumed lorem ipsum was born as a nonsense text. It's not Latin, though it looks like it, and it actually says nothing, Before & After magazine answered a curious reader, Its words loosely approximate the frequency with which letters occur in English, which is why at a glance it looks pretty real.

As Cicero would put it, Um, not so fast.

The placeholder text, beginning with the line Lorem ipsum dolor sit amet, consectetur adipiscing elit”, looks like Latin because in its youth, centuries ago, it was Latin.

Richard McClintock, a Latin scholar from Hampden-Sydney College, is credited with discovering the source behind the ubiquitous filler text. In seeing a sample of lorem ipsum, his interest was piqued by consectetur—a genuine, albeit rare, Latin word. Consulting a Latin dictionary led McClintock to a passage from De Finibus Bonorum et Malorum On the Extremes of Good and Evil, a first-century B.C. text from the Roman philosopher Cicero.

In particular, the garbled words of lorem ipsum bear an unmistakable resemblance to sections 1.10.32–33 of Cicero's work, with the most notable passage excerpted below: 
"""
yazi = yazi.lower()
words = yazi.split()
for i in words:
    i = i.strip(" ")
    i = i.strip(".")
    i = i.strip(",")
    i = i.strip(":")
    i = i.strip("\n")
    i = i.strip(" ")

kelimeler = {}
#kelimeler = dict()

for i in words:
    if i in kelimeler:
        kelimeler[i] += 1
    else:
        kelimeler[i] = 1

for i,j in kelimeler.items():
    print(f"{i} kelimesi {j} kadar geçer")
