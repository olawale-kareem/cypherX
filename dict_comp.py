
def dict_comp(stop, step):
    
    # item numbers count
    result_count = divmod(stop,step)
    total_item_count = result_count[0]
    total_item_count_range = total_item_count + 1
    item_list = [ f"items-{item}" for item in range(1, total_item_count_range)]
    
    

    # get the array list creacted
    # get the array factor 
    # destructure from the in-built divmod
    array_factor , _ = divmod(stop, step)
    # print the individual array inside a big one
    big_array_list = [] 
    # creating the small-small lists and push in the big one
    # list(range((step * i) + 1, (step * (i + 1)) + 1 ))
    big_array_list_filler = [ big_array_list.append(list(range((step * i) + 1, (step * (i + 1)) + 1 ))) for i in range(0, array_factor)]
    

    # combine them to  form the required display
    # create a list comprhension using item_list and big_array_list
    final_output = {f"{item_list[i]}": big_array_list[i]  for i in range(array_factor) }
    # print the output
    print (final_output)


dict_comp(100, 19)



