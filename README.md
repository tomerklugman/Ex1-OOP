#  Ex1-OOP
## Useful links explaining the problem

1. [closest path to the elevator and optimization](https://softwareengineering.stackexchange.com/questions/331692/what-algorithm-is-used-by-elevators-to-find-the-shortest-path-to-travel-floor-or)
2. [visual representation and other problems](https://www.youtube.com/watch?v=xOayymoIl8U)
3. [explanation on programming ideas](https://www.youtube.com/watch?v=14Cc8IDWtFM)
4. [algorithm and program approach](https://www.geeksforgeeks.org/scan-elevator-disk-scheduling-algorithms/)
5. [differnt algirithm approaches and optimizations on differnt cases](https://www.youtube.com/watch?v=siqiJAJWUVg)

## algorithm explantation
in the offline algorithm we get calls upfront, and choose the elevator with the less time to reach. first each call will be reached by free elevators, after that we choose free and fastest elevator for that call or add its calls array. each elevator will get floors in its path and continue until reaches its call end.

## uml
![alt text](https://i.imgur.com/9lcfM9w.jpeg)

## how to run
choose b1-b5 then Calls_a-d 
```sh
py Ex1.py B1.json Calls_a.csv out.csv
```
then we get output file and run the simulator on it
```sh
java -jar Ex1_checker_V1.2_obf.jar 312723612 B1.json out.csv out.log
```
