from tracemalloc import reset_peak
from urllib import response
from git import RepositoryDirtyError
import requests
import urlshortner


def anime_statistics():
    
    anime_name = str(input("Enter Anime Name: "))
    search_url = f"https://api.jikan.moe/v4/anime?q={anime_name}"
    search_response = requests.get(search_url).json()
    anime_id = search_response['data'][0]['mal_id']
    title_e = search_response['data'][0]['title_english']
    title_je = search_response['data'][0]['title']
    confirmation = str(input(f"Did you Mean : {title_e} / {title_je}, enter y or n : "))
    print(anime_id)
    if confirmation == 'y' or confirmation == 'Y':
        print("THESE STATISTCS ARE BASED ON THE DATA AVAILABLE IN 'MY ANIME LIST' \n\n")
        url = f'https://api.jikan.moe/v4/anime/{anime_id}/statistics'
        response = requests.get(url).json()
        message = f"Title : {title_je}\n\n Planned to Watch : {response['data']['plan_to_watch']}\n Currently Watching : {response['data']['watching']}\n Completed Watching : {response['data']['completed']}\n Dropped in middle : {response['data']['dropped']}\n On Hold : {response['data']['on_hold']}\n Total Weebs : {response['data']['total']}"
        print(message)

def anime_ep_list():
    
    anime_name = str(input("Enter Anime Name: "))
    search_url = f"https://api.jikan.moe/v4/anime?q={anime_name}"
    search_response = requests.get(search_url).json()
    anime_id = search_response['data'][0]['mal_id']
    title_e = search_response['data'][0]['title_english']
    title_je = search_response['data'][0]['title']
    confirmation = str(input(f"Did you Mean : {title_e} / {title_je}, enter y or n : "))
    print(anime_id)
    if confirmation == 'y' or confirmation == 'Y':
        ep_name_response = requests.get(f"https://api.jikan.moe/v4/anime/{anime_id}/videos").json()
        url = f"https://api.jikan.moe/v4/anime/{anime_id}/episodes"
        response = requests.get(url).json()
        message=''
        for i in range(len(response['data'])):
            ep_name = ep_name_response['data']['episodes'][len(response['data'])-i-1]['title']
            air = response['data'][i]['aired']
            ep_info = f"Episode Number : {i+1}\n"f"Episode Title : {ep_name}"+'\n\n' +f"Aired on: {air[:-15]}"
            ep_url = (response['data'][i]['url'])
            forum_url = (response['data'][i]['forum_url'])
            message+=ep_info+f'\n\nWatch Here : {ep_url}\n'+f'Discussion Forum : {forum_url}\n'+'\n===============\n\n'
        print(message)
            
        
        

def animeinfo_by_name():
    
    anime_name = str(input("Enter Anime Name: "))
    url = f"https://api.jikan.moe/v4/anime?q={anime_name}"
    response = requests.get(url).json()
    title_e = response['data'][0]['title_english']
    title_je = response['data'][0]['title']
    confirmation = str(input(f"Did you Mean : {title_e} / {title_je}, enter y or n : "))
    if confirmation == 'y' or confirmation == 'Y':
        anime_id = response['data'][0]['mal_id']    
        trailer_url = 'Watch Trailer : ' +response['data'][0]['trailer']['url']
        title_j = response['data'][0]['title_japanese']
        basic_info = "Type : "+response['data'][0]['type'] + '\n' + 'Source : ' +response['data'][0]['source'] + '\n' + 'Episode Count : ' +str(response['data'][0]['episodes']) + '\n' + 'Status : ' +response['data'][0]['status'] + '\n' + "Aired : "+   response['data'][0]['aired']['string'] + '\n'   
        ep_duration = 'Ep Duration : ' +response['data'][0]['duration']     
        rating = 'Rating : ' +response['data'][0]['rating']
        synopsis = response['data'][0]['synopsis']
        iterpool = (title_je,synopsis,rating,basic_info,ep_duration,trailer_url)
        message = ""
        for item in iterpool:
            message+=item+'\n\n'
        print(message)
    else:
        print("Sorry please try again with original title \n\n(eg: Your Name. ❌, Kimi no Na wa ✅)")
        
        

anime_statistics()