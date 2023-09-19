#IELTS
s, w, l, r = map(float, input().split())

average_score = (s + w + l + r) / 4

fractional_part = average_score % 1

if 0.1 <= fractional_part < 0.25:
    ielts_score = int(average_score)
elif 0.25 <= fractional_part < 0.75:
    ielts_score = int(average_score) + 0.5
else:
    ielts_score = int(average_score) + 1

print(ielts_score)
