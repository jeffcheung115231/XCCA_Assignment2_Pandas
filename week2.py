import pandas as pd

d1 = {'A':[1,0,0,1], 'B':[0,1,1,0], 'C':[0,1,1,0], 'D':[1,0,0,1]}

# the prints are for testing output

# Problem 1
def makeDataFrame(data):
	# YOUR SOLUTION STARTS HERE
	df = pd.DataFrame(data)
	return df

print(makeDataFrame(d1))

    # YOUR SOLUTION ENDS HERE
	
# Problem 2a
def load():
	#SOLUTION START( ~ 1 line of code)

	df = pd.read_csv('data/openrice.csv', index_col=[0])
	return df

print(load()) 

	#SOLUTION END


df = load() # use df for the remaining problems

# Problem 2b
def makeCategory():
	#SOLUTION START( ~ 1-2 lines of code)
 
	price_category = df['price_range'].map({"Below $50": "Cheap", "$51-100": "Not Cheap", "$101-200": "Expensive", "$201-400": "Very Expensive"})
	return price_category 

	#SOLUTION END

print(makeCategory())

# Problem 2c
def totalDislike():
	#SOLUTION START( ~ 1-2 line of code)
 
	notgood = df.groupby('price_range')['dislikes'].sum()
	return notgood

	#SOLUTION END

print(totalDislike())


# Problem 2d
def totalBookmarks():
	#SOLUTION START( ~ 1-2 line of code)
 
	hk = df[df['food_type'] == 'Hong Kong Style']['bookmarks'].sum()
	return hk

	#SOLUTION END

print(totalBookmarks())


# Problem 2e
def extractReview():
	#SOLUTION START( ~ 1-2 line of code)
 
    numbers = df['number_of_reviews'].apply(lambda x: ''.join([c for c in str(x) if c.isdigit()]))
    return numbers

	#SOLUTION END

print(extractReview())
