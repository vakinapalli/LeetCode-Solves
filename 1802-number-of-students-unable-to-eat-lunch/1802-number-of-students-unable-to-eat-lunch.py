class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        line = deque(students)

        for i in sandwiches:
            hold = len(line)
            for j in range(len(line)):
                temp = line.popleft()
                if temp == i:
                    break
                line.append(temp)
            if hold == len(line):
                break
        return len(line)
        
        