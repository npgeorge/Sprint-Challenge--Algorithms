#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Final Answer: O(n) --> Linear, the larger the number, the longer it will take to run.
a = 0 # constant O(1)
n = 10
while (a < n * n * n): # O(n) until a catches up
    print(a)
    a = a + n * n # O(n)
    print(a)


b) Final Answer: 0(n) * O(log n) = O(n log n) --> Linearithmic, runtime grows at a slightly faster rate as n increases.

sum = 0 # constant
n = 20000
for i in range(n): # O(n) over the range
  j = 1 # constant
  print(j)
  while j < n: # O(log n)
    j *= 2 # constant
    print(j)
    sum += 1 # constant
    print(sum)


c) Final Answer: O(n) * O(n-1) = O(n^2 - n) = O(n^2)
def bunnyEars(bunnies): # O(n)
  if bunnies == 0: # constant
    return 0 # constant
  return 2 + bunnyEars(bunnies-1) # O(n-1)

print(bunnyEars(500))

## Exercise II

'''
--UPER--
Understand
- n story building and plenty of eggs
- if thrown of floor "f" or higher, egg breaks
- if thrown of less than floor "f", egg doesn't break
- develop algo to determine value of f such that the # of eggs dropped + broken eggs is minimized

Plan
- function with an input "n" number of total stories, "cf" for current floor of the building, "e" for number of eggs thrown
- determine rules: 
- if dropped off of floor "f" or higher, return False, indicating the egg broke
- else return True, indicating egg did not break
- implement minimizing algo, minimize your dropped / broken ratio of eggs

so....
n = 30
cf = 0
e = 10

### number of stories as input
def break_an_egg(n):
    # initializing lists
    dropped =[]
    broken = []
    # record drops
    floor_outcome = {'floor': broken or not?}

    # random int for f chosen
    f = random(int(range(0,n)))

    # start at middle, then drop
    middle_floor = n // 2

    # drop an egg from middle floor
    # inside for loop for number of eggs
        # if egg breaks
        # record to dict
        # go down by half or n // 4
        # if recorded, f = i -1
        # elif
        # record to dict
        # go up n ** 3/4
        # check if recorded in dict

    return f

'''

