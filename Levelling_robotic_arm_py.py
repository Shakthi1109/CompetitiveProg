#  0,[3,1,2,2],false

def solve(claw_pos, boxes, box_in_claw):
    total = sum(boxes) + (1 if box_in_claw else 0)
    n = len(boxes)
    avg = total // n
    remainder = total % n
    target = [avg + 1 if i < remainder else avg for i in range(n)]

    if box_in_claw:
        less = [i for i, v in enumerate(boxes) if v < target[i]]

        if not less:
            return "PLACE"

        closest = min(less, key=lambda i: abs(claw_pos - i))
        if claw_pos < closest:
            return "RIGHT"
        elif claw_pos > closest:
            return "LEFT"
        else:
            return "PLACE"

    else:
        more = [i for i, v in enumerate(boxes) if v > target[i]]

        closest = min(more, key=lambda i: abs(claw_pos - i))
        if claw_pos < closest:
            return "RIGHT"
        elif claw_pos > closest:
            return "LEFT"
        else:
            return "PICK"