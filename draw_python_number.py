"""
	*
	* *
	* * *
	* * * *
	* * * * *
"""
for row in range(5):
	for col in range(row):

		print('*',end=' ')
	print()
print()
"=================================================="
"""
* * * * *
  *     *
    *   *
      * *
        *
"""
for row in range(5):
	for col in range(5):
		if (row - col==0)or (row==0 or col==4):
			print("*" ,end=' ')
		else:
			print(end='  ')
	print()
print()
"=================================================="
"""
  * * * *
      * *
    *   *
  *     *
*     """
for row in range(5):
	for col in range(5):
		if (row + col==4)or (row==0 or col==4)and(col >0 and row <4):
			print("*" ,end=' ')
		else:
			print(end='  ')
	print()
print()
"================================================="
"""
	* * * * * *
	* * * * *
	* * * *
	* * *
	* *
	*
"""
print()
for row in range(5):
	for col in range(5-row):

		print('*',end=' ')
	print()
print()
"=================================================="
"""
* * * * * * *
  * * * * * *
    * * * * *
      * * * *
        * * *
          * *
            * """
for row in range(5):
	for col in range(5):
		if (row==0 or col==4)or (row==col) or (col-row==1 or col-row==2 or col-row==3):
			print("*" ,end=' ')
		else:
			print(end='  ')
	print()
"=================================================="
"""
	1 2 3 4 5
	1 2 3 4
	1 2 3
	1 2
	1
"""
for row in range(5):
	for col in range(1,5-row):

		print(row,end=' ')
	print()
print()
"=================================================="
"""
	1
	1 2
	1 2 3
	1 2 3 4
	1 2 3 4 5
"""

for row in range(5):
	for col in range(1,row+1):

		print(row,end=' ')
	print()
print()
"=================================================="
"""
	1
	2 2
	3 3 3
	4 4 4 4
	5 5 5 5 5
"""
for row in range(5):
	for col in range(1,row+1):

		print(col,end=' ')
	print()
print()
"=================================================="
"""
	     *
	    * *
	   * * *
	  * * * *
	 * * * * *
	* * * * * *
"""
for row in (range(0,5)):
	for col in range(0,5-row-1):
		print(end=" ")
	for col in range(0,row+1):
		print("*",end=" ")
	print()
print()
"=================================================="
"""
	* * * * * *
	 * * * * *
	  * * * *
	   * * *
	    * *
	     *
"""
for row in range(5,0,-1):
	for col in range(0,5-row):
		print(end=" ")
	for col in range(0,row):
		print("*",end=' ')
	print()
print()
"=================================================="
"""
	 ***
	*   *
	*   *
	*****
	*   *
	*   *
	*   *
"""
for row in range(7):
	for col in range(5):
		if ((col==0 or col==4)and row !=0)or ((row ==0 or row==3)and (col>0 and col<4)):
			print('*',end='')
		else:
			print(end=' ')
	print()
print()
"=================================================="
"""
    *     *
	**    *
	* *   *
	*  *  *
	*   * *
	*    **
	*     *
"""
for row in range(7):
	for col in range(7):
		if (col ==0 or col==6)or (col==row):
			print('*',end='')
		else:
			print(end=' ')
	print()
print()
"=================================================="
"""
	*     *
	**   **
	* * * *
	*  *  *
	*     *
	*     *
	*     *

"""
for row in range(7):
	for col in range(7):
		if (col== 0 or col ==6)or ((col== row)and (col >0 and col <4)) or ((row==1 and col==5)or (row==2 and col==4)):
			print('*',end='')
		else:
			print(end=' ')
	print()
print()
"=================================================="
"""
	*
	*
	*
	*
	*
	*
	*******
"""
for row in range(7):
	for col in range(7):
		if (col==0 or row== 6):
			print('*',end='')
		else:
			print(end=' ')
	print( )
print( )
"=================================================="
"""
	 ***
	*   *
	*   *
	*   *
	*   *
	*   *
	 ***

 """
for row in range(7):
	for col in range(5):
		if ((col==0 or col== 4)and (row!=0 and row !=6))or (row==0 or row == 6)and  (col >0 and col<4):
			print('*',end='')
		else:
			print(end=' ')
	print(  )
print( )
"=================================================="
"""
	*     *
	**   **
	* * * *
	*  *  *
	* * * *
	**   **
	*     *
"""
for row in range(7):
	for col in range(7):
		if (col ==0 or col ==6)or ((row-col==0)or(col+row==6)) :
			print('*',end='')
		else:
			print(end=' ')
	print()
print()
"=================================================="
"""
	*******
	*
	*
	*******
	*
	*
	*
"""
for row in range(7):
	for col in range(7):
		if (col==0 or row ==0 or row ==2):
			print('*',end='')
		else:
			print(end=' ')
	print()
print()
"=================================================="
"""
	 ***
	*   *
	*   *
	 ***
	*   *
	*   *
	*   *
	 ***
 """
for row in range(8):
	for col in range(5):
		if ((col==0 or col==4) and (row!=0 and row!=3 and row !=7))or (row==0 or row==3 or row==7)and (col>0 and col<4):
			print('*',end='')
		else:
			print(end=' ')
	print()
print()
"=================================================="
"""
	 *****
	*     *
	*     *
	    *
	   *
	  *
	 *****
 """
for row in range(7):
	for col in range(7):
		if (col==0 or col==6)and (row!=0 and row !=6 and row !=3 and row!=4 and row!=5)or(row==3 and col==4)or(row==4 and col==3)or(row==5 and col==2)or((row==0 or row==6)and (col>0 and col<6)):
			print('*',end='')
		else:
			print(end=' ')
	print( )
print()
"=================================================="
"""
	 *****
	*
	*
	*
	*
	*
	 *****
 """
for row  in range(6):
	for col in range(7):
		if (col==0)and (row!=0 and row!=5)or (row==0 or row ==5)and (col >0 and col <6):
			print('*',end='')
		else:
			print(end=' ')
	print()
print()
"=================================================="
"""
	****
	*   *
	*   *
	****
	*   *
	*   *
	****
"""
for row in range(7):
	for col in range(5):
		if (col==0) or (col==4 and(row!=0 and row!=3 and row!=6))or (row == 0 or row==3 or row==6)and(col>0 and col<4):
			print('*',end='')
		else:
			print(end=' ')
	print()
print()
"=================================================="
"""
	*   *
	*   *
	*   *
	*****
	*   *
	*   *
	*   *
"""
for row in range(7):
	for col in range(5):
		if (col==0 or col==4)or(row==3):
			print('*',end='')
		else:
			print(end=' ')
	print()
print()
"=================================================="
"""
	****
	*   *
	*   *
	****
	*   *
	*   *
	*   *
"""
for row in range(7):
	for col in range(5):
		if (col==0) or (col==4 and(row!=0 and row!=3 ))or (row == 0 or row==3)and(col>0 and col<4):
			print('*',end='')
		else:
			print(end=' ')
	print()
print()
"======================================================="
"""
*******
   *
   *
   *
   *
   *
   *
 """
for row in range(7):
	for col in range(7):
		if (col==3)or(row==0):
			print('*',end='')
		else:
			print(end=' ')
	print()
print()
"======================================================="
"""
	****
	*   *
	*   *
	*   *
	*   *
	*   *
	****
"""
for row in range(7):
	for col in range(5):
		if (col==0) or (col== 4 and (row!=0 and row !=6))or (row==0 or row == 6)and  (col >0 and col<4):
			print('*',end='')
		else:
			print(end=' ')
	print(  )
print()
"======================================================="
"""
	*   *
	*  *
	* *
	**
	* *
	*  *
	*   *
"""
for row in range(7):
	for col in range(5):
		if (col== 0)or (row+col==4)or (col==2 and row==4)or(col==3 and row==5)or(col==4 and row==6):
			print('*',end='')
		else:
			print(end=' ')
	print()
print()
"======================================================="
"""
	 *   *
	  * *
	   *
	  * *
	 *   *
	*     *
"""
for row in range(7):
	for col in range(7):
		if (col-row==1)or (col+row==5):
			print('*',end='')
		else:
			print(end=' ')
	print()
print()
"======================================================="
"""
	*
	**
	* *
	*  *
	*   *
	*    *
	*     *
	********
"""
print('*')
for row in range(7):
		for col in range(8):
			if (col==0 or row==6)or (col-row==1):
				print('*',end='')
			else:
				print(end=' ')
		print()
print()
"======================================================="
"""
	*   *
	 * *
	  *
	  *
	  *
"""
for row in range(5):
	for col in range(5):
		if(col==2 and row >1)or (col-row==0 and col<2)or (col+row==4 and row <2):
			print('*',end='')
		else:
			print(end=' ')
	print()
print()
"======================================================="
"""
****
*   *
*   *
****
*
*
*
"""
for row in range(7):
	for col in range(5):
		if col==0 or (col==4 and(row==1 or row==2)or(row==0 or row==3)and(col>0 and col<4)):
			print('*',end='')
		else:
			print(end=' ')
	print()
print()
