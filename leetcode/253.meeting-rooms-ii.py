from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        sorted_by_endtime = sorted(intervals, key=lambda t: t[0])

        # print(sorted_by_endtime)
        rooms = []
        for meet in sorted_by_endtime:
            find_room = False
            for room in rooms:
                if room[1] <= meet[0]:
                    room[1] = meet[1]
                    find_room = True
                    break
            if not find_room:
                rooms.append(meet)
            rooms = sorted(rooms, key=lambda t: t[0])
        #     print('rooms', rooms)
        # print(rooms)
        return len(rooms)


if __name__ == "__main__":
    sol = Solution()
    print(sol.minMeetingRooms([[0, 30],[5, 10],[15, 20]]))
    print(sol.minMeetingRooms([[2,15],[36,45],[9,29],[16,23],[4,9]]))
    print(sol.minMeetingRooms([[7,10],[2,4]]))