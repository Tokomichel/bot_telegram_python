import requests
from time import sleep

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
        print("pp1")
        rep = Repos(repository[i]['name'])
        print("pp2")
        l = repository[i]['language']
        print("pp3") 
           
        repos.append(repository[i]['name'])
    
    return repository

def get_lang_list(lang_url: str, index: int):
    # lags = requests.get(repos_url).json()[index]
    zed = requests.get(lang_url)
    return zed
    

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
    rep = get_repos_list(lag['repos_url'])
    
    print(lag)
    print(rep)