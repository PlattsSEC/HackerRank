x = int(raw_input())
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rem_dep(astring):

     my_set = set(astring)

     new_string = ""

     for i in astring:

          if i in my_set:
               new_string = new_string + i
               my_set = my_set - set(i)

     return new_string

def cipherkey(key):

    #someshit
    my_key = rem_dep(key)

    my_array = []

    my_array.append(list(my_key))

    my_len = len(my_key)

    i = 0

    #print(list(repetitions("SECRET")))


    #make new_letters here

    my_letters = letters

    for j in range(my_len):

        my_letters = my_letters.translate(None,my_key[j])
        #print("This is j :"+str(j))

    #print(letters)


    val = 0

    if ((26-my_len)%my_len==0):
         my_range = (26-my_len)/my_len
         for p in range(my_range):
              #something
              my_array.append(list(my_letters[val:val+my_len]))
              val = my_len + val
    else:
         my_range = ((26-my_len)/my_len)+1
         for p in range(my_range):
              
              #something
              my_array.append(list(my_letters[val:val+my_len]))
              val = my_len + val


    #print(my_array)

    my_column = []
    my_string = ""

    for k in range(my_len):

        for l in range(len(my_array)):

            try:
                my_string = my_string + my_array[l][k]
            except IndexError:
                continue                    

        my_column.append(my_string)
        my_string = ""

    '''
    for k in my_array:
         if k:
              #something
              my_column.append("".join(k))
    #print("This is my_array: "+str(my_array))
    print("This is my_column: "+ str(my_column))
    '''
    sort_string = ""

    for x in my_column:
        sort_string = sort_string + x[0]
    quickref = sorted(list(sort_string))
    #print(quickref)
    new_column = []
    for y in quickref:

        for z in my_column:

            if y in z:
                new_column.append(z)

            else:
                continue



    #print("This is new_column: "+ str(new_column))

    comp_string = "".join(new_column)
    #print("This is comp_string: "+ str(comp_string)+ str(len(comp_string)))
    return comp_string

def uncipher(key,text):

    my_string = ""
    letter_list = list(letters)

    ref = list(cipherkey(key))

    #print("This is ref"+str(ref)+" "+str(len(ref)))

    for i in text:
        my_string = my_string + letter_list[ref.index(i)]

    return my_string


for k in range(x):
    
    out_list = []
    key = raw_input()
    message = raw_input().split(" ")
    for u in message:
        out_list.append(uncipher(key,u))
    out_string = " ".join(out_list)
    print(out_string)
