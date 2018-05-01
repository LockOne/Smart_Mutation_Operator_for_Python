f1 = open('repository_names', 'r')
for repo_name in f1:
    print(repo_name)
    repo_name = repo_name.strip()
    diffname = 'diffs/'+repo_name+'_diff'
    diff_file = open(diffname,'r',encoding="ISO-8859-1")
    new_diffname = 'diffs_modified/'+repo_name+'_diff_modified'
    new_diff_file = open(new_diffname, 'w')
    write1 = False
    minus = None
    for line in diff_file:
        if (line[0:6] == "commit"):
            write1 = False
        elif (line[0:4] == "diff"):
            line = line.rstrip()
            ext = line.split('.')[-1]
            write1 = (ext == 'py')

        if not write1:
            continue

        if (line[0:3] == '---' or line[0:3] == '+++'):
            continue

        if (line[0] ==  '-'):
            minus = line
        elif line[0] == '+':
            if minus is None:
                continue
            else:
                new_diff_file.write(minus)
                new_diff_file.write(line)
                minus = None
        
    diff_file.close()
    new_diff_file.close()
f1.close()
