def solution(genres, plays):
    answer = []
    genres_dict = {}
    for i in range(len(genres)):
        if genres[i] in genres_dict:
            genres_dict[genres[i]].append(plays[i])
        else:
            genres_dict[genres[i]] = [plays[i]]
    
    genres_dict = sorted(genres_dict.items() , key = lambda x: sum(x[1]),reverse=True)
    for i in genres_dict:
        if len(i[1]) >= 2:
            i[1].sort(reverse= True)
            if i[1][0] == i[1][1] : 
                answer.append(plays.index(i[1][0]))
                answer.append(plays.index(i[1][1],plays.index(i[1][0])+1))
            else:
                answer.append(plays.index(i[1][0]))
                answer.append(plays.index(i[1][1]))
        else:
            answer.append(plays.index(i[1][0]))
    
    return answer