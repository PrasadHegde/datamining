
#Finds longest common subsequence - Assumes always str1 is bigger than str2
#Write a helper function to swap str1 and str2 arguments to account for other way.

def findsub(str1, str2):

    if str2 in str1:
        return str2, len(str2)

    else:
        sofarstr1, sofarlen1 = findsub(str1, str2[1:])
        sofarstr2, sofarlen2 = findsub(str1, str2[:-1])

        if(sofarlen1 > sofarlen2):
            return sofarstr1, sofarlen1
        else:
            return sofarstr2, sofarlen2


#reverse words in sentence
#You need to retain white spaces too.

#def reverse_words(s):
#   r_s = s[::-1]
#    print r_s
#    return

def reverse_words(s):

    r_s = s[::-1]
    words = s.split()
    result = ''
    i = 0
    cnt = len(words)-1

    while (i < len(s)):
        if(r_s[i] == ' '):
            result = result + r_s[i]
            i = i + 1
        else:
            result = result + words[cnt]
            i = i + len(words[cnt])
            cnt = cnt -1

    return result
             
#result = reverse_words(' Prasad Hegde        ')
#print result

def validate_ip_address(s):
    digits = s.split('.')
    
    if(len(digits) != 4):
        return False

    i = 0
    while(i<len(digits)):
        try:
            x = int(digits[i])
        except:
            return False

        if(( x > 255 ) or (x < 0)):
            return False
        i =  i + 1
    
    return True 

#Tests

#b = validate_ip_address('10.0--.0--.1')
#print b

#TODO #generate  power set - All 2^n possibilities

def Powerset(a):

    l = len(a)
    n = 1
    pset = []

    while(n <= l):
        #number of elements to select
        start = 0 #select elements from start to start+n
        while ( start < l):
            oneset = []
            for i in range (start,start+n):
                oneset.append(a[i]) 
        



    return


def Lossy(s):
    i = 1 #length of tokensize
    l = len(s)
    r_s = s
    tsize = int(l/2) + 1 #upper limit for token size

    while (i <= tsize):
        for j in range(0,l-1):
            start = j
            end = j + i
            t1 = r_s[start:end]
            t2 = r_s[end:end+i]
            print t1, t2, start, end # f
            #return   
            while (( start < end) and (t1 == t2)):
                n_s = r_s.replace(t2,"")
                print 'n_s =' + n_s 
                start = end + 1
                end = end + i
                r_s = n_s 
                t1 = r_s[start:end]
                t2 = r_s[end+1:end+1+i]
        i = i + 1
    return r_s

#res = Lossy('ab')
#print res


def permutations(head, tail=''):
        
        print 'head= ' + head
        print 'tail= ' + tail

        if len(head) == 0:
                print tail
        else:
                for i in range(len(head)):
                        #print i,head[i]
                        permutations(head[0:i] + head[i+1:], tail+head[i])


#permutations('abc')

#Find the kth maxima in a array

 

def base_4(n):

        res = ''
        while(n):
                d = int(n/4)
                rem = n -(d*4)
                n = d
                res = res + str(rem)

        return res[::-1]

#input = 21
#b4 = base_4(21)
#print b4

                      
#TODO print all permutations of a string.



#quicksort

def my_qsort(a, start, end):
    #print 'Quick Sort'
    
    if(start >= end):
        return

    pivot = a[start]
    p_st = start

   #Partition array
    for i in range(start+1,end):
       if (pivot > a[i]):
           #Swap pivot to right position
           tmp = a[i]
           a[i] = pivot
           a[p_st] = tmp
           p_st = i

    p_st = i + 1
    
    my_qsort(a, start, p_st-1)
    my_qsort(a,p_st+1, end)
    return
    
a = [4,2]
#print 'Input = '
#print a
#my_qsort(a,0,len(a))

#for i in range(0,1):
    #print i
#    print 'Output = '
#    print a

#find kth minimum

# Loop to compare n elements of array as token once and compare elegantly. Don't need t1 = and t2 = before while loops.

def Print_token():
    
    print 'Token'

    a = 'abcdefg'
    f = len(a)/2+1
    print a

    r_s = ''
    n_s = ''
    for t in range (1,f):
        for i in range(len(a)-t):
            start = i
            end = i + t
            if(end+t <= len(a)):
                print a[start:end], a[end:end+t]
                if(a[start:end] == a[end:end+t]):
                    n_s = n_s + a[0:start] + a[start:end] + a[end+t:]
                    
                     
    return

#Print_token()

#Tests

#lcs, lcslen = findsub('abca', 'bcd')

#lcs, lcslen = findsub('abca', 'bcd')
#print lcs, lcslen
#print ' prasad '

#coin filling problem - given set of denominations come up with minimum number of coins to fill
#Also come up with actual coins filled array

# greedy of picking maximum works in canonical coin systems.

def Fillcoins(c,rem,res):

    if(rem == 0):
        return res

    else:
        for i in range(len(c)):
            s=[]
            if(rem >= c[i]): #select coin i
                #print s
                s.append(c[i])
                res = Fillcoins(c, rem-c[i],res)
                s.extend(res[rem-c[i]])
                res[rem] = min(res[rem],s, key=len)

        return res

#d[0] means 1 coin
d = dict()
sum = 6
c= [1,3,4]
for i in range(sum+1):
    d[i] = [1 for x in range(i)]

#print d
#rs = Fillcoins(c,sum,d)
#print rs

#Fibonanci number recursive

def Fib(n, res):

    if(n < 1):
        return res

    elif(n == 1):
        res.append(1)
        return res

    elif(n == 2):
        res.append(1)
        res.append(1)
        return res

    else:

         t_s = Fib(n-1,res)
         print t_s
         sum = t_s[n-2] + t_s[n-3]
         res.append(sum)
         return res


#print Fib(4, [])



#Fibonanci number non-recusrive


#Fibonanci number using dynamic programming


#Develop min heap in python

#Seriliaze and deserialize a binary tree

#Store binary tree in xml file

#Store binary tree in json file

class tNode:
    
    def __init__(self,val):
        self.v = val
        self.l = None
        self.r = None


def TestTree():
    root = tNode(10)
    rl = tNode(5)
    rr =  tNode(20)
    
    mm = tNode(30)
    rr.r = mm

    root.l = rl
    root.r = rr

    return root

import json

def TreetoJason(r,d):

    if(r == None):
        return {}

    #print d
 
    nd = {}
    nd['v'] = r.v
    nd['l'] = TreetoJason(r.l,d)
    nd['r'] = TreetoJason(r.r,d)
    return nd

#root = TestTree()

#dj = {}
#dj = TreetoJason(root, dj)

#print dj

#print dj

#prim's , kruskal, dikstra algorithm.


#Edit or Levenstein Distance

def ED(src, dst):
    
    print 'src = ' + src +  'dst =' +  dst

    if(src == ''):
        return len(dst)
    
    if(dst == ''):
        return len(src)
    
    if(src[0] == dst[0]):
        c = 0
    else:
        c = 1

    return min(ED(src[1:], dst[1:])+c, ED(src[1:], dst)+1, ED(src, dst[1:])+1) 

#cost = ED('def', 'abc')

#print cost


#Read about word partials (ngrams), phrase terms (shingles), word-proximity ( word clustering index), ternary search tree ( word look up)
#One of simpler solution for type ahead search control is - trie and each leaf node has frequency of it being used.


#Implement a class / subclass - multiple level heirarchical stuff in python. And see how to store it in DB


class vehicle:
    
    def __init__(self, n,manu):
        self.n = n
        self.manu= manu

class car(vehicle):

    #enum = (sedan, suv, hatchback)

    def __init__(self, ty, manu, n):
        self.ty = ty
        vehicle.manu = manu
        vehicle.n = n

#    0,1,2,3,4,5,6
a = [1,2,4,3,4,7,8]

def findlongesuenceinarray(a):
    
    l = len(a)

    r_st = None
    r_end = None
    r_diff = 0

    for i in range(0,l):
        flag = 1
        for j in range(i,l-1):
            if(a[j] > a[j+1]):
                flag = 0
                break

        if(r_diff < (j-i+flag)):
            r_st = i
            r_end = j+flag
            r_diff = j-i+flag

    return r_st,r_end,r_diff

r_st,r_end,r_diff = findlongesuenceinarray(a)

print r_st,r_end,r_diff

#Bubble sort


        









     

 

