import csv


m= [log n]
C= Create Array(n*n)
InitToZero(C)
for i  in range (1 , [n/m] + 1 ) :
	rs= Create Array ((2^m)*n)
	InitToZero (rs[0])
	bp=1
	k=0
	
	for j  in range (1 , 2^m ):
		rs[j]= rs[j-(2^k)] + RowFromBottom(Bi,K+1)
		if bp=1 then :
			bp=j+1
			k=k+1
		else:
			bp=bp-1
			
	Ci= CreateArray (n*n)
	for j in range (0 , n ):
		Ci[j] = rs[Num(Ai[j])]
		
	C= C + Ci
return C