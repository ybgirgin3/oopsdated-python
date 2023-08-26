# oopsdated-python

# create repo command


**get repo gql query**
```gql
query getRepo {
  repo {
    name
    url
    owner
  }
}
```


**create repo gql query**
```gql
mutation CreateRepo {
  create_repo(
    repo_input: {
       name: "oopsdated-python", 
       owner: "ybgirgin3", 
       url: "https://www.github.com/ybgirgin3/oopsdated-python"}
      ) {
          name
          owner
          url
      }
  }
```



