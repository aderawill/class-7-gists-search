from gist_search.utils import get_gists


def search_gists(username, description=None, file_name=None):
    if not description and not file_name:
        print("At least one search parameter must be specified")
        return
    
    gists =  get_gists(username)
    if gists is None:
        print('Request failed')
        return
    if gists == []:
        print('Couldnt find gists for user {}'.format(username))
        return
    
    
    #Solution 1
    results = []
    for gist in gists:
        if description and description.lower() not in gist['description'].lower():
            continue
        if file_name:
            matched = False
            for json_fname in gist['files']:
                if file_name in json_fname:
                    matched = True
                    break
            if not matched:
                continue
        results.append(gist)
    return results    
            
    
    
    
    #           Solution 2
    # results = []
    # for gist in gists:
    #     if description and file_name:
    #         if description and description.lower() in gist['description'].lower():
    #             for json_fname in gist['files']:
    #                 if file_name in json_fname:
    #                     results.append(gist)
                        
    #     elif description and description.lower() in gist['description'].lower(): 
    #         results.append(gist)
        
    #     elif file_name:
    #         for json_fname in gist['files']:
    #                 if file_name in json_fname:
    #                     results.append(gist)
                
