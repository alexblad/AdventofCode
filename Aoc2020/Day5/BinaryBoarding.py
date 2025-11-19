## Part 1 Find the highest seat ID
seats = open('input.txt').read().splitlines()

def get_seat_id(seat):
    row = seat[:7].replace('F', '0').replace('B', '1')
    col = seat[7:].replace('L', '0').replace('R', '1')

    row_num = int(row, 2)
    col_num = int(col, 2)

    seat_id = (row_num * 8) + col_num
    return seat_id

seat_id = 0
for seat in seats:
    seat_id_new = get_seat_id(seat)
    if seat_id_new > seat_id:
        seat_id = seat_id_new

print(seat_id)

## Part 2 Find my seat ID
seat_ids = set()
for seat in seats:
    seat_ids.add(get_seat_id(seat))

for i in range(min(seat_ids), max(seat_ids)):
    if i not in seat_ids:
        print(i)
        break

## Visualize the seating arrangement
