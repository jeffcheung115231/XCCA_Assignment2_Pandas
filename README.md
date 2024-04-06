[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/sXHV6rZl)
# FTDS-week2-test


## Problem 1
Write a Pandas program to convert a given dictionary into a Dataframe.\
The first element of the input list must be the column name.\
The converted dataframe should be returned.
Sample Input: 

```dict={'A':[1,0,0,1], 'B':[0,1,1,0], 'C':[0,1,1,0], 'D':[1,0,0,1]}```

Sample Output:
```
   A  B  C  D
0  1  0  0  1
1  0  1  1  0
2  0  1  1  0
3  1  0  0  1
```

## Problem 2  
#### Problem 2a

Write inside the load() function to read the openrice.csv file in the data folder and return the whole dataframe.

The dataframe should only have 10 rows and 8 columns.

Output:
```
address  ...  price_range
0                     Shop J-K., 200 Hollywood Road,  ...    Below $50
1                           G/F, 108 Hollywood Road,  ...     $201-400
2                           G/F, 206 Hollywood Road,  ...     $201-400
3  Shop 3018, 3/F, Shun Tak Centre, 168-200 Conna...  ...    Below $50
4                          G/F, 38 Queens Road West,  ...      $51-100
5  Shop 1, G/F, King Ho Building, 41-49 Aberdeen ...  ...     $101-200
6                               G/F, 12 Tung Street,  ...    Below $50
7  G/F, Sea View Commercial Building, 21-24 Conna...  ...     $101-200
8  Shop 1B, G/F, Cheungs Building, 1 Wing Lok Str...  ...      $51-100
9                             G/F, 8 Hillier Street,  ...      $51-100
```
---------------
#### Problem 2b


Write inside the makeCategory() function to only return a column called 'price_category' which categorizes the price_range as follows:

 "Below $50": Cheap

 "$51-100": Not Cheap

 "$101-200": Expensive

 "$201-400": Very Expensive



 Output (return type should be a Series):
 ```
 0             Cheap
1    Very Expensive
2    Very Expensive
3             Cheap
4         Not Cheap
5         Expensive
6             Cheap
7         Expensive
8         Not Cheap
9         Not Cheap
Name: price_category, dtype: object
 ```

**Note:** Make sure that the new categories' strings are exact. For example for the category Cheap, the representation of that category in the dataframe should be the string ```'Cheap'```. 

 ---------------
 #### Problem 2c


Write inside the totalDislike() function to only return the total number of dislikes for each price range.

 Output (return type should be a Series):
 ```
 price_range
$101-200      3
$201-400      7
$51-100       1
Below $50    10
Name: dislikes, dtype: int64
 ```
 ---------------
 #### Problem 2d


 Write inside the totalBookmarks() function to return the sum of bookmarks of all 'Hong Kong Style' restaurants.

 Output should be:
 ```
 7011
 ```
 ---------------
 #### Problem 2e


 For the 'number_of_reviews' column, only extract the values of reviews. For example, ```(13 Reviews)``` should be converted to ```13``` as an integer. Write inside extractReview() function to return the modified 'number_of_review' column.

 Output (return type should be a Series):
 ```
 0    133
1     30
2     43
3     39
4     57
5     33
6     25
7     37
8     32
9     37
Name: number_of_reviews, dtype: object
 ```
