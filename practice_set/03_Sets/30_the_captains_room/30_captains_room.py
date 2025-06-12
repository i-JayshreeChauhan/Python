
"""
k = people in each group
here each group has K memebers - hence all room number appears k times (except the captains)
(sum(set(room_list)) * k)  --> as set contains all unique entries -- 
sum(room_list)) --> gives the actual sum of all rooms (memeber rooms appears k times and captain room appears 1 time)

ex :     (k * sum(unique_rooms) - sum(all_rooms)) = (k - 1) * captain_room  <---- difference will be k-1 times captains room as 1 time captain room is in sum

captain_room = ((sum(set(room_list)) * k) - sum(room_list)) // (k - 1)

"""

k = int(input())
room_list = list(map(int, input().split()))
captain = (sum(set(room_list)) * k - sum(room_list)) // (k - 1)
print(captain)
