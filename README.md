# Leetcode-815-Hard-Modified-Bellman-Ford
A hard question asking for the sortest path from the start to the end. 
Comparing with other problems, it is not that hard if you know about which method to use and how to use that. 

There is a list initialized just like the png file I uploaded, listing the minimum bus required to get to some station. 
In the loop, constantly refresh the list and record the new shortest path.
Use the "flag" variable to see if the list is modified or not, to control the outermost while loop

After all, the list[target] will be the answer we want. 
(changes: If there is a useless bus, will that lead to any problems?)
