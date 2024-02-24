#!/usr/bin/env python
# coding: utf-8

# In[1]:


INPUT = """
#.?#.#???????...??## 1,2,2,1,1,4
???#???.?#?????? 1,2,2,3,2
???????#??.???#? 2,2,4,3
.???????#?? 4,1
?????#????. 1,2,1
#.?#???#???.?#. 1,3,1,1,2
???#?.#.?#??????# 1,2,1,9
.???#????? 4,1
#????#??..????? 1,2
??.#?.???????#??? 2,1,6,3
???.???????.#.#?#?. 1,3,1,1,1,1
???##?????????????## 12,2
???#?????.?#??????.. 9,1,4
?????#?..???????##?? 4,1,1,6
.?#.?.??????.????#. 2,2,5
?##?##.#?##?#????. 5,4,2,1
???..??..????? 2,1,4
?????#?.?##.??##?. 5,3,4
.???.#.#??????.??? 3,1,1,1,1,1
?.???.?#???#??#?# 1,3,1,1,6
.?.??..???#???#????# 1,1,12
..?.?..??? 1,3
???.????????? 3,1,1
.?????.??##??? 3,2
.???????#.### 2,2,1,3
##???.??????#?#?#??? 3,1,1,10
.?##??##??#??? 3,3,1
.????.????????????? 2,1,3,1,1,1
???#??#??.#?? 8,1
???.????.?? 2,1,2
??#?#?.????? 4,1
???????#???#?#?#? 4,9
#.???????. 1,1,3
?#??????.? 1,1,1
?#???##?.???..???? 8,2,1
????????#???.# 9,1,1
???.???#???#?????? 1,1,1,3,4,1
?????##?.??#? 1,5,3
#??##.?.????#???? 1,2,1,6,1
?????#????#???? 1,1,7
????????..??????? 1,2,1,3,1
?##?...???#.?? 4,4
?????#.?.??? 2,3
????.?????#???### 1,1,5,3
#.???#?#?????# 1,3,1,5
.????#?.?????#????? 4,5
.??.???.#?#?#?#.? 2,1,7
.??#?????.?. 5,1
??#??##?.???? 4,2,2
?.?.###?.?#?????##? 1,3,2,5
?#??????#?.??..?# 2,5,2
.????????##?.? 2,4
????##??#???????. 12,2
?.#??.??????#??#?# 1,1,1,9
?#?#??#??#?.???????# 8,1,3,1,1
.?????????.??#? 2,1
??##??.??.? 1,3,1
??.????##???#????# 1,1,7,2,1
????.#???#??##????.? 2,1,9,1
?.??###?.?.??? 4,1
??????#.??????? 6,3,1
??.?????##??. 1,1,6
.#????#??? 1,1,1
??#??.??.?. 4,2,1
?.????????.?.... 1,1
#??..?.#??.?? 3,3
..?#???#?#??#?..#??? 2,8,1,1
???#???.??? 4,1,1
????#?..?.?????? 3,3
??????#????#?.?.?# 12,1,1
#??????????#..? 1,3,1,1,1
???#??#.?#????#? 4,1,2,2
#.?#??#?#???#?.# 1,1,6,1,1
??????.??????. 1,1,2,2
???#???#?. 1,1,1
..??.????#?##??#?? 1,1,9
???.????#?? 1,5
.??.?.???? 1,1,1
??.#????????????#. 1,8,1,2
?#?????????????? 5,1,5
..??.??.#?#?? 1,1,1,3
?????#?????...???? 5,1,1,1,1
.???.??#??# 3,5
???#.????#??????# 3,2,1,1
??????####?.?? 1,8,1
..???#???..??? 4,1,2
????##?#?.#?.?? 2,5,2,1
??##?#???????.??.. 8,1,1
??????????#? 2,1,1
?.?#???#????.???#?? 1,3,1,3,1,3
???????#?? 1,3
???.?#...##???# 1,1,2,1,1
#?.#?#?????. 1,1,1,2
.##.????###?.?.? 2,7,1,1
?#????#???????#???. 9,2
?.#???#??##????? 1,2,6,2
.#?#???.?#??????# 3,1,1,2,3
?#?#??.?..???#?. 4,1,4
?###..?##???#??#. 4,3,1,1
.#??.#????..?..?? 2,1,2,1,2
?..??.??????.?..? 2,3
.?#.??##???????.?? 1,9
???..???????###???. 1,1,8,1
???##??????.? 3,3
???????#??? 1,1,3
??.??????##.??. 1,1,6,2
.##????????????????. 2,5,1,2,1
?#??#????? 1,4,1
#??????.???#???? 4,1,2,1
.##??.??#???#?????? 3,11
.?.??..???.#??? 1,2
...??..??.#????? 2,1
.??#?#?#?#???#?? 9,3
.?#????..##?? 3,3
##??##?????#???#??? 13,2,1
????????????#??# 1,1,6,1,1
?#?##???#??? 1,6
##????#.?#??.#?????? 5,1,2,3,1
??#????#??? 1,4
?.?.?.????##?#?##?? 1,1,1,7,2,1
?????????.??.??. 2,2,1,2,1
??????.????? 4,5
??#?.???#?#??.???? 2,1,6,2
.#.??#...#?.??? 1,1,2
..???.??.?. 1,1
#????.????? 1,1,4
?#.???#??##??? 1,1,3,1
???##???##??#?##.#?? 15,1
?????.#.????? 1,1
???#?#?###??????? 1,8,1,1
?????#????????.#?# 2,7,1,1,1
.????????.#?.#. 3,3,1,1
???##?#?.. 1,6
????#????????#?.??. 6,3
.##?#?.????????? 4,1,2
?#?...????#? 3,4
???.????#? 1,3
???.#??????#??.#??. 3,8,1,1,1
.#???##???? 3,3
??????#?????. 6,1
???.?.?????#? 3,3,1
??##???#????.?#?#?? 4,4,2,1,1
???#??.??.#??#? 3,2,2,1
##?##???????????.? 7,2,1,1,1
.?.??.#????? 1,1,3
?.??????.???#????# 1,1,4,1,2
??#???#?.#?#?##.? 4,2,6,1
..??#..??###?? 2,5
?#????????..?#???#? 3,3,1,3,2
?.???????? 2,2
#?????#?###??? 1,9
??.???##?.???????#?? 1,1,2,10
?#?#.????#?.?#??? 4,5,5
???.????????..? 1,5
???#?????.?#.???##?. 2,6,1,5
.????????###??????? 2,1,6,1
??#?.?#?.???? 3,2,1
.????#????.# 1,1,5,1
??????##?.?..??? 2,3
.?#??????. 2,1
?.?.???????.???????? 1,1,1,4,6,1
??.??.#??##??#???? 1,11
????????##?#??? 12,1
?#??#?#.????#?#???# 6,9
?#???.#?.. 3,1
??#?.?#?????. 4,2,4
.??.?..??#??? 1,4
???#..??.?#??????? 1,1,1,4,3
?###???.?#???? 6,5
?.#?????????.?# 1,2,3,2,2
.?#?.#????##.?. 1,7
?.?#..???????? 1,1,2,2
?????.??#?.?#??..? 1,3,4,1
#??..??????????##? 1,1,1,1,3,5
?????.??#??##???? 2,1,6
..?.?#??###????. 2,4,1,1
##??.#????#?#???.. 4,6,2,1
??#?#??#.#???#??? 4,2,1,6
.#?#????#..?#??#. 8,4
???..???#?..#??? 2,5,1,1
?##?.?.???##?????.?# 2,1,1,7,1
??????#.?.?#???#.? 1,3,1,6
?????????#????#? 3,5,2
?.##?##???#? 5,3
???#?#??#?#?# 1,10
?##??#???? 3,1,3
??#??#????.??.?##. 1,3,2,1,2
???????##????? 1,5,1
??##????#.???# 9,3
?.??????#??.?.????. 9,2
??.??????#???? 7,2
??#?.??.#.??? 4,1,1,2
??.#??#??.?? 6,1
#??????????? 1,1,2,1
?##???##?.?##???? 8,5
?.?#?#??.?#??#?.? 3,4
.#?.????#??#?##.. 2,1,7
?#?.#?##.? 1,4,1
?????##?##??? 7,2,1
??.?.?##???? 2,7
???.????#???. 1,6
?#?????.??. 5,2
????#??.#?#. 1,2,1,1
.???.????#?#?.?? 3,6,2
???.??.?.?.? 1,1,1,1
?#.#????#??#??? 1,7,1
.???#?????#??.?? 1,2,2,1,1
..??.???##..? 1,5,1
.???????..? 2,2
?#????????????#? 2,2,4,1
????..??##?...#????? 1,1,4,1,1,2
?#.???#?????????? 2,4,4
?#??..??.#? 2,1,1
?.?#??????.??#?..?# 1,7,1,1,1
#??#..???? 2,1,1
??#?.??#?.???? 2,2,3
.#???..??? 1,2,1
.??.?#?##.#???.?#? 1,5,3,1
?????.?#?#??????#?? 1,1,7,1,1
??#??????.?#??#?#? 1,5,8
??.?.?.???????? 1,8
?#?#???#?????# 1,9,1
.??#.#??.?#???##?# 2,1,1,1,4
???#???.??#?#? 6,1,1
?###???.?#.?..? 4,2
?#???.????.??#.???. 5,2,1,1,1,1
??????..??.?.##.? 1,2
?.#?#??????...????? 9,1
..??.?.#?? 1,1,2
??##???????????.##? 9,1,1,2
.???.?????? 2,1,1
??#.#?.?#?????.?.? 1,1,1,1,3,1
???#????#????.#. 1,1,7,1
?????#?#?.?.. 6,1
???.???????#??#????. 1,12,1
??.??.?#??# 2,5
?.????#?#????. 1,4,1
???##????#??? 4,3
???????##. 1,1,3
.?.##???#?.?#????? 1,3,2,5
?.??.##??.? 1,2,2
???????#?#???? 3,1,7
#?#.??????#?#??.?.?. 3,2,8,1
.??.??.???? 1,2
???????..?#??? 4,1
?.????##?? 1,5
????#??#??.?#. 7,2
?.##????##?????#???? 2,5,5
.??#.???...##?? 1,1,1,1,2
#??????##???? 1,1,3,3
?###??????????????? 6,11
?#?.#????#??.? 3,2,2
.????#?????#?? 10,1
?????#???? 1,1,5
?#?????.?????#??#.. 1,1,1,1,1,4
????#??.?# 1,5,1
???#?????? 4,1,1
?#?..?.?.?? 2,1,1
#??.??#??#?##??#???? 1,4,1,5,3
?..?#?#??.#???? 4,1,2
?????#???#??#.?#??? 13,1,2
?..#??.??? 2,1,1
???#????#?.????#? 8,2
.???#.???##?????? 1,2,1,9
#..#?#???## 1,5,2
??..?#.??? 1,1,1
??????#?.??.???#. 1,3,1,4
.?##.?..???##?. 3,1,4
?#????#?#?????.? 9,4
??##?.?#??##??. 5,7
??#????####??..#???? 11,4
..#??????? 3,2
?.????????##????.?#? 11,1
.?##????#???. 4,1,4
#???.???????#. 2,1,1,5
#??????#??.?? 1,1,5,1
???????##???#?#.?#? 1,1,5,3,2
?##????##??##? 2,2,2,2
?##?#????..????#?? 5,3,7
.????.#???#? 1,1,2,1
??##???#.?.?#.#?? 7,1,1,3
??.#??#.?#?????.#? 1,1,1,6,1
???????.?#????? 3,1,5
??.?#?.?#?? 2,3
?##??????.?##?? 5,1,4
???.#???#?????#???. 2,12,1
???#??##???#??# 1,6,3,1
??.??.#??####??#?#? 1,2,2,10
??????.?.??????. 2,5
...???.??##?... 1,3
????#..#??#?#?#??### 1,1,13
????????.???.?#.? 4,1,2,1,1
??##??????#????? 7,4,1
???????#?#?#?????#.? 1,1,4,4,1
..?#???#????? 4,4
?#??.##???.#?? 2,5,1,1
.??????#??.#?.?. 1,1,3,2,1
#???.??????????? 1,1,1,9
??.??.?#?.? 1,1,3
#??????#??? 3,4
??#??.??.???#.??# 4,2,4,3
??#???????..?.???### 4,1,1,1,1,4
?.?????#??#?????.. 7,1
?????..?.# 1,2,1
.???###???????###??? 10,6
?#??.?????? 3,1
.#.??#??????? 1,2,1,1
.??#??????#? 1,8
?.?#??..?????? 4,4
?#?#.#.?.?#????? 4,1,1,1,4
?#.?.?###????? 1,1,6,1
.?#?##?###??.?..? 9,1,1
..??????#??????#??? 7,3,2
???#???#?????.. 7,1
??##????.??#??. 5,1
???#????.#?#????? 1,1,1,1,5
????#?????.? 1,5,1
?????#?????????#?..# 4,5,6,1
?????#?#???.?..???? 6,1,1,1,1
?.???#?#?.#?.?.? 1,5,1,1,1
?##????.?.?##?? 3,4
.#?..????. 2,1
??#.##??.. 1,3
?####?#####?????? 11,1
.??.#?..??#.???? 2,3,3
???..????#?#?. 1,3,3
????????#??? 1,2,4
##???.??.#?#????##?# 2,1,11
??.?##??.?..?#??. 3,3
??.#.#.??.????? 2,1,1,1,2
?????..?#???? 4,3
??????#?#??###??? 2,4,5
??#??#?#.?? 8,1
??#?????#? 6,1
??.##?#?#?#???# 8,1
#?#?##???#??#?#????? 1,5,2,1,1,1
.?.#?#?#..??. 5,2
??##?###????? 7,1
?.#???????##????? 1,1,4,2
.??.??.?.?#?????# 1,1,3,2,1
.#???????.??#?? 2,1,4
????##?????.#?? 8,1
????????.#.. 5,1
?????#?#???? 6,1
..?..???????..?#?# 6,3
??.?????#?#? 1,4,1,1
.?????#..???? 2,2,1,1
.#??????#???##??? 1,1,7,1
??.?##??#.????..? 5,1
?.??#.????? 1,1
???.?.?????#??#???# 1,1,1,1,8,1
.?#??.##.##??#??#??? 2,1,2,6,3
?.???#??????.? 4,1,2
?.?????#.?? 3,1
#???##?.?. 6,1
????.???##?#???????? 1,1,4,3,2
.??.?#?.## 2,1,2
???.??????????.?? 1,10,1
.???.?????? 1,1,2
??..???????#?..?#?#? 2,4,3,5
#?##?.????? 4,3,1
???#??#?#????#??#??? 7,7
??#.??##????. 2,4,1
??#??????????.#?? 1,6,1,1
????##?????.?#???? 7,1,4
?.??????????#.???? 9,2
???????##.????#.? 6,5
????#??.??????#???? 3,2,1,5
.???#?????#.?..???. 9,1
#..??.??##. 1,2,4
???????#?#..? 2,1,1,1
?????????.????? 2,5,1
???#?#???.? 1,6
?#???##?#?. 2,6
?..??#???? 1,1,1
?????#?.#.? 2,1,1
.#.????#??#?##?? 1,1,11
?.??.#??#????#. 1,1,1,6
?...##.????#.? 2,2
?????.???#??.#. 1,1,6,1
?#???#????###?#. 1,1,1,8
??#??.?.?. 2,1
#??????????.????##? 1,1,3,1,6
?.?.?????#??????#??? 1,1,9,1
???#??.????????##?## 1,4,4,1,5
.#???????. 3,2
???#.????.?.####?# 1,1,3,6
....??????#???? 3,6
.??????#??????.? 5,3
?.????.?## 2,2
?#????#?..?#? 7,1
.?#??????.??? 6,1
?.?#????????#??. 2,3
?..????#???.?#?? 3,1
##???#???.?.?.? 2,3,1,1,1
?.??#?.?#?#?####?.?. 2,9
.??..##?????. 1,3,3
.?#???##?#??.??..? 4,6,1
?.?#?..??#?#??. 3,6
???#?????##?.??#?#? 3,2,2,6
?#????#?.?#.#? 3,3,1,1
???#??????????????? 1,4,3,6
.##?#?.?#????##?? 2,2,7,1
?????#????.??.?.#??? 8,1,2,1,1,1
#.?.?????#?..????.? 1,1,7,2,1,1
..##?.#?.??#?.# 2,1,1,2,1
??#??...?#???##. 4,2,3
#?#?#????????????? 7,3,1,2
..#??#?##. 4,2
##?####.#??.??.?? 7,1,1,1,1
??#.???##??#.#?#? 2,8,4
?#????#..?.????#?# 2,3,2,4
?.?.#.?????#?#???. 1,1,1,2,1,6
?#???##?#.##???????. 8,6,2
????.??..??##?#? 1,2,1,5
???#??.#?#????? 1,1,1,1,5
????###?#?????? 1,12
???????##????#?##? 1,2,8,3
#.???.?.?#??????. 1,1,1,1,7
?.?#....????. 1,4
??.#???.?#? 1,2,1
?.?.?#???? 1,5
????#?.???#?? 5,1,3
??#?#??#.?.?? 8,1
??#.?#??#.??.?? 1,2,1,1,1
???#???..??#?? 1,1,3
??.#??????? 1,3
?.?#?#?#???????#? 1,8,1,3
?.?####??.?.?.? 5,1
?#???#?.???.?##? 2,3,1,2
.#??????#??..? 3,4
????##?.????#???#? 1,3,1,1,5
???????#????#????#?. 1,2,2,3,1,1
??#..?????#???? 1,2,3
????#?.??? 1,1
??.?#??#???.????? 1,5,2,2,1
..??????#.???# 5,1,1
?#?#?##.????. 6,2
?##.?????.??... 2,4
.????.#?...?##.# 1,1,2,3,1
.????#?#??# 2,7
?#?#.##??#?#??.?#??# 1,1,7,1,2,1
????#?????? 1,3
????##?#?..#?#?#??? 7,5
.?.???.??.?? 1,1,1,1
???.???#??.???#???# 3,4,3,3
.??##???#??#???#??.? 12,2,1
????#?#?#???#.#???.# 1,7,1,1,1,1
.?#?###??#??.?#?? 7,1,1,4
.#????.?#?#. 1,1,3
?#?????.?? 2,2
??.???#.?????? 1,2,1,3
?#.??##???#?.. 1,2,1,2
??.??.???#??? 2,4
???.????.?..?? 2,1,1,2
?#??#####???#.?????? 3,9,2
??.??.??#???#? 1,1,3,4
??#.?.??#???#??. 2,1,2,1,1
?.?????#?? 1,7
?.###????.??. 6,1
.??#??????#?##?? 8,1,4
???##?#???.??.? 6,1
.??..####? 1,4
??????.??????# 2,2,1,1
?.#???#.??#?? 5,3
?...#?#?.???#??.?# 1,1,1,3,1,1
#???.????? 1,1,2
??#..??#?? 3,3
#????.????#?#..?#. 2,1,1,5,1
.#?#??????????????? 1,1,7,1,1,1
??#?????#??.??.?## 11,1,3
#??#????#????? 9,1,1
?????##?????#? 2,8
???????????.???###? 9,1,3
??#?.?.???.#.?. 3,2,1,1
?.??#?#?????.???? 1,4,1,1,4
.##??????? 3,1,1
?????#???#????? 1,1,4,1
.??#?????..#????? 6,6
#??#??#????????# 13,1
??###?????#??????# 9,1,3,1
##???.???#?#?????# 2,2,1,5,1,1
.??...???#? 1,4
?.????.???.???#?#? 2,1,2,3,1
??#?#????? 1,1,2
???#??????????? 3,6
??#?.?#?#. 2,4
.?#????????.??? 3,4,2
????#.???????? 3,8
.??.???#?#???. 2,4
?.??#????#.#.??# 1,8,1,2
..???.?#??. 1,1,1
?????#..?#???# 6,2,1
?###???.#.???#?.??.? 6,1,2,2,1,1
?.??##??##???? 1,3,6
????#.??#??#??#??? 3,2,1,4
#?##?????.##????#? 5,2,7
????#??##?..??? 1,2,3,1
???????#????#?? 1,3,2,1
##??#???????..??#. 8,1,1,1
.##?#?##?#??#?#?#? 12,1,1
??????##?.????? 9,2
????????.. 3,1
?.?#??..?#???.# 1,1,1,5,1
.#???..?#.?#???? 1,1,1,2,2
#.#?#?#?#.#??.???? 1,7,2,1,1
????#??.?#?#??????#? 1,2,1,11
?.#???.??.?#????## 1,2,2,1,5
?#???.??.#?#? 4,2,1,2
????.?.????#??.?? 3,7
?????.#???.# 1,1,1,1
#?.?.???#?##??? 1,1,2,5,1
.?.??#.?#?..?#?????? 1,1,1,2,4,1
??????#.??????? 4,1,1,2
???##??###? 3,4
????.#?????#???#.# 2,2,1,1,1,1
?????.???#??#???? 4,7,2
#.??#?????#?. 1,5,3
?##????.??. 3,2,1
????..??##? 1,1,4
?.#??.?#??.??????#? 1,3,2,1,4
????.?#???. 2,2
#.???#?.?#?? 1,1,1,2
??##?.?#???##??.## 4,7,1,2
?.?????.?#? 2,1,2
????????### 2,6
#?.?????#?# 1,6,1
??#?#??.??????.??.. 3,1,1,4,1,1
?#?.??.#?? 1,2,2
.??????#.#??.#????# 7,1,3,2
??##???###?#??????? 5,8,2
?#.??#?????#??#?? 1,6,1,2,1
?.##??#?#???. 1,2,3,1
#???#????#?#????? 6,1,4,1
?.?#..?????????# 1,1,5,1
???#???.#??? 4,1,1,1
?#??#?##.??? 4,2,1
?####????#? 6,3
?????##??#?##??#???? 1,11,3
?????????????#??#??? 1,1,1,1,1,7
???????.??##.?#?? 3,1,3,3
???#?.????? 3,1
??.#??????#???.?#.? 1,1,1,5,2
?#???#??.. 1,1,3
??#?#???????? 5,1,1,1
?#.???#??#???#?#??? 2,3,9
????##?????.?#???# 1,2,1,2,6
?.????#???????.?? 1,8,1
.??????#?#?? 1,9
.?##..???#??.?# 2,1,1,1,2
.#?#?????#????????#. 1,1,1,2,7
??#??????#?#? 3,1,3
?????.???..???? 1,1,2,1,2
.???.???.#?#? 1,1,1
????#.??#?#?.?##??? 3,2,2,4,1
.????????.#?#??#? 1,1,1,4,1
?.#??##???????? 1,2,2,2,2
.?????#?????##? 3,1,2,2
???#??????.?? 1,3,3,1
.???#?####?#??.?# 1,11,2
#?#..????#?. 1,1,1,2
.???????#??#??? 3,5
?.?.???#?.?#??. 1,1,1,3,3
?.??#?#####?.#???.? 8,4
??.???#?.#??#????#?# 5,5,3
.??????..??? 1,1,3
#????##??????? 3,3,2,1
#?.?##??##????. 1,9
??#??#.????#?.?#?## 3,1,2,3,5
.???#?????.?? 3,1
..????????#???.. 8,1
?????#?.???# 4,2
?.?.????#??.???##? 1,1,2,1,1,4
??#?#..?#???#?#??.?? 4,8,1
?#??.??.?#? 3,1,2
?.?...##???? 1,5
??#?.??????? 2,5
???.??##?#?#??? 1,1,7,1
.??.???????#???? 1,9
??##?.????.?#???#?? 5,3,1,4
#?????#?.?? 2,3,2
??#??#???##??????.? 4,11
???????##????. 1,11
?#??..?#??#??? 2,6
????????#?#????#???? 1,1,8,1,1,1
?..?.#??.???#?? 1,2,2,1
???#?.???#? 4,2
?.??.#?.??? 1,2
???.?????#? 2,3,1
?..#??#???#?#.? 1,1,1,5
?#?#?#??????#.?#???? 13,3
????#?.??????? 2,6
???..#???.????#? 2,4,4
?????#.??#?#??#?##? 1,1,1,6,3
.???????????? 2,5
.??.??.?????.??#?#? 2,1,1,2,3
.?#?#??????.###?#.? 5,2,1,5,1
??.??##???#?.?.????. 7,1
.#??.?#???#?#?????.. 3,12
?..??..#?.?.?? 2,2
???????.?#????. 1,5,2,1
##?.?#.???????#??#? 3,1,1,2,2,1
?.??#?.?????????. 4,1,1,1,2
????.??##? 3,4
?..??.?#???#?#???#.? 1,11
???#??#?????????. 1,4,4,1
#????#?.??#. 1,3,1,1
.???..??????.? 2,1,2
.??????????#?##?.?? 1,7
#.?.#.????#?.#? 1,1,4,2
???#?.?.??#. 4,1,1
?.??#??.?.?.#????# 3,1,1,1,4
??????#?#.?# 2,4,1,1
?.?????##?.??.??? 1,1,4,1,1
?##????.?.#?# 5,1,1,1
..??#??#??. 1,3
??????#?#???..??. 9,1,1
?.#.#?##?##?#???# 1,1,1,7,1
??.?#????? 1,1,4
?.?.??#?#.??#????. 1,5,5,1
???.?#?#??? 1,1,1
??#??????? 1,2,2
..????.??#.? 1,3
???.??..??#?##??.?.? 2,7,1
?#?.???.????.?? 1,3,1,2
#?????#.???# 5,1,1,1
??.??.???#???##??? 2,7
?.?.#?#??.???..? 1,1,3,1,1
.#?.???..###??????#? 2,1,5,5
??.??????????.???? 8,2
??????????? 4,1
??#??#???.#. 3,2,1,1
???#????##?.?#?#? 4,4,4
??#????#?????.. 2,8
?.???.##?????? 1,1,6
??#.?##???#?. 2,2,4
???#?#?????????? 6,1,2
?.????##?###?##? 9,3
?????????? 1,4,1
.??#?????? 4,1
.??##..?#?#? 2,4
?????#??#??#?.#.? 1,8,1
.??.?##?#?#? 1,7
????????#??. 2,6
??#.?.#???.?? 2,4
?##?##???##? 7,3
?#????????#? 3,3,2
?.?????##?? 1,4
.????????.??? 5,3
##.????#??? 2,3,1
?#?.?..??. 3,1,2
????????#????##??### 1,3,3,9
??????#????#????? 2,4,1,6
???.???.#.???#?##? 2,1,1,1,5
???###?.#?????##.. 6,8
???#???#?##.??#?. 3,6,1
?#???...?.??###.??.# 4,1,4,1,1
??????#??#? 1,2,2
??????.??.??. 1,2,2,1
?.?.#????? 1,1,1
.??????.#??? 1,1,1,1
?.?#??#??.????#??.?# 2,2,1,3,3,2
??????.?.#?#???.? 4,1,1,2,1
?????#.###.? 1,2,3,1
???##??#??#???????? 12,4
?#?????????? 3,1,1
?.??#??.????#? 5,1,3
.???##???? 1,2,1
?.???????? 4,1
.#?.?.???? 1,3
??#.??????# 3,3,1
??.?##?.?.??#?? 1,2,1,1,2
.????#??.##??.?#. 2,4,2,1,1
?????.#??. 2,1,1
?#?????#.? 2,1,3
?.?????#?? 1,5
??????#?#..?? 1,1,1,2
?????.????###? 1,2,1,5
.???#?#??? 4,1
.?.?###????? 1,5,1
??????????..?###? 6,1,3
????#?#?#?????###??? 2,3,3,8
??#?..#???? 1,3
???#???.??.?? 4,1,1
??#..???#???#??? 1,1,5,4
??..???##?.??#..? 1,4,1,1,1
#??#.?#????? 1,1,4,1
.??.?##????# 4,2
??#??#????.???# 1,1,1,1,2
?#.????.?.????#??.?# 2,3,1,2,3,1
##???..?.?.????? 5,1,2,1
???.?????????????#?? 1,15
??##???.??#??? 1,5,2,1
.?.??????#?? 2,3
?.#???#??? 1,2
.??.??..???# 2,2,2,1
????#?#??? 1,4
??#??#???? 1,3
??#..??#??????? 1,1,1,8
??????.????#???#.? 1,2,1,6,1
.???##???? 1,2,1
.?????.?#..?. 4,1
#?.???####?#?.???? 1,1,8,1,2
.?.?#..??#??.? 1,3
?????#????????#??. 1,6
#???#??.??# 1,3,3
?????????? 7,1
??.???.??? 1,1,1
??????#??.???????.#? 1,2,1,5,1,1
?#??????????????#?. 5,2,7
#???.?.??.?..#? 3,1,1,1,1
.????????????.???.# 1,9,1,1,1
?#?#??????#???## 6,7
..??#.???#.#.????#? 3,3,1,5
?????###?????##???. 16,1
????????#??????#??# 1,1,7,5
.#?????#???####??#? 2,4,8
?#.????###?#?. 1,1,1,6
?.??????###??#?? 1,1,6,4
.?..??.??.???#?.##? 1,1,1,5,3
?????.?#??#??##? 1,2,1,1,3
?#??.?.#?? 3,3
.?????#??.?.# 1,5,1,1
.???????.??#?##?#?#? 1,5,1,9
????#?#??#. 5,1,1
?#????.##?##?..?# 5,6,2
.?????.??#????#???# 1,3,5,2,1
?##????.#??????#? 6,1,1,1
??##?.????##??#?#?? 5,4,4
.???###??...?????? 1,4,1,1,1,2
???#?..???. 3,2
.?.?.#???##???.. 1,2,6
????#?#?#?????. 10,1
.???#??.??.??? 2,1,2
?..#?.?#?????.?? 1,2,1,3,1
??????.??#?#?#. 1,1,3,3
??#??.?##?????##??? 2,3,4
?#?.#.???? 2,1,1
.?.?#?#?####.?.#?# 1,3,4,1,1,1
??.#?..?#?????? 1,1,3,1
#??#??#??.?# 2,6,1
?#??#???????#??#??? 5,6,2
?..#??#?#####.?#???? 1,10,1,1,1
??.????#???#?##?? 1,9
????.?#.?# 1,1,1
???????????? 6,1,2
#..????#?#?#??##.??. 1,3,1,1,5,2
??#?.????###???? 1,1,1,6,1
????.????#?.?# 2,1,1,1
???##????.?.???.??. 1,2,2,2,2
?????.#?#.???.??? 2,1,1,1,2
???#??????.?? 4,1,2
?#?#?????#?#..??#. 11,2
.?#?##?????###???.#? 6,7,1
#?.##?????# 1,8
#..#????????? 1,3,1,2
????#??#??? 2,2
.?##?.?..?.???.?# 4,1,1,1,1
?.????.?#?.???? 2,1,2,2
??#??#?.?. 6,1
?#??#??#??##..?## 3,1,6,3
??#.???##? 2,4
#??#????.?????..?.? 1,5,2,1,1
.?#??#??#????#?#?? 2,2,10
####????#??##.?????? 5,1,3,4
???##.?.??.? 1,2,1,1
.?#?????##?????##?. 8,4
.?#????###??#??#???? 2,11
???###?#???#????# 9,1,4
??.??.?.?#???. 1,1,4
#???#??#?#?#???##? 1,3,1,1,1,2
#????##?.? 1,6
##?.?#?#??#?? 3,7
??##????#?.?.?#?#??? 1,2,5,1,1,4
.?#?#?..#?.... 4,1
##?#?#??????. 2,4,1,1
?????????#?????? 1,3,1
?.??#??????? 3,1
###?????#?#??#.#??. 3,2,4,1,1,1
.#???.??###? 1,1,5
?###???.?????. 5,2
?##???????????.? 3,1,5
??#??#?####??.?? 9,1,1
##??#..??????.??#??? 3,1,1,4,2
.???.???...?????? 1,1,5
.?????#????# 3,2,2
.####?.???? 4,1,1
?#.?#??#??##?????? 2,12
.????#?.???? 2,1,2
??#????#??#?? 3,5
?????#???#.?..??#??# 9,2,2
??????.?#? 1,1,3
?#?.#?????. 2,1,1
?#??.???.? 2,1
???????#?.. 6,2
#?????#?#??..# 10,1
?????????. 1,2
...??.##?????#??.?? 8,1
#??????#??##???.? 2,4,6,1
?.##????#??#.?#???# 3,1,1,2,2,1
???#??.???? 1,2,1
#..??#??#??.?????.? 1,4,2,3,1
?#?#.??###??##? 4,9
.???#.??.? 4,2
?..?.?#.????#.?? 2,2
.???##??#???###.?.?? 6,7,1
??##???#?.?? 4,1
??##?#????#?????#.? 13,1
???#?.#?##?.#?#? 3,5,1,1
??.???#????. 1,5,1
.??#???.???. 5,2
??????.#??#.??? 5,4
??#????#?##???.?#??? 12,3
#????????? 1,1,2
???????????#?.. 1,1,1,1,2
??#??#?##????#???#?? 1,2,9,2
?????..??????.??#.?. 3,3,3
??.?#?#?????##?.#?.? 4,6,1,1
??#????##.???? 8,2
?#?.??.#?#?##????? 2,1,9,1
???#???#?..??.?.. 7,2
#.??#??#???.????.?#? 1,9,1,1,2
????##?.?.??.?????## 7,1,2,1,1,2
.?#?#???#???#.?.. 6,1,1,1,1
??.?#??#????.? 1,3,5,1
?#?.??#??? 2,3,1
???#?##???????? 6,1,1
?#?.?????#?????#?. 2,5,5
#?#?#??#???.???? 6,1,1,2
?.??#????#?.??###?. 8,5
.##??#??#???.? 2,2,1,1
???##?.??? 1,3,1
?##.?.????#.#..?# 2,1,3,1,1
?#?#?...?#?#????.??? 4,3,2,3
..##??..????#?????? 2,9
?#??.?#?#?????#???. 3,5,4
???#?????.#???#??? 1,1,1,1,5,2
????.??.#?#??# 2,1,3,1
?#??#????#???.#? 12,1
??????????#??????.?# 1,7,1,2,2
??.????#?##????#? 1,2,1,4,2
??###????? 1,3,1
?#?#???#???.??# 3,1,1,1,2
???#????????. 6,1
##..????.? 2,3
?##????... 3,3
.?.?.?.#?? 1,3
.?.???????????????? 8,7
??#?###?.??..?? 7,1,1
?????.?#?#? 2,3
??#.??#???????#????. 1,7,1,3,1
?????.??#?? 1,1,4
.?????##??# 3,4,1
..??.??#??. 1,1
??????????.#??#?#? 6,7
##???????? 4,4
?????##.?#??. 5,2
#?.?????#??? 2,2,1,1
??#??...??? 4,1
???#??.???#? 1,2,4
??#?????.#? 1,5,1
????.??##?? 2,1,3
?????.??.?.? 3,2,1
.#??.???.?.??#??#?? 2,2,1,2,1,1
#????.??..??#?.#?## 5,1,1,2,4
???????##.????.?#? 7,1,2,2
.???.???????#??????? 1,2,1,5,2
.?#????.??? 1,1,2
.#?#?#?#??#???#..??? 1,10,1,1
??.????#?.????????#? 1,3,2,1,8
?????##??#??.????.. 5,2
..?#???#?##?#??? 2,2,5
??#.?#.??????#? 2,2,1,1,2
.???.????#????? 1,8
??##?###??????#???? 8,3,2,2
???..#.??#? 2,1,2
?#???#???.?# 7,1,1
.#?.???#???#? 1,7
???.??#???..??.? 3,2
..?.#????????. 1,1,1,3
????#??#???#??????? 9,1
.?#????.?...?. 5,1
#??.?????.???#??#?? 3,4,5,1,1
????###??#? 5,1
#???##?#??.?.?????? 10,1,2
?????#?##??.?...##?? 1,6,4
???????#???.?##??. 4,4
#.??#?#.#??.??# 1,2,1,2,3
?????.??????? 2,1,1,1
?????#.##??#?#? 1,3,7
.??????#?#???.??.?. 12,2
??#????.####??#??.?? 3,1,4,3,1
?#.#?????#.?#? 1,7,2
?.?????.?????? 3,4
??????#?.????#???? 2,1,1,1,6
???.#???#? 1,1,2
????#???#??. 6,3
#?##????.?? 6,1,1
?.???##?##.??? 7,1
????.????#.? 2,5
.?#???#???# 1,3,3
##????..#??###???.?? 6,2,4,1,1
?????#?..?#???#?? 2,2,8
??#?##??..?#????#??? 5,3,2,2
???#?????#?.???? 1,7,2
.?.???#????.??#???? 5,1,1,1,2
#????????#?.?#?? 11,1
???#??#??? 1,5
?#??#??????#? 2,1,4
????.#??#.??? 1,1,1
.?????????? 7,1
.??#?#???.??. 1,5,1
#???#?????.#..?..? 1,1,6,1,1,1
?..??.???#???? 2,5,1
???????..??##???.. 3,7
#????.????? 5,1,2
.??#????#???? 1,3
?##????##?. 3,1,3
.?..??#??? 2,1
??#?#????.?# 4,3,1
?##?..????#??#??#? 2,6,1,2
??#??#?###???##?#.#? 1,1,12,1
??##??.#?#??#?.? 1,4,7
??##?#??#??? 6,2,1
????.???.?#?#?##? 2,2,6
#????.????.# 4,1,1,1
#?????#?.???? 1,1,1,3
?#???.##?##?#?#?.?# 3,2,2,4,2
..#?#??#?????#?? 4,9
??#?.??#?. 3,3
.??.????????# 1,2,1,2
?.????..?????????? 1,2,6,1
??#??.????#??.????#? 5,3,3,1,2
.#?.????.????#?? 2,1,2,5
#?.##????#? 2,3,2
..#?.#?##???.?#?#? 2,4,1,4
????????????#??.?#? 4,1,5,1,1
#?#????#..#????##??? 1,1,2,1,6
?#???#?#?????? 2,8,1
?#???.?#?? 2,1,4
?#???.???#?# 1,2,6
?#?##?.??# 5,2
?#???.???????? 3,1,7
?.???????????#?????? 1,3,1,4,1,2
..???????.??? 1,1
#?????#??#.?.#.??..? 10,1,1,2,1
?.?#??????? 4,2
.???#????##?????? 10,2
?#??????##. 1,1,2
###???????#..??#.?? 11,3,1
.???#??.?#??? 2,1,2
.?.?###?##? 1,3,2
#.#?#??####?#?????. 1,1,10,1
.??.????#?#? 1,5
#???????#.??? 3,1,1,1
#..????#??#?#?##. 1,13
?.???.?#?.???#.???? 1,2,2,2,1,3
?..????????. 1,2,3
?.????.?....#????? 2,1,1,6
?##?..??#. 3,3
???.#???..??#.. 2,1,1,3
.?#??.????? 2,1
??????.???. 1,1,1
???#.????#???????. 1,1,8,1
???##???.??#??? 3,1,1,2
????#?..??? 1,2
???#.#??#???##?.??? 1,1,1,7,1
?.????#.?????? 1,5,3,1
????????.??#??#.??.? 1,6,3,1,1,1
..???.?..?#?? 2,1,1,1
???.??..????###?#? 1,1,1,7
??.????.????###? 2,6
????#??#?.?# 1,4,2
.#.##?.?????. 1,2,2
?.????????? 2,2,1
?#???#???.??? 2,1,2,2
???????##? 1,6
#.?????#.#????# 1,4,6
??.##?#?????.#?????? 2,9,1,2,1
##.?..?####?##?? 2,8
???#?.???#??#????? 3,10
?#?????????.?#?????? 10,4,2
.???.????#????? 1,3
#??.?????? 3,2
.??????.?#?#?? 1,1,6
?????????#.# 1,1,1,1
??#.?#???????#.????? 2,6,2,5
??.?#?##??#?#?##??? 13,1
.?.?#???##? 1,1,3
#??????.##. 1,2,2
?##??#????? 6,1
?#????#??#.??.# 6,1,1,1
##...???.?. 2,1
?###???#.#?#?..?.?? 8,3,1
??#?.???##???????#. 1,1,1,4,1,1
#####?.????#???# 5,1,1,3
#???###??..?#? 2,6,2
?.???#??.#?? 4,1,2
????#?#?????????# 1,9,1,1
?##??????#? 3,2,2
"""


# In[ ]:


import functools

#@functools.lru_cache(maxsize=None)
def solve(s, withinRun, remain):
    # print(s, withinRun, remain)
    if not s:
        if withinRun is None and len(remain) == 0:
            print("NOT S - A")
            return 1
        if len(remain) == 1 and withinRun is not None and withinRun == remain[0]:
            print("NOT S - B")
            return 1
        print("NOT S - C")
        return 0
    possibleMore = 0
    for ch in s:
        if ch == "#" or ch == "?":
            possibleMore += 1

    if withinRun is not None and possibleMore + withinRun < sum(remain):
        print("WITHIN - A")
        return 0
    if withinRun is None and possibleMore < sum(remain):
        print ("NOT WITHIN - A")
        return 0
    if withinRun is not None and len(remain) == 0:
        print("WITHIN - B")
        return 0
    poss = 0
    if s[0] == "." and withinRun is not None and withinRun != remain[0]:
        print("COND 1")
        return 0
    if s[0] == "." and withinRun is not None:
        print("COND 2")
        poss += solve(s[1:], None, remain[1:])
    if s[0] == "?" and withinRun is not None and withinRun == remain[0]:
        print("COND 3")
        poss += solve(s[1:], None, remain[1:])
    if (s[0] == "#" or s[0] == "?") and withinRun is not None:
        print("COND 4")
        poss += solve(s[1:], withinRun + 1, remain)
    if (s[0] == "?" or s[0] == "#") and withinRun is None:
        print("COND 5")
        poss += solve(s[1:], 1, remain)
    if (s[0] == "?" or s[0] == ".") and withinRun is None:
        print("COND 6")
        poss += solve(s[1:], None, remain)
    return poss


def day12_puzzle1():
    result = 0
    for line in INPUT.strip().splitlines()[:1]:
        groups, counts = line.split()
        counts = tuple(map(int, counts.split(",")))
        result += solve(groups, None, counts)

    print(f"Part 1: {result}")


def day12_puzzle2():
    result = 0
    for line in INPUT.strip().splitlines():
        groups, counts = line.split()
        groups = "?".join([groups]*5)
        counts = tuple(map(int, counts.split(","))) * 5
        result += solve(groups, None, counts)

    print(f"Part 2: {result}")


day12_puzzle1()
# day12_puzzle2()


# In[ ]:
