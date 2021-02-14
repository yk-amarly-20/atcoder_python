class Robot():

    def __init__(self, s_x: int, s_y: int, d_f: int, d_r: int,
                d_b: int, d_l: int):
        self.x = s_x
        self.y = s_y
        self.move_num = [d_f, d_r, d_b, d_l]
        self.Front = 0
        self.dic = {"F": 0, "R": 1, "B": 2, "L": 3}

    def drive(self, command: str, direction: str):
        if command == 't':
            self.turn(direction)
        elif command == 'm':
            self.move(direction)

    def turn(self, direction: str):
        self.Front = (self.Front + self.dic[direction]) % 4

    def move(self, direction: str):
        move_direction = (self.Front + self.dic[direction]) % 4
        masu = self.move_num[self.dic[direction]]
        if move_direction == 0:
            self.y += masu
        elif move_direction == 1:
            self.x += masu
        elif move_direction == 2:
            self.y -= masu
        else:
            self.x -= masu

    def __str__(self):
        return "{} {}".format(self.x, self.y)

def main():
    s_x, s_y = list(map(int, input().split()))
    d_f, d_r, d_b, d_l = list(map(int, input().split()))
    robot = Robot(s_x, s_y, d_f, d_r, d_b, d_l)
    n = int(input())

    for i in range(n):
        command, direction = input().split()
        robot.drive(command, direction)

    print(robot)

if __name__ == "__main__":
    main()
