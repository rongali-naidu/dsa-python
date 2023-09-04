```python
movie = {
    "movieName":"Kushi",
    "movieHero":"Pawan Kalyan"
}
```


```python
print(movie)
```

    {'movieName': 'Kushi', 'movieHero': 'Pawan Kalyan'}



```python
movie.keys()
```




    dict_keys(['movieName', 'movieHero'])




```python
movie.values()
```




    dict_values(['Kushi', 'Pawan Kalyan'])




```python
movie.items()
```




    dict_items([('movieName', 'Kushi'), ('movieHero', 'Pawan Kalyan')])




```python
#note that each item is returned as tuple.
for item in movie.items():
    print(item)
```

    ('movieName', 'New Name')
    ('movieHero', 'Pawan Kalyan')



```python
for key,value in movie.items():
    print(key+" is "+value)
```

    movieName is New Name
    movieHero is Pawan Kalyan



```python
for key in movie.keys():
    print(key)
    print(movie[key])
```

    movieName
    New Name
    movieHero
    Pawan Kalyan



```python
#note that looping on dictionary object name also return keys

for key in movie:
    print(key)
    print(movie[key])
```

    movieName
    New Name
    movieHero
    Pawan Kalyan



```python
for value in movie.values():
    print(value)
```

    Kushi
    Pawan Kalyan



```python
#Lenth of dict i.e number of keys/items in the dict
print(len(movie))
```

    2



```python
#updating the item's value of a dictionary
movie['movieName'] = "Kushi2"
```


```python
print(movie)
```

    {'movieName': 'Kushi2', 'movieHero': 'Pawan Kalyan'}



```python
#Adding new item to dictionary
movie['releaseYear'] = 2000
```


```python
print(movie)veg_name
```

    {'movieName': 'New Name', 'movieHero': 'Pawan Kalyan', 'releaseYear': 2000}



```python
#deleting an item from dictionary
del movie['releaseYear']

```


```python
print(movie)
```

    {'movieName': 'New Name', 'movieHero': 'Pawan Kalyan'}



```python
#nupdating items while iterating
for key,value in movie.items():
    movie[key]=value.upper()
```


```python
movie
```




    {'movieName': 'KUSHI2', 'movieHero': 'PAWAN KALYAN'}




```python
#iterarting using __iter__ method

movieIter = movie.__iter__()
print(movieIter.__next__())
print(movieIter.__next__())
```

    movieName
    movieHero



```python
prices = {'banana':1.0, 'apple':2.0, 'orange':1.5}
#total price?
#using accumulator variable approach

total_price = 0
for price in prices.values():
    total_price += price
    
print(total_price)
```

    4.5



```python
#using sum function
sum(prices.values())
```




    4.5




```python
#forming dictionary from two lists using zip
veg_names = ['banana', 'apple', 'orange']
veg_prices = [1.0, 2.0, 1.5]
veg_prices = dict(zip(veg_names,veg_prices))
print(veg_prices)
```

    {'banana': 1.0, 'apple': 2.0, 'orange': 1.5}



```python
#filtering while expanding the dict
{key:value for key,value in veg_prices.items() if value > 1}
```




    {'apple': 2.0, 'orange': 1.5}




```python
#swapping keys , value while expanding the dict
new_dict = {value:key for key,value in veg_prices.items()}
print(new_dict)
```

    {1.0: 'banana', 2.0: 'apple', 1.5: 'orange'}



```python
#sorting on the keys
for key in sorted(veg_prices.keys()):
   print(key," is ", veg_prices[key])
```

    apple  is  2.0
    banana  is  1.0
    orange  is  1.5



```python
#sorting on the values
#note : key in the sorted function is the input for sorting the tuples returned by items()

for key,value in sorted(veg_prices.items(),key=lambda item:item[1],reverse=False):
   print(key," is ", veg_prices[key])
```

    banana  is  1.0
    orange  is  1.5
    apple  is  2.0



```python
#traversing dictionary in reverse order
for key,value in reversed(veg_prices.items()):
    print(key,"'s price is ",value)
```

    orange 's price is  1.5
    apple 's price is  2.0
    banana 's price is  1.0



```python
#traversing list using popitem.
#note : popitem removed item from dict so, slowly it becomes empty. this empty check is used in whole conditon

while veg_prices:
    print("lengh of dict ",len(veg_prices))
    print(veg_prices.popitem())
```

    lengh of dict  3
    ('orange', 1.5)
    lengh of dict  2
    ('apple', 2.0)
    lengh of dict  1
    ('banana', 1.0)



```python
print(veg_prices)
```

    {}



```python
#applying map on dictionary to transform its elements

dict(map(lambda item: (item[0],item[1].lower()), movie.items()))
```




    {'movieName': 'kushi2', 'movieHero': 'pawan kalyan'}




```python
#applying filter on  dictionary to select items meeting a criteria

dict(filter(lambda item: item[1] > 1, prices.items()))
```




    {'apple': 2.0, 'orange': 1.5}




```python```python
movie = {
    "movieName":"Kushi",
    "movieHero":"Pawan Kalyan"
}
```


```python
print(movie)
```

    {'movieName': 'Kushi', 'movieHero': 'Pawan Kalyan'}



```python
movie.keys()
```




    dict_keys(['movieName', 'movieHero'])




```python
movie.values()
```




    dict_values(['Kushi', 'Pawan Kalyan'])




```python
movie.items()
```




    dict_items([('movieName', 'Kushi'), ('movieHero', 'Pawan Kalyan')])




```python
#note that each item is returned as tuple.
for item in movie.items():
    print(item)
```

    ('movieName', 'New Name')
    ('movieHero', 'Pawan Kalyan')



```python
for key,value in movie.items():
    print(key+" is "+value)
```

    movieName is New Name
    movieHero is Pawan Kalyan



```python
for key in movie.keys():
    print(key)
    print(movie[key])
```

    movieName
    New Name
    movieHero
    Pawan Kalyan



```python
#note that looping on dictionary object name also return keys

for key in movie:
    print(key)
    print(movie[key])
```

    movieName
    New Name
    movieHero
    Pawan Kalyan



```python
for value in movie.values():
    print(value)
```

    Kushi
    Pawan Kalyan



```python
#Lenth of dict i.e number of keys/items in the dict
print(len(movie))
```

    2



```python
#updating the item's value of a dictionary
movie['movieName'] = "Kushi2"
```


```python
print(movie)
```

    {'movieName': 'Kushi2', 'movieHero': 'Pawan Kalyan'}



```python
#Adding new item to dictionary
movie['releaseYear'] = 2000
```


```python
print(movie)veg_name
```

    {'movieName': 'New Name', 'movieHero': 'Pawan Kalyan', 'releaseYear': 2000}



```python
#deleting an item from dictionary
del movie['releaseYear']

```


```python
print(movie)
```

    {'movieName': 'New Name', 'movieHero': 'Pawan Kalyan'}



```python
#nupdating items while iterating
for key,value in movie.items():
    movie[key]=value.upper()
```


```python
movie
```




    {'movieName': 'KUSHI2', 'movieHero': 'PAWAN KALYAN'}




```python
#iterarting using __iter__ method

movieIter = movie.__iter__()
print(movieIter.__next__())
print(movieIter.__next__())
```

    movieName
    movieHero



```python
prices = {'banana':1.0, 'apple':2.0, 'orange':1.5}
#total price?
#using accumulator variable approach

total_price = 0
for price in prices.values():
    total_price += price
    
print(total_price)
```

    4.5



```python
#using sum function
sum(prices.values())
```




    4.5




```python
#forming dictionary from two lists using zip
veg_names = ['banana', 'apple', 'orange']
veg_prices = [1.0, 2.0, 1.5]
veg_prices = dict(zip(veg_names,veg_prices))
print(veg_prices)
```

    {'banana': 1.0, 'apple': 2.0, 'orange': 1.5}



```python
#filtering while expanding the dict
{key:value for key,value in veg_prices.items() if value > 1}
```




    {'apple': 2.0, 'orange': 1.5}




```python
#swapping keys , value while expanding the dict
new_dict = {value:key for key,value in veg_prices.items()}
print(new_dict)
```

    {1.0: 'banana', 2.0: 'apple', 1.5: 'orange'}



```python
#sorting on the keys
for key in sorted(veg_prices.keys()):
   print(key," is ", veg_prices[key])
```

    apple  is  2.0
    banana  is  1.0
    orange  is  1.5



```python
#sorting on the values
#note : key in the sorted function is the input for sorting the tuples returned by items()

for key,value in sorted(veg_prices.items(),key=lambda item:item[1],reverse=False):
   print(key," is ", veg_prices[key])
```

    banana  is  1.0
    orange  is  1.5
    apple  is  2.0



```python
#traversing dictionary in reverse order
for key,value in reversed(veg_prices.items()):
    print(key,"'s price is ",value)
```

    orange 's price is  1.5
    apple 's price is  2.0
    banana 's price is  1.0



```python
#traversing list using popitem.
#note : popitem removed item from dict so, slowly it becomes empty. this empty check is used in whole conditon

while veg_prices:
    print("lengh of dict ",len(veg_prices))
    print(veg_prices.popitem())
```

    lengh of dict  3
    ('orange', 1.5)
    lengh of dict  2
    ('apple', 2.0)
    lengh of dict  1
    ('banana', 1.0)



```python
print(veg_prices)
```

    {}



```python
#applying map on dictionary to transform its elements

dict(map(lambda item: (item[0],item[1].lower()), movie.items()))
```




    {'movieName': 'kushi2', 'movieHero': 'pawan kalyan'}




```python
#applying filter on  dictionary to select items meeting a criteria

dict(filter(lambda item: item[1] > 1, prices.items()))
```




    {'apple': 2.0, 'orange': 1.5}




```python
#combining two dicts using update

prices1 = {'banana':1.0, 'apple':2.0, 'orange':1.5}
prices2 = {'ice-cream':1.1, 'coke':2.1, 'coffe':1.52}

#prices1+prices2 throwing error
prices2.update(prices1)
print(prices2)

```

    {'ice-cream': 1.1, 'coke': 2.1, 'coffe': 1.52, 'banana': 1.0, 'apple': 2.0, 'orange': 1.5}



```python
#combining two dicts using expansion operator 

prices1 = {'banana':1.0, 'apple':2.0, 'orange':1.5}
prices2 = {'ice-cream':1.1, 'coke':2.1, 'coffe':1.52}

prices2 = {**prices1,**prices2}
print(prices2)
```

    {'banana': 1.0, 'apple': 2.0, 'orange': 1.5, 'ice-cream': 1.1, 'coke': 2.1, 'coffe': 1.52}



```python
#combining two dicts using chain operator 
from itertools import chain

prices1 = {'banana':1.0, 'apple':2.0, 'orange':1.5}
prices2 = {'ice-cream':1.1, 'coke':2.1, 'coffe':1.52}

prices2 = dict(chain(prices1.items(), prices2.items()))
print(prices2)
```

    {'banana': 1.0, 'apple': 2.0, 'orange': 1.5, 'ice-cream': 1.1, 'coke': 2.1, 'coffe': 1.52}



```python

```
#combining two dicts using update

prices1 = {'banana':1.0, 'apple':2.0, 'orange':1.5}
prices2 = {'ice-cream':1.1, 'coke':2.1, 'coffe':1.52}

#prices1+prices2 throwing error
prices2.update(prices1)
print(prices2)

```

    {'ice-cream': 1.1, 'coke': 2.1, 'coffe': 1.52, 'banana': 1.0, 'apple': 2.0, 'orange': 1.5}



```python
#combining two dicts using expansion operator 

prices1 = {'banana':1.0, 'apple':2.0, 'orange':1.5}
prices2 = {'ice-cream':1.1, 'coke':2.1, 'coffe':1.52}

prices2 = {**prices1,**prices2}
print(prices2)
```

    {'banana': 1.0, 'apple': 2.0, 'orange': 1.5, 'ice-cream': 1.1, 'coke': 2.1, 'coffe': 1.52}



```python
#combining two dicts using chain operator 
from itertools import chain

prices1 = {'banana':1.0, 'apple':2.0, 'orange':1.5}
prices2 = {'ice-cream':1.1, 'coke':2.1, 'coffe':1.52}

prices2 = dict(chain(prices1.items(), prices2.items()))
print(prices2)
```

    {'banana': 1.0, 'apple': 2.0, 'orange': 1.5, 'ice-cream': 1.1, 'coke': 2.1, 'coffe': 1.52}



```python

```
