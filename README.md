# demo-graphql-django
<br/>
clone the repo <br/>
cd demo-graphql-django <br/>
virtualenv -p python3 venv <br/>
source venv/bin/activate <br/>
pip3 install -r requirement.txt <br/>
python manage.py migrate <br/>
python manage.py loaddata ingredients <br/>
python manage.py runserver <br/>
http://127.0.0.1:8000/graphql
<br/> 


# To get all ingredients

```
query {
  allIngredients {
    edges {
      node {
        id,
        name,
        notes,
       category {
         id,
        name
       }
      }
    }
  }
}
```



# get ingredient by id 
```
## Graphene creates globally unique IDs for all objects.
## You may need to copy this value from the results of the first query
```
```
query {
  ingredient(id: "SW5ncmVkaWVudE5vZGU6Mg==") {
    name
    notes
    category{
      name 
    }
  }
}
```



# You can also get each ingredient for each category:

```
query {
  allCategories {
    edges {
      node {
        name,
        ingredients {
          edges {
            node {
              name
            }
          }
        }
      }
    }
  }
}
```



# Or you can get only ‘meat’ ingredients containing the letter ‘e’:
## You can also use `category: "CATEGORY GLOBAL ID"`
```
query {
  allIngredients(name_Icontains: "e", category_Name: "Meat") {
    edges {
      node {
        name
      }
    }
  }
}
```
