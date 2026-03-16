class Solution:
    # time:
    # Overall sorting across all students → O(n log n) since total scores = n
    # ---- overall: O(n log n)
    # space:
    # create a hash with the entire test scores O(n)
    # ----- overall: O(n)
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # we use students hash dict to group their test scores
        students = {}

        # go through the scores [ID, grade] from items
        for score in items:
            student_id = score[0]
            test_score = score[1]
            # check if the ID is not in students
            if student_id not in students:
                # insert the student_id:[test_score] in students
                students[student_id] = [test_score]
            # check if the ID is already in students
            else:
                # add the test score to the List for the value of the student_id key
                students[student_id].append(test_score)

        # now we must get the top five average from each value in the students hash
        result = []
        for student in sorted(students):
            sorted_scores = sorted(students[student], reverse=True)
            top_five_avg = sum(sorted_scores[:5]) // 5
            result.append([student, top_five_avg])
        return result
    