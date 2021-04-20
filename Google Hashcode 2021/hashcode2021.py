#%%
fh = open('f.txt')
first_line = fh.readline()[:-1]
(time, intersections, streets, cars, score)  = tuple(first_line.split(' '))
(time, intersections, streets, cars, score) = (int(time), int(intersections), int(streets), int(cars), int(score))
print(time, intersections, streets, cars, score)

#%%
unique_streets = {}
for i in range(streets):
    (start, end, cur_street, traversal_time) = fh.readline()[:-1].split(' ')
    (start, end, traversal_time) = (int(start), int(end), int(traversal_time))
    print(start, end, cur_street, traversal_time)
    unique_streets[cur_street] = (start, end, traversal_time)
print(unique_streets)

#%%
car_paths = []
path_lengths = []
for i in range(cars):
    path = fh.readline()[:-1].split(' ')[1:]
    print(path)
    car_paths.append(path)
    path_lengths.append((i, len(path)))
    
path_lengths = sorted(path_lengths, key= lambda x:x[1])
print(path_lengths)
fh.close()

#%%
used_street_names = {}
intersection_data = {}
for i in range(len(path_lengths)):
    cur_car = path_lengths[i][0]
    cur_path = car_paths[cur_car]
    print(cur_car, cur_path)
    sim_time = 0
    prev_traversal_time = 0
    for j in range(len(cur_path)):
        street = cur_path[j]
        try:
            used_street_names[street] += 1
            continue
        except:
            used_street_names[street] = 0
            (start, end, traversal_time) = unique_streets[street] 
            try:
                    intersection_data[end].append(street)
            except:
                    intersection_data[end] = [street]
print(intersection_data)

#%%
fh = open('f_results.txt', 'w')
total_intersections = len(intersection_data.keys())
fh.writelines(str(total_intersections) + '\n')
for key in intersection_data.keys():
    fh.writelines(str(key) + '\n')
    total_streets = intersection_data[key]
    fh.writelines(str(len(total_streets)) + '\n')
    if len(total_streets) == 1:
        fh.writelines(total_streets[0] + ' 1 ' + '\n')
        continue
    else:
        for street_name in total_streets:
            fh.writelines(street_name + ' ' + str(total_streets.count(street_name)) + ' ' + '\n')
fh.close()
    

            
    