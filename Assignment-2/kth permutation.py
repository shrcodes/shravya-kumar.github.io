def generate_permutations(ch, idx, result):
	if idx == len(ch):
		str1 = ""
		result.append(str1.join(ch))
		return
	for i in range(idx, len(ch)):
		ch[i], ch[idx] = ch[idx], ch[i]
		generate_permutations(ch, idx + 1, result)
		ch[i], ch[idx] = ch[idx], ch[i]
def findKthPermutation(n, k):
	s = ""
	result = []
	for i in range(1, n + 1):
		s += str(i)

	ch = [*s]
	generate_permutations(ch, 0, result)
	result.sort()
	return result[k - 1]
if __name__ == "__main__":
	n = 3
	k = 4
	kth_perm_seq = findKthPermutation(n, k)
	print(kth_perm_seq)


