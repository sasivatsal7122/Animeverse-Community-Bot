import requests
import urlshortner

def top_10():
    item_choice_ls = ['Top-10 Anime','Top-10 Manga']
    user_choice = int(input(f"1.{item_choice_ls[0]}\n2.{item_choice_ls[1]}\n\nChoose one: "))
    if user_choice==1:
        type_choice_ls = ['tv','movie','music','special']
        print("1.Tv\n2.Movie\n3.Music\n4.Special")
        filter_ls = ['airing','upcoming','bypopularity']
        print("\n\n1.Airing\n2.Upcoming\n3.By Popularity\n4.Special")
        user_type,user_filter = str(input("Choose one (eg:1.1 or 1.3): ")).split('.')
        url = f'https://api.jikan.moe/v4/top/anime?type={type_choice_ls[int(user_type)-1]}&filter={filter_ls[int(user_filter)-1]}'
        response = requests.get(url).json()
        message = ""
        for i in range(10):
            basic_info = "Type : "+response['data'][i]['type'] + '\n' + 'Source : ' +response['data'][i]['source'] + '\n' + 'Episode Count : ' +str(response['data'][i]['episodes']) + '\n' + 'Status : ' +response['data'][i]['status'] + '\n' + "Aired : "+   response['data'][i]['aired']['string'] + '\n'   
            trailer_url = 'Watch Trailer : ' +response['data'][i]['trailer']['url']
            title_e = f"{i+1}.{response['data'][i]['title']} / {response['data'][i]['title_english']}"
            ep_duration = 'Ep Duration : ' +response['data'][0]['duration']     
            rating = 'Rating : ' +response['data'][i]['rating']
            iterpool = (title_e,rating,basic_info,ep_duration,trailer_url)
            for item in iterpool:
                message+=item+'\n\n'
            message+='=========================\n\n'
        print(message)
    else:
        type_choice_ls = ['manga','novel','lightnovel','oneshot']
        print("1.Manga\n2.Novel\n3.Light Novel\n4.One Shot")
        filter_ls = ['publishing','upcoming','bypopularity']
        print("\n\n1.Publishing\n2.Upcoming\n3.By Popularity")
        user_type,user_filter = str(input("Choose one (eg:1.1 or 1.3): ")).split('.')
        url = f'https://api.jikan.moe/v4/top/manga?type={type_choice_ls[int(user_type)-1]}&filter={filter_ls[int(user_filter)-1]}'
        response = requests.get(url).json()
        message = ""
        for i in range(10):
            basic_info = "Type : "+response['data'][i]['type'] + '\n' + 'Chapters : ' +str(response['data'][i]['chapters']) + '\n' + "Volumes : "+ str(response['data'][i]['volumes'])+ '\n'   
            more_info = 'Find More Info at : ' +response['data'][i]['url']
            title_e = f"{i+1}.{response['data'][i]['title']} / {response['data'][i]['title_english']}"
            published_dates = 'Published Dates : ' +response['data'][0]['published']['string']     
            rating = 'Rating : ' +str(response['data'][i]['score'])
            iterpool = (title_e,rating,basic_info,published_dates,more_info)
            for item in iterpool:
                message+=item+'\n\n'
            message+='=========================\n\n'
        print(message)
    

def anime_relations():
    anime_name = str(input("Enter Anime Name: "))
    search_url = f"https://api.jikan.moe/v4/anime?q={anime_name}"
    search_response = requests.get(search_url).json()
    anime_id = search_response['data'][0]['mal_id']
    title_e = search_response['data'][0]['title_english']
    title_je = search_response['data'][0]['title']
    confirmation = str(input(f"Did you Mean : {title_e} / {title_je}, enter y or n : "))
    if confirmation == 'y' or confirmation == 'Y':
        url = f"https://api.jikan.moe/v4/anime/{anime_id}/relations"
        response = requests.get(url).json()
        message = f'Relations found for {title_je} are :\n\n'
        for i in range(len(response['data'])):
            typee = response['data'][i]['relation']
            for j in range(len(response['data'][i]['entry'])):
                name = response['data'][i]['entry'][j]['name']
                urll = response['data'][i]['entry'][j]['url']
                message+=f'> Category : {typee}'+'\n\n'
                message+=f'> Title : {name}'+'\n\n'
                message+=f'>> Find More info at : \n{urll}'+'\n\n'
            message+='\n\n===================\n\n'
        print(message)


def anime_review():
    anime_name = str(input("Enter Anime Name: "))
    search_url = f"https://api.jikan.moe/v4/anime?q={anime_name}"
    search_response = requests.get(search_url).json()
    anime_id = search_response['data'][0]['mal_id']
    title_e = search_response['data'][0]['title_english']
    title_je = search_response['data'][0]['title']
    confirmation = str(input(f"Did you Mean : {title_e} / {title_je}, enter y or n : "))
    print(anime_id)
    if confirmation == 'y' or confirmation == 'Y':
        url = f"https://api.jikan.moe/v4/anime/{anime_id}/reviews"
        response = requests.get(url).json()
        message = f"Top Review for {title_je}:\n\n"
        date = response['data'][0]['date']
        message+=f'Reviewed on {date[:-15]}'
        message+= '\n\n'+response['data'][0]['review']        
        print(message)



def anime_recommedation():
    anime_name = str(input("Enter Anime Name: "))
    search_url = f"https://api.jikan.moe/v4/anime?q={anime_name}"
    search_response = requests.get(search_url).json()
    anime_id = search_response['data'][0]['mal_id']
    title_e = search_response['data'][0]['title_english']
    title_je = search_response['data'][0]['title']
    confirmation = str(input(f"Did you Mean : {title_e} / {title_je}, enter y or n : "))
    if confirmation == 'y' or confirmation == 'Y':
        url = f"https://api.jikan.moe/v4/anime/{anime_id}/recommendations"
        response = requests.get(url).json()
        message = f'Anime Recommendations for {title_je} are: \n\n'
        for i in range(10):
            message+=f"{i+1}. {response['data'][i]['entry']['title']}"
            message+= f"\n\nFind More info at:\n{response['data'][i]['url']} \n"
            message+='\n================================\n\n'
        print(message)
     


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
        
        

top_10()