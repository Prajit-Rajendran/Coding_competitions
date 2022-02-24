#### ACCEPTING INPUT #######
import numpy as np 

fh = open('f_find_great_mentors.in.txt')  
#'a_an_example.in.txt', 'b_better_start_small.in.txt', 'c_collaboration.in.txt'
#'d_dense_schedule.in.txt', 'e_exceptional_skills.in.txt', 'f_find_great_mentors.in.txt'
content = fh.readline().split(' ')
N, M = int(content[0]), int(content[1])
print(N,M)

skills_dict = {}

for i in range(N):
    content = fh.readline().split(' ')
    name, S = content[0], int(content[1])
    #print(name, S)
    for j in range(S):
        content = fh.readline().split(' ')
        skill, level = content[0], int(content[1])
        #print(skill, level)
        if skill not in skills_dict.keys():
            skills_dict[skill] = {level : [name]}
        else:
            if level not in skills_dict[skill].keys():
                skills_dict[skill][level] = [name]
            else:
                skills_dict[skill][level].append(name)

project_scores = []
projects_req = {}

for i in range(M):
    content = fh.readline().split(' ')
    name, duration, score, best_before, no_of_roles = content[0], int(content[1]), int(content[2]),int(content[3]), int(content[4])
    #print(name, duration, score, best_before, no_of_roles)
    project_scores.append((name, score))
    for j in range(no_of_roles):
        content = fh.readline().split(' ')
        skill, level = content[0], int(content[1])
        #print(skill, level)
        if name not in projects_req.keys():
            projects_req[name] = {skill : [level]}
        elif skill not in projects_req[name].keys():
            projects_req[name][skill] = [level]
        else:
            projects_req[name][skill].append(level)

#print(projects_req['p244'])

project_scores.sort(key = lambda x: x[1], reverse=True) 
        
#print(skills_dict)
#print(project_scores)
#print(projects_req)

#%%
###### CHOOSING THE HIGHEST SCORING PROJECTS #######

projects_count = 0
assignment_tuple = []
for (a,b) in project_scores:
    project_name = a 
    skills_needed = list(projects_req[project_name].keys())
    #print(project_name, skills_needed)
    available = 1
    collaborators = []
    total_collab_needed = 0
    for skill in skills_needed:
        level_needed = projects_req[project_name][skill]
        total_collab_needed += len(level_needed)
        #print(skills_dict[skill])
        for key in skills_dict[skill]:
            used_collab = []
            for i in range(len(level_needed)):
                if key >= level_needed[i]:
                    #print(skills_dict[skill][key])
                    cur_collab = np.random.choice(skills_dict[skill][key])
                    while cur_collab not in used_collab:
                        if cur_collab not in used_collab:
                            break
                        cur_collab = np.random.choice(skills_dict[skill][key])
                    used_collab.append(cur_collab)
                    collaborators.append(cur_collab)
                    break
                    
    if len(collaborators) == total_collab_needed:
        projects_count += 1
        assignment_tuple.append((project_name, collaborators))
    #print(project_name, collaborators, len(collaborators),len(skills_needed), projects_count)
    
#print(projects_count)
#print(assignment_tuple)
#%%
###### OUTPUT FILE #######

fw = open('f_solutions.txt', 'w')
fw.writelines(str(projects_count) + '\n')
for i in range(len(assignment_tuple)):
    (project_name, collaborators) = assignment_tuple[i]
    fw.writelines(project_name  + '\n')
    collab_str = ' '.join(collaborators)
    fw.writelines(collab_str  + '\n')
fw.close()
                
    
