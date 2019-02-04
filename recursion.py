college={"Name":"IMED", "Program":{"C_name":"MCA",'Fees':{'ist year':127000,'2ndyear':113000,'3rd year':None}}}

def print_dict(dictionary, ident = '', braces=1):
    """ Recursively prints nested dictionaries."""

    for key, value in dictionary.items():
        if isinstance(value, dict):
            print '%s%s%s%s' %(ident,braces*'[',key,braces*']')
            print_dict(value, ident+'  ', braces+1)
        else:
		if(value==None):
		        dictionary.pop(key,value)
		else:
			print ident+'%s = %s' %(key, value)


if __name__ == '__main__':
    print(college)
    print(" ")
    print_dict(college)