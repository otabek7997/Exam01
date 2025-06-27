grade = int(input('Ballni kiriting: '))


if 90 <= grade <=100:
    print("A","(Alo)")
elif 80 <= grade <=89:
    print("B","(Yaxshi)")
elif 70 <= grade <=79:
    print("C","(Qoniqarli)")
elif 60 <= grade <=69:
    print("D","(Qoniqarsiz)")
elif 0 <= grade <=59:
    print("F","(Yomon)")
else:
    print("Ball 0-100 oralig'ida bo'lishi kerak")         