from collections import defaultdict


def tasksToRun(taskDefinitionsInput, changedFiles):
    N = len(taskDefinitionsInput)
    files = defaultdict(set)
    for i in range(1, N, 4):
        for fil in taskDefinitionsInput[i].split(":")[1].split(" ")[1:]:
            files[fil].add(taskDefinitionsInput[i - 1].split(": ")[1])

    A = set()
    for f in changedFiles:
        A.update(files[f])
    print(A)
    return


taskDefinitionsInput = [
    "task: taskA",
    "files: lib/foo.txt lib/bar.txt README.md",
    "deps:",
    "",
    "task: taskB",
    "files: src/baz.txt",
    "deps:",
    "",
    "task: taskC",
    "files: README.md",
    "deps:",
    ""
]
changedFiles = [
    "lib/foo.txt",
    "README.md"
]

tasksToRun(taskDefinitionsInput, changedFiles)
