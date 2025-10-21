checklist=[]
print("CREATING UR CHECKLIST:")
print("enter ur tasks for today(type 'over' when finished)")
while True:
    task=input("enter task:")
    if task.lower()=="over":
        break
    else:
        checklist.append(task)
completed_tasks=[]
incomplete_tasks=[]
print("\n---end of day review---")
for task in checklist:
    status=input(f"did you complete'{task}'?(yes/no):").lower()
    if status=="yes":
                 completed_tasks.append(task)
    else:
        incomplete_tasks.append(task)

print("\n===daily summary===")
print("\ncompleted tasks:")
for i in completed_tasks:
    print("*",i)
print("\nincomplete tasks:")
for i in incomplete_tasks:
    print("-",i)
