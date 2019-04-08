
# coding: utf-8

# In[ ]:


def find_runner_up(prtcpt_scores):
    #Sorting the list in descending order
    list_prtcpt_scores = sorted(prtcpt_scores, reverse = True)
    for score in list_prtcpt_scores:
        if(-100 < score < 100):
            if score < max(list_prtcpt_scores):
                print(score)
                break

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

find_runner_up(arr)

