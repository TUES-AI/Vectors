# Лекция 4 - вектори

---

[Тук може да разгледаде какво рисувах на дъската по време на лекцията](images/README.md)

---

В тази директория е кода от лекцията за вектори. Качвам го и тук:

1.py
```python
for i in range(1,11):
    print(i)

suma = 0

for i in range(1,11):
    suma = suma + i

print("Sumnata na chislata ot 1 do 10 = ", suma)

N = int(input())

for i in range(1,N):
    print(i)
```
```bash
1
2
3
4
5
6
7
8
9
10
Sumnata na chislata ot 1 do 10 =  55
1
2
3
4
5
6
7
8
9
```

---

2.py
```python
for i in range(1,11):
    for j in range(1,11):
        if (j<i):
            print(end='  ')
        else:
            print(j, end=' ')
    print()
```
```bash
1 2 3 4 5 6 7 8 9 10 
  2 3 4 5 6 7 8 9 10 
    3 4 5 6 7 8 9 10 
      4 5 6 7 8 9 10 
        5 6 7 8 9 10 
          6 7 8 9 10 
            7 8 9 10 
              8 9 10 
                9 10 
                  10 
```

---

3.py
```python
for i in range(1,11):
    number_of_spaces = 11-i
    for j in range(1,number_of_spaces):
        print(end=' ')
    print(i)

for i in range(1,11):
    number_of_spaces = 11-i
    for j in range(1,number_of_spaces):
        print(end=' ')
    for j in range(1,i):
        print(j,end=' ')
    print()
```
```bash
         1
        2
       3
      4
     5
    6
   7
  8
 9
10
         
        1 
       1 2 
      1 2 3 
     1 2 3 4 
    1 2 3 4 5 
   1 2 3 4 5 6 
  1 2 3 4 5 6 7 
 1 2 3 4 5 6 7 8 
1 2 3 4 5 6 7 8 9 
```

---

4.py
```python
vector = [1,2,3]
vector2 = [2,3,4]

for i in range(3):
    print(vector[i], end=' ')
print()
for i in range(3):
    print(vector2[i], end=' ')

print("\nSum of the vectrors")
for i in range(3):
    print(vector[i]+vector2[i])

print("\nScalar multiplication of the vector1")
for i in range(3):
    print(vector[i]*10)
```
```bash
1 2 3 
2 3 4 
Sum of the vectrors
3
5
7

Scalar multiplication of the vector1
10
20
30
```

---

5.py
```python
v1 = [1, 2]
v2 = [2, 3]
sum = 0
for i in range(0,2):
  umnovenie = v1[i] * v2[i]
  sum = sum + umnovenie
print(sum)
```
```bash
8
```

---

6.py
```python
import math

def dulzina(v):
    return math.sqrt(v[0]*v[0]+v[1]*v[1])

print(dulzina([3,4]))
```
```bash
5.0
```
