## What would you do differently if you had more time?
    I would prove other alternatives for top100 function making test using "timeit" library to improve the time  
    and make tests with schedule library to ensure its functions.

## What is the runtime complexity of each function?
    Follow Big O notaiton  
    request_handled :  complexity = 1
    top100: complexity = n
    clear: 1 (but I'm not sure, I didn't have time to check schedule code)

## How does your code work?
    
    request_handled :  I save each ip in dictionary as a key and put the frecuency as a value, 
    top100: I sorted in reverse order by value of dictionary and return just the top 100.
    clear: I assigned a empty dictionary to "ip_group" and add schedule lybrary to run this function every day at 11:59:59 pm

## What other approaches did you decide not to pursue?
    Make test, prove the speed of top 100, validate each IP, ask for the version of python3.

## how would you test this?
    request_handled :  Simple unit test, pass a valid a IP and check if ip_group has this ip as a key.
    top100: making file with 1 million of ip and prove it  perform the time with timeit library.
    clear: simple unit test, move the time to 11:59:59 and check if "ip_group" is empty

