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

    def sort(self):
        """
        Sort the robot's list.
        """
        
        # while light is not on, turn it on
        while not self.light_is_on():
            self.set_light_on()
            
            # lets go from left to right
            while self.can_move_right():
                # swap current with one in FRONT
                self.swap_item()
                # move right or stay in place
                self.move_right()
                
                # if compared item is greater than current, swap item
                if self.compare_item() == 1:
                    self.swap_item()
                    # turn light off to indicate False 
                    self.set_light_off()
                
                # check both sides of current
                # if it can move left and swap items, do it, else stay in place
                self.move_left()
                # swap item in FRONT of current
                self.swap_item()
                # if it can move right, it will, else it will stay in place
                self.move_right()
            
            # while loop for moving left now
            while self.can_move_left():
                # swap current with one in FRONT
                self.swap_item()
                # move Left or stay in place
                self.move_left()
                
                # if compared item is less than current, swap item
                if self.compare_item() == -1:
                    # swap with one in Front
                    self.swap_item()
                    # turn light off to indicate False
                    self.set_light_off()
                
                # check both sides again
                # if move right it will, else it'll stay in place
                self.move_right()
                # swap item in front
                self.swap_item()
                # move left, else stay in place
                self.move_left()

# trying to optimize for time
    def sort_2(self):
        while not self.light_is_on():
            self.set_light_on()

            while self.can_move_right():
                if self.compare_item() == 1:
                    self.move_right()
                    self.swap_item()
                    self.set_light_off()
                
            while self.can_move_left():
                if self.compare_item() == -1:
                    self.move_left()
                    self.swap_item()
                    self.set_light_off()




if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort_2()
    print(robot._list)