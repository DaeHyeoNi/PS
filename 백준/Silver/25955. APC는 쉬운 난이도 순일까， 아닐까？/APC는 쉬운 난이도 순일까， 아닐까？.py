class Problem:
    def __init__(self, clazz: str, level: int):
        self.clazz = clazz
        self.level = level

    def __lt__ (self, other):
        # B, S, G, P, D == clazz
        # 1, 2, 3, 4, 5 == level
        if self.clazz == other.clazz:
            return self.level > other.level
        else:
            clazz_order = ['B', 'S', 'G', 'P', 'D']
            return clazz_order.index(self.clazz) < clazz_order.index(other.clazz)

    def __gt__(self, other):
        return other < self

problem_cnts = int(input())
problems = list(map(str, input().split()))

problem_objs = []
for problem in problems:
    clazz = problem[0]
    level = int(problem[1:])
    problem_objs.append(Problem(clazz, level))


sorted_problems = sorted(problem_objs)

if problem_objs == sorted_problems:
    print("OK")
else:
    print("KO")
    different_problems = []
    for problem, sorted_problem in zip(problem_objs, sorted_problems):
        if problem != sorted_problem:
            different_problems.append(sorted_problem.clazz + str(sorted_problem.level))
    print(' '.join(different_problems))
