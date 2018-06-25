def command_help():
    command_list = '''
    ?hello -- Say hello, Everybot has feelings, even these in dungeons :<
    example :?hello
    
    ?bot -- Bot will tell me something about himself
    example :"?bot
    
    ?allow -- Allow certain roles to have immunity
    example :?allow <role>
    
    ?deny -- Take the role from the list
    example :?deny <role>
    
    ?play -- You can play any video from YT
    example :?play <yt link>
    
    ?stop -- Stop playing music
    example :?stop
    
    ?add_filter -- Bot will filter unwanted words in chat
    example :?add_filter Kitty
     
    ?rmv_filter -- Bot will remove specific word from unwanted words
    example :?rmv_filter Kitty
    
    ?curr -- Will tell you value of currencies to PLN
    example :?curr gbp 250
    '''

    return command_list
