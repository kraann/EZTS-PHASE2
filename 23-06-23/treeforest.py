families={
          'kranthi':
                {'sai':{'durga','devi'},
                 'Neha':{'pandu'}
                 }
          'Rahul':
                {'rakesh':{'Tony'},
                 'sandeep':{'brahma'},
                 'sravan':{'krishna'}
                 }
          'carle':
                {'akash':'naresh','ramesh':'david'}
          }
for parent,children in families.items():
    print(f"(parent) has (len(children)),kid(s):")
    print(f" {', and '.join([str(child)for child in [*children]])}")
                 
