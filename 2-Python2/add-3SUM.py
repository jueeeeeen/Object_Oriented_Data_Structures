nums = [int(num) for num in input("Enter Your List : ").split(" ")]
answers = []

if len(nums) < 3:
    print("Array Input Length Must More Than 2")
    exit()

for i in range(0, len(nums)-2):
    for j in range(i+1, len(nums)-1):
        for k in range(j+1, len(nums)):
            if nums[i] + nums[j] + nums[k] == 5:
                for ans in answers:
                    if sorted(ans) == sorted([nums[i], nums[j], nums[k]]):
                        break
                else:
                    answers.append([nums[i], nums[j], nums[k]])
print(answers)