class Solution(object):
    def romanToInt(self, s):
        my_dict={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        if len(s)==1:
            return my_dict[s]
        else:
            resul=0
            for n in range (len(s)-1):
                actual_value=my_dict[s[n]]
                next_value=my_dict[s[n+1]]
                if(actual_value<next_value):
                    resul-=actual_value
                else: resul+=actual_value
            resul+=my_dict[s[-1]]
            return resul