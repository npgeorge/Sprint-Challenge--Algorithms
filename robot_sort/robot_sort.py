class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"
    
#'''
#UPER
#Understand
# Sort of like insertion sort?
#
#- ALL: can_move_right, can_move_left, move_right, move_left, swap_item, compare_item, light on, light off, light indicator
#-----KEY-----
#- can_move_right --> true if can move right, false at end of list
#- can_move_left --> true if can move left, false if at start of list
#- move_right --> if it can, moves to the right and returns True, else stays in place and returns False
#- move_left --> if it can, moves to the left and returns True, else stays in place and returns False
#- swap_item --> swaps currently held with ***** list item in FRONT of it *****
#- compare_item --> compare held with item in front, if > return 1, if < return -1, if = return 0, if either is None, return None
#- set_light_on --> turn on robots light
#- ser_light_off --> turn off robots light
#- light_is_on --> True if on, False otherwise
#
#Plan
#- Robot should be able to travel one way down the list
#- while it can move left let it, compare & swap items out along the way
#- while it can move right let it, compare & swap items out along the way.
#- we can use the robot light to encompass the entire loop
#
#'''

# trying to optimize for time
    def sort(self):
        '''
        l = [4,17,8,10]

        understand current position
        understand current item
        compare current item to item in front (next item)
        for i in l:
            if current item is less than next item, do nothing
            elif current item is greater than next item, swap & move right
            elif current item is equal to next item, move right
            elif current item is None, move right
            else we are at the end of the list, traverse back from end of list to beginning

        '''

        # understand current position
        print("List to sort: ", l,
        "\nLength of list: ", (len(l)-1),
        "\nCurrent position: ", self._position, 
        "\nCan we move right? ", self.can_move_right(),
        "\nCan we move left?", self.can_move_left(),
        "\nCurrent value: ", self._item,
        "\nComparing next item: ", self.compare_item()
        )
        while self.can_move_right():
            self.swap_item()
            while self.can_move_right():
                # exits while loop when we can't move right any longer
                #pick up first item, begins with "None"
                self.move_right()
                if self.compare_item() == 1:
                    print('Swapped going from left right...')
                    y = self._item
                    print("Current value: ", y)
                    self.swap_item()
                    print("Compared ", y, " to ", self._item, "...")

                #if self.compare_item() == 1:
                #    print('Swapped going from left right...')
                #    y = self._item
                #    print("Current value: ", y)
                #    self.swap_item()
                #    print("Compared ", y, " to ", self._item, "...")
#
                #if self.can_move_right() == False:
                #    self.swap_item()

                #self.move_right()

                #print("----------------",
                #"\nList to sort: ", l,
                #"\nLength of list: ", (len(l)-1),
                #"\nCurrent position: ", self._position, 
                #"\nCan we move right? ", self.can_move_right(),
                #"\nCan we move left?", self.can_move_left(),
                #"\nCurrent value: ", self._item,
                #"\nComparing next item... ", self.compare_item()
                #)

            while self.can_move_left():
                self.move_left()
                if self.compare_item() == None:
                    print('Swapped coming back...')
                    x = self._item
                    print("Current value: ", x)
                    self.swap_item()
                    print("Swapped ", x, " for ", self._item, "...")
                    break

                if self.can_move_left() == False:
                    self.swap_item()

            self.move_right()
        
        print("-------FINAL SORT---------",
            #"\nList to sort: ", l,
            "\nLength of list: ", (len(l)-1),
            "\nCurrent position: ", self._position, 
            "\nCan we move right? ", self.can_move_right(),
            "\nCan we move left?", self.can_move_left(),
            "\nCurrent value: ", self._item,
            "\nComparing next item... ", self.compare_item()
            )
                

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]
    #l = [4,17,8,10,3]
    robot = SortingRobot(l)

    robot.sort_2()
    print(robot._list)