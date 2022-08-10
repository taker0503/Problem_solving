#요소 별로 오름차순 내림차순 정렬할 때
a_list.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))