scores = [90, 80, 95, 85]

score_sum = 0
subject_num = 0 
for score in scores:
    score_sum = score_sum + score
    subject_num = subject_num + 1
average = score_sum / subject_num
print("총점:{0}, 평균: {1}".format(score_sum, average))