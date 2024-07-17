print("*** Fun with countdown ***")
nums = [int(num) for num in input("Enter List : ").split(" ")]
output = [0, []]
sequence = []
for i in range(len(nums)):
    if i+1 <= len(nums) - 1 and nums[i] - nums[i+1] == 1:
        sequence.append(nums[i])
    if (nums[i] == 1) and (sequence == [] or sequence[-1] == 2):
        sequence.append(1)
        output[0] += 1
        output[1].append(sequence)
        sequence = []
print(output)