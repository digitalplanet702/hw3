testscore: int =  int(input("what is your test score?"));
if testscore >= 0 and testscore <= 40:
    print ("try harder next time");
elif testscore >= 41 and testscore <=60:
    print("you're getting there, need some more work");
elif testscore >=61 and testscore <=80:
    print("pretty work");
elif testscore >= 81 and testscore <= 95:
    print("awesome");
elif testscore >= 95 and testscore <= 100:
    print("excellent you're star");
else:
    print("illigal grade")