test_list = [1,1,1,2,2,2,3,3,3,3,4,4,5,5,5,5,5,6,6,7,7,7]
drop_count = 0
my_arr = []
drop_queue = []
for items in range(len(test_list)):
  bool_pop = False
  my_arr.append(test_list[items])
  if my_arr.count(test_list[items]) > 3:
    bool_pop = True
    my_arr.pop()
    drop_count = drop_count + 1
    drop_queue.append(test_list[items])
  if items > 19 and test_list[items] - test_list[items - 20] < 10:
    bool_pop = True
    my_arr.pop()
    drop_count = drop_count + 1
    drop_queue.append(test_list[items])
  if items > 59 and test_list[items] - test_list[items - 60] < 30:
    bool_pop = True
    my_arr.pop()
    drop_count = drop_count + 1
    drop_queue.append(test_list[items])
  if my_arr.count(test_list[items]) < 3 and bool_pop is False and len(drop_queue) != 0 and test_list[items + 1] - test_list[items] > 0:
    my_arr.append(drop_queue.pop(0))
print(drop_count)
print(my_arr)
print(drop_queue)
