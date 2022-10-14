str=input("Enter the str : ")
n = len(str) 
if (n < 2):
	print ("Longest palindrome substr is:",str)
	print(n)

start=0
maxlen = 1
ls=""
for i in range(n):
	l = i - 1
	h = i + 1
	while (h < n and str[h] == str[i] ):							
		h=h+1

	while (l >= 0 and str[l] == str[i] ):				
		l=l-1
	
	while (l >= 0 and h < n and str[l] == str[h] ):
		l=l-1
		h=h+1
	
	length = h - l - 1
	if (maxlen < length):
		maxlen = length
		start=l+1

ls=str[start:start + maxlen]		
print ("Longest palindrome substr is : "+ls)
print("Longest palindrome substr is : ", maxlen)