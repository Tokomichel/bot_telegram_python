import requests
class Repos():
    def __init__(self, ame) -> None:
        self.ame =  ame
        self.lag = []
    
    def __str__(self) -> str:
        return self.ame + "\n" + self.lag
    
def get_repos_list(repos_url: str):
    repos = []
    print("4")
    repository = requests.get(repos_url).json()
    print("3")
    
    for i in range(len(repository)):
        rep = Repos(repository[i]['name'])
        l = repository[i]['language']
        a = requests.get(repository[i]['languages_url']).json()
        print(f"{a[l]}")
        
        if len(l) == 1:
           print("pp")
           rep.lag.append(( l, a[l])) 
           print('dd')
           
        else:
          for j in range(len(l)): 
           rep.lag.append(( l[j], a[l[j]]))
           print("de")    

        print(rep.lag)   
           
        repos.append(repository[i]['name'])
    
    return repos

def get_lag_list(lag_url: str):
    lags = requests.get(lag_url).json()

def   get_github_user(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        #) Traitez les données de l'utilisateur ici
         
        return user_data
    else:
        print(f"Erreur de requête. Code de statut : {response.status_code}")
        return 

if __name__ == "__main__":
    # Utilisez la fonction pour obtenir les informations d'un utilisateur
    lag = get_github_user('Tokomichel')
    
    print(lag)