# Offline-Elevator-Algorithm
This project will be focusing on planning and executing an offline algorithm for smart elevators.

What is offline algorithm?:

In an offline algorithm all the elevators calls are given in sdvance, including the calls' time, src floor and dest floor

*The algorith basics:*

load all calls
.
initiate the algorith:

    - initiate the building
    
    - initiate the calls list
    
    - initiate list of elevators' sources
    
    - initiate list of elevators' time of leaving sources
    
    - initiate list of elevators' destinations
    
    - initiate list of elevators' time of arrival to destination
    
for each call in calls list:

     for each elevator in elevators array:
     
        calculate estimated arrival time of elevator based on call time, sourse and destination and set min arrival time and save the elevator index
        
    if the call src and dest can fit inside currnt elevator run:
    
         change estimated arrival time to current elevator destnation to the current time plus two stop time
         
    if the call src is can fit in the current run but call's dest not:
    
       set elev destination to call's dest and set time to min time
       
    if both cant fit into the current elevator run:
    
       set elevator's start floor to call's src
       
       update elevator time of arrival to start to current dest arrival time plus the time from current dest to call's src plus two stops' time
       
       set elevator's dest floor to call's dest
       
       update elevator's time of arrival to dest to min time
   


After some previous research here are some relevant sources that are trying to tackle the problem of planning an efficient algorithm:

   1. This article form 2019 �The Hidden Science of Elevators� is discussing several questions such as what is even a perfect elevators' system? Is it the one that serves the person who waits the longest or one that get the nearest and quickest calls? Etc. :
https://www.popularmechanics.com/technology/infrastructure/a20986/the-hidden-science-of-elevators/


   2. This discussion from "thinksoftware.medium.com" which discuses the problem from a work interview angel, and there are few suggestions on how to tackle the problem and solve it. :
https://thinksoftware.medium.com/elevator-system-design-a-tricky-technical-interview-question-116f396f2b1c


   3. This work done by Ido Grinberg in 2014 in the subject of minimizing waiting times for elevators. In his work he goes in depth into the calculations and the effects of different approaches on the waiting time. In addition, he tries to find the answer to the problem in the case that an elevator is not going anywhere, what is the best place for it to be in order to minimize the waiting times:
https://idogreenberg.neocities.org/linked%20files/Articles/Elevators%20weighting%20time%20optimization.pdf


   4. This research optimizing elevators. In the research there are graphs representing the difference between various factors such as: up going calls and down going calls, the hours in the day when the waiting time are the longest, which floors have the longest waiting time etc. at the end of the research there are recommendations on how to execute an efficient elevator algorithm. :
https://towardsdatascience.com/elevator-optimization-in-python-73cab894ad30