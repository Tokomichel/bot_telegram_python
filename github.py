import requests
from Repository import Repository
    
def get_repos_list(repos_url: str):
    repos = []
    print("4")
    repository = requests.get(repos_url).json()
    print("3")
    for i in range(len(repository)):
        rep = Repository(repository[i]['name'])
        l = repository[i]['language']
        a = requests.get(repository[i]['languages_url']).json()
        print(f"{repository[i]['name']} {repository[i]['language']}")
        
        # for j in range(len(l)):
        #    rep.lag.append(( l[j], a[l[j]]))
        #    print(( l[j], a[l[j]]))
        #    print("3")
           
        repos.append(repository[i]['name'])
    
    return repos

def get_lang_list(lag_url: str):
    lags = requests.get(lag_url).json()

def get_github_user(username):
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