tensor3 = [
	[1,2,3],
	[4,5,6],
	[7,8,9]]

def double_tensor(tensor):
	for i in range(len(tensor)):
		for j in range(len(tensor[i])):
			tensor[i][j] *= 2
	return tensor

print(tensor3)
print(double_tensor(tensor3))

bottom_right = tensor3[1][1:] + tensor3[2][1:]
print(bottom_right)
