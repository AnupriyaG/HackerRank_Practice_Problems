
# coding: utf-8

# In[ ]:


def string_validators(given_string):
    if(0 < len(given_string) <1000):
        print(any(i.isalnum() for i in given_string))
        print(any(i.isalpha() for i in given_string))
        print(any(i.isdigit() for i in given_string))
        print(any(i.islower() for i in given_string))
        print(any(i.isupper() for i in given_string))   

if __name__ == '__main__':
    s = input()
    string_validators(s)

